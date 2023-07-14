#Import the required libraries
import streamlit as st
import boto3
import botocore.exceptions

#Create the Streamlit app
def get_s3_client():
    # Create an S3 client
    s3 = boto3.client('s3')
    return s3


def upload_file_to_s3(file, bucket_name, school_name, city):
    # Generate the file name based on school name and city
    file_name = f"{school_name}_{city}_workhours.csv"

    # Upload the file to S3
    s3_client = get_s3_client()
    try:
        s3_client.upload_fileobj(file, bucket_name, file_name)
        return True
    except botocore.exceptions.NoCredentialsError:
        st.error("Error: AWS credentials not found. Please configure your AWS credentials.")
        return False


def main():
    st.title("CSV File Uploader to S3 Bucket")
    st.write("Please enter the name of the school and the city where the school is located.")

    # User input fields for school name and city
    school_name = st.text_input("School Name:")
    city = st.text_input("City:")

    # Create a file uploader
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

    # Check if file is uploaded
    if uploaded_file is not None:
        if st.button("Upload"):
            # Pass the uploaded file, bucket name, school name, and city to the upload_file_to_s3 function
            if upload_file_to_s3(uploaded_file, "schoolworkhours", school_name, city):
                st.success("File uploaded successfully!")

if __name__ == '__main__':
    main()
