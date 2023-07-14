import streamlit as st
import boto3
import botocore.exceptions
import pandas as pd
import smtplib
from email.message import EmailMessage
import random

# Create an S3 client
s3 = boto3.client('s3')

from  def check_file_exists 

GONE query file 

GONE send conf email

GONE validate_code

def main():
    query_result = None
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
        st.warning("File found in the storage. Please try to find yourself in the file. Give your name and First Name")
        # Prompt for personal information
        name = st.text_input("Name:")
        first_name = st.text_input("First Name:")
        query_result = query_file("schoolworkhours", file_name, name, first_name)
        
        #If file was already uploaded
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
        send_confirmation_email(email, code)

        # Prompt for the code
        entered_code = st.text_input("Enter the code:")

        # Validate the code
        if validate_code(entered_code, school_name):
            st.success("Code validated! You can now query the files.")

            # Perform file querying
            if st.button("Query Files"):
                query_file("schoolworkhours", file_name, name, first_name, show_result=True)
        else:
            st.warning("Invalid code. Please try again.")


if __name__ == '__main__':
    main()
