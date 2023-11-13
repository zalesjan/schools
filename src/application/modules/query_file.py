import pandas as pd
import streamlit as st

def query_file(bucket_name, file_name, name, first_name, show_result=False):
    # Query the file
    df = pd.read_csv(f"s3://{bucket_name}/{file_name}")
    query_result = df[(df['Name'] == name) & (df['FirstName'] == first_name)]
    
    if show_result:
        # Display query result
        if not query_result.empty:
            st.write("Query Results:")
            st.write(query_result)
        else:
            st.warning("No matching records found.")
    
    # Return the query result
    return query_result

def query_someone(bucket_name, file_name, looked_name, looked_first_name, show_result=True):
    # Query the file
    df = pd.read_csv(f"s3://{bucket_name}/{file_name}")
    query_result = df[(df['Name'] == looked_name) & (df['FirstName'] == looked_first_name)]
    
    if show_result:
        # Display query result
        if not query_result.empty:
            st.write("Query Results:")
            st.write(query_result)
        else:
            st.warning("No matching records found.")
    
    # Return the query result
    return query_result

def show_certain_columns(bucket_name, file_name, name, first_name, show_result=False):
    # Query the file
    df = pd.read_csv(f"s3://{bucket_name}/{file_name}")
    query_result = df[(df['Name'] == name) & (df['FirstName'] == first_name)]
    
    # Select the desired columns
    columns_to_select = ['Name', 'FirstName', 'Gender', 'Email']
    query_result = query_result[columns_to_select]
    
    if show_result:
        # Display query result
        if not query_result.empty:
            st.write("Query Results:")
            st.write(query_result)
        else:
            st.warning("No matching records found.")
    
    # Return the query result
    return query_result
