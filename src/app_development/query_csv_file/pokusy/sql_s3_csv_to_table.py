import streamlit as st
import boto3
import json
import pandas as pd

# Create an AWS Lambda client
lambda_client = boto3.client('lambda')

def invoke_lambda_function(payload):
    # Convert payload to bytes
    payload_bytes = json.dumps(payload).encode('utf-8')

    # Invoke the Lambda function with the provided payload
    response = lambda_client.invoke(
        FunctionName='sql_test',
        Payload=payload_bytes
    )
    return response

def main():
    st.title("CSV Query with Lambda and Streamlit")
    st.write("Enter your query parameters:")

    # Query input fields
    query_param1 = st.text_input("Parameter 1:")
    query_param2 = st.text_input("Parameter 2:")

    # Query button
    if st.button("Query"):
        # Prepare the payload to send to Lambda
        payload = {
            'param1': query_param1,
            'param2': query_param2
        }

        # Invoke the Lambda function
        response = invoke_lambda_function(payload)

        # Process the Lambda response
        if response['StatusCode'] == 200:
            query_result = response['Payload'].read()
            query_result = json.loads(query_result)
            df = pd.DataFrame.from_records(query_result)
            st.write("Query Results:")
            st.table(df)
        else:
            st.error("Error executing query.")

if __name__ == '__main__':
    main()
