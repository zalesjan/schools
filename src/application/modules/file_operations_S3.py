import boto3
import botocore.exceptions

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

def upload_file(file, bucket_name, file_name):
    s3 = boto3.client('s3')
    s3.upload_fileobj(file, bucket_name, file_name)
