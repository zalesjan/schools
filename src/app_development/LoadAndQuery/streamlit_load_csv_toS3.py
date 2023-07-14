#Import the required libraries
import streamlit as st
import boto3
import botocore.exceptions

#Create the Streamlit app
# @st.cache
def get_s3_client():
    # Create an S3 client
    s3 = boto3.client('s3')
    return s3


def upload_file_to_s3(file, bucket_name):
    # Upload the file to S3
    s3_client = get_s3_client()
    try:
        s3_client.upload_fileobj(file, bucket_name, file.name)
        return True
    except botocore.exceptions.NoCredentialsError:
        st.error("Error: AWS credentials not found. Please configure your AWS credentials.")
        return False


def main():
    st.title("CSV File Uploader to S3 Bucket")
    st.write("Please select a CSV file to upload to your S3 bucket.")

    # Create a file uploader
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

    # Check if file is uploaded
    if uploaded_file is not None:
        if st.button("Upload"):
            # Pass the uploaded file to the upload_file_to_s3 function
            if upload_file_to_s3(uploaded_file, "schoolworkhours"):
                st.success("File uploaded successfully!")

if __name__ == '__main__':
    main()
