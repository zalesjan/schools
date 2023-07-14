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

def query_file(bucket_name, file_name, name, first_name):
    # Query the file
    df = pd.read_csv(f"s3://{bucket_name}/{file_name}")
    query_result = df[(df['Name'] == name) & (df['FirstName'] == first_name)]
    # Display query result
    if not query_result.empty:
        st.write("Query Results:")
        st.write(query_result)
    else:
        st.warning("No matching records found.")

def send_confirmation_email(email):
    # Compose the email message
    subject = "Confirmation Email"
    body = "This is your confirmation email message."
    sender_email = "zalesjan@gmail.com"
    recipient_email = email

    msg = EmailMessage()
    msg["Subject"] = subjectck
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg.set_content(body)

    # Set up the SMTP connection
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = sender_email
    smtp_password = "9227341K2CU3VFK9"

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send the email
        server.send_message(msg)

    st.warning("Confirmation email sent.")

def main():
    st.title("CSV File Uploader to S3 Bucket")
    st.write("Please enter the school name and city.")

    # Get user input for school name and city
    school_name = st.text_input("School Name:")
    city = st.text_input("City:")
    # Generate the file name
    file_name = f"{school_name}_{city}_workhours.csv"

    # Check if the file exists in S3
    if check_file_exists("schoolworkhours", file_name):
        # File exists, prompt for personal information
        st.warning("File already exists. Please fill in your personal information.")
        # Prompt for personal information
        name = st.text_input("Name:")
        first_name = st.text_input("First Name:")
        # Query the file
        query_file("schoolworkhours", file_name, name, first_name)
    else:
        # File does not exist, prompt for file upload
        st.write("File does not exist. Please upload the file.")
        # Create a file uploader
        uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
        if uploaded_file is not None:
            if st.button("Upload"):
                # Upload the file to S3
                s3.upload_fileobj(uploaded_file, "schoolworkhours", file_name)
                st.success("File uploaded successfully!")
        if check_file_exists("schoolworkhours", file_name):
            # File exists, prompt for personal information
            st.warning("File found in the storage. Please try to find yourself in the file. Give your name and First Name")
            # Prompt for personal information
            name = st.text_input("Name:")
            first_name = st.text_input("First Name:")
            query_file("schoolworkhours", file_name, name, first_name)

    if check_file_exists:
        # Query the file and get the result
        query_result = query_file("schoolworkhours", file_name, name, first_name)

        # Check if query_result is not empty
        if not query_result.empty:
            # Show the query result
            #st.write("Query Result:")
            #st.write(query_result)

            # Get the email from the query result
            email = query_result["Email"].values[0]

            # Send the confirmation email
            send_confirmation_email(email)


if __name__ == '__main__':
    main()
