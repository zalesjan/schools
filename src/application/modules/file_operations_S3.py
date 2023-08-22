import streamlit as st
import boto3
import botocore.exceptions

AWS_access_key_id = st.secrets["AWS_ACCESS_KEY_ID"]
AWS_secret_access_key = st.secrets["AWS_SECRET_ACCESS_KEY"]

s3 = boto3.client("s3", aws_access_key_id=AWS_access_key_id, aws_secret_access_key=AWS_secret_access_key)

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

def upload_file(file, bucket_name, file_name):
    s3 = boto3.client('s3')
    s3.upload_fileobj(file, bucket_name, file_name)
