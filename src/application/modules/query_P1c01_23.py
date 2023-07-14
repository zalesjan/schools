import pandas as pd
import streamlit as st


def prepare_for_P1c01_23(bucket_name, file_name, job, department, stupen, trida, show_result=False):
    # Query the file
    df = pd.read_csv(f"s3://{bucket_name}/{file_name}")
    query_result = df[(df['job'] == job)  & (df['department'] == department) & (df['trida'] == trida) & (df['stupen'] == stupen)]
    
    if show_result:
        # Display query result
        if not query_result.empty:
            st.write("Query Results:")
            st.write(query_result)
        else:
            st.warning("No matching records found.")
    
    # Return the query result
    return query_result
