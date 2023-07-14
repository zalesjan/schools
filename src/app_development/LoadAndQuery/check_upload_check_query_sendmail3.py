import streamlit as st
import boto3
import botocore.exceptions
import pandas as pd
import smtplib
from email.message import EmailMessage

# Create an S3 client
s3 = boto3.client('s3')

def check_file_exists(bucket_name, file_name):
    try:
        # Check if the file exists in S3
        response = s3.head_object(Bucket=bucket_name, Key=file_name)
        return True
    except botocore.exceptions.ClientError as e:
        # File does not exist in S3
        if e.response['Error']['Code'] == '404':
            return False
        else:
            raise

def query_file(bucket_name, file_name, name, first_name, show_result=False):
    # Query the file
    df = pd.read_csv(f"s3://{bucket_name}/{file_name}")
    query_result = df[(df['Name'] == name) & (df['FirstName'] == first_name)]
    
    if show_result:
        # Display query result
        if not query_result.empty:
            st.write("Query Results:")
            st.write(query_result)
        else:
            st.warning("No matching records found.")
    
    # Return the query result
    return query_result

def send_confirmation_email(email, code):
    # Compose the email message
    subject = "Confirmation Email"
    body = f"Thank you for using our service!\n\nYour verification code is: {code}\n\nPlease enter this code in the app to proceed with file querying."
    sender_email = "zalesjan@gmail.com"
    recipient_email = email

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg.set_content(body)

    # Set up the SMTP connection
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = sender_email
    smtp_password = "mpzfssutfpcelqbm"

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send the email
        server.send_message(msg)

    st.warning("Confirmation email sent.")
    
    # Set email_sent flag to True if email is successfully sent
    email_sent = True
    return email_sent

def validate_code(code, school_name):
    # Split the code into components
    code_components = code.split("_")

    # Check if the code has the expected number of components
    if len(code_components) != 2:
        return False

    # Extract the code components
    extracted_school_name, extracted_code = code_components

    # Validate the code
    if extracted_school_name.lower() == school_name.lower() and extracted_code.isdigit() and len(extracted_code) == 2:
        return True
    else:
        return False

def main():
    query_result = None
    email_sent = False  # Initialize email_sent variable
    st.title("CSV File Uploader to S3 Bucket")
    st.write("Please enter the school name and city.")

    # Get user input for school name and city
    school_name = st.text_input("School Name:")
    city = st.text_input("City:")
    # Generate the file name
    file_name = f"{school_name}_{city}_workhours.csv"

    if not check_file_exists("schoolworkhours", file_name):
        # File does not exist, prompt for file upload
        st.write("File does not exist. Please upload the file.")
        # Create a file uploader
        uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
        if uploaded_file is not None:
            if st.button("Upload"):
                # Upload the file to S3
                s3.upload_fileobj(uploaded_file, "schoolworkhours", file_name)
                st.success("File uploaded successfully!")
           
    # Check if the file exists in S3
    if check_file_exists("schoolworkhours", file_name):
        # File exists, prompt for personal information
        st.warning("File found in the storage. Give your name and First Name")
        # Prompt for personal information
        name = st.text_input("Name:")
        first_name = st.text_input("First Name:")
        query_result = query_file("schoolworkhours", file_name, name, first_name)
        
        #if query_result is not None:
        # Get the email from the query result
        if not query_result.empty:
            email = query_result["Email"].values[0]
        else:
            st.warning("No matching records found.")
            return  # Exit the function if no matching records are found

        # Generate the verification code (school name + random 2-digit number)
        import random
        code = f"{school_name}_{random.randint(10, 99)}"

        # Send the confirmation email with the code
        if not email_sent:
            send_confirmation_email(email, code)
            email_sent = True

        # Prompt for the code
        entered_code = st.text_input("Enter the code:")

        # Validate the code
        if validate_code(entered_code, school_name):
            st.success("Code validated! You can now query the files.")

            # Perform file querying
            if st.button("Query Files"):
                query_file("schoolworkhours", file_name, name, first_name, show_result=True)
                if not validate_code(entered_code, school_name):
                    st.warning("Invalid code. Please try again.")


if __name__ == '__main__':
    main()
