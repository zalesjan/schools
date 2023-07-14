import pandas as pd
from io import StringIO

import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Retrieve the query parameters from the event
    param1 = event['param1']
    param2 = event['param2']  # Assuming param2 is an integer

    # Retrieve the CSV file from S3
    bucket_name = 'synthschooldata'
    file_name = 'synth_data3.csv'
    obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    csv_content = obj['Body'].read().decode('utf-8')

    # Create a DataFrame from the CSV content
    # df = pd.read_csv(pd.compat.StringIO(csv_content))
    # Read the CSV data using StringIO
    df = pd.read_csv(StringIO(csv_content))

    # Print the DataFrame to verify its contents
    print("DataFrame Contents:")
    print(df)
    
    # Perform the query on the DataFrame
    query_result = df.loc[(df['Name'] == param1) & (df['FirstName'] == param2)]

    # Return the query result
    return query_result.to_string(index=False)