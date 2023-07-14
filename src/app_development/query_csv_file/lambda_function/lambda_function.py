import boto3
from pyspark.sql import SparkSession

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Retrieve the query parameters from the event
    param1 = event['param1']
    param2 = int(event['param2'])  # Assuming param2 is an integer

    # Retrieve the CSV file from S3
    bucket_name =  'schoolworkhours'
    file_name = 'Symptom-severity.csv'
    obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    csv_content = obj['Body'].read().decode('utf-8')

    # Create a Spark session
    spark = SparkSession.builder.appName('CSVQuery').getOrCreate()

    # Create a DataFrame from the CSV content
    df = spark.read.option('header', 'true').csv(spark.sparkContext.parallelize([csv_content]))

    # Perform the query on the DataFrame
    query_result = df.filter((df['FirstName'] == param1) & (df['ID'] > param2))

    # Convert the query result to a Pandas DataFrame for easier handling
    query_result_pandas = query_result.toPandas()

    # Return the query result
    return query_result_pandas.to_string(index=False)