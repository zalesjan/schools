import pandas as pd
import io
import streamlit as st
import boto3
import botocore.exceptions

# Create an S3 client
s3 = boto3.client('s3')

def file_exists(bucket_name, file_name):
    try:
        # Check if the file exists in the S3 bucket
        s3.head_object(Bucket=bucket_name, Key=file_name)
        return True
    except botocore.exceptions.ClientError as e:
        # File does not exist or user does not have access
        return False

def upload_file_to_s3(file, bucket_name, file_name):
    # Upload the file to S3
    try:
        s3.upload_fileobj(file, bucket_name, file_name)
        return True
    except botocore.exceptions.NoCredentialsError:
        st.error("Error: AWS credentials not found. Please configure your AWS credentials.")
        return False

def query_file(bucket_name, file_name, name, first_name):
    # Query the file in S3 for the given name and first name
    try:
        obj = s3.get_object(Bucket=bucket_name, Key=file_name)
        csv_content = obj['Body'].read().decode('utf-8')
        df = pd.read_csv(io.StringIO(csv_content))
        query_result = df[(df['Name'] == name) & (df['FirstName'] == first_name)]
        return query_result
    except botocore.exceptions.ClientError as e:
        # Error occurred while querying the file
        st.error("Error occurred while querying the file.")
        return None

def main():
    st.title("CSV File Uploader and Query")
    st.write("Please enter the following information:")

    # User inputs
    school_name = st.text_input("School Name")
    city = st.text_input("City")
    name = st.text_input("Name")
    first_name = st.text_input("First Name")

    # Generate the file name
    file_name = f"{school_name}_{city}_workhours.csv"

    if file_exists("schoolworkhours", file_name):
        # File already exists in S3
        st.warning("File already exists. Please fill in your personal information.")
        # last_name = st.text_input("Last Name")
        # position = st.text_input("Position")

        if st.button("Query"):
            # Query the file for the given name and first name
            query_result = query_file("schoolworkhours", file_name, name, first_name)
            if query_result is not None:
                st.write("Query Results:")
                st.write(query_result)
    else:
        # File does not exist in S3
        st.info("File does not exist. Please upload the file.")

        # File uploader
        uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

        if uploaded_file is not None:
            if st.button("Upload"):
                # Upload the file to S3
                if upload_file_to_s3(uploaded_file, "schoolworkhours", file_name):
                    st.success("File uploaded successfully!")

if __name__ == '__main__':
    main()
