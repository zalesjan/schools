import pandas as pd
import streamlit as st

job_position = 'teacher'
department = 'school' 
platovy_stupen = '14'
platova_trida = '14'

def P1c01_23(bucket_name, file_name, job_position, department, platovy_stupen, platova_trida, show_result=False):
    # Query the file
    df = pd.read_csv(f"s3://{bucket_name}/{file_name}")
    query_result = df[(df['job/position'] == job_position) & (df['department'] == department) & 
                      (df['platovy stupen'] == platovy_stupen) & (df['platova trida'] == platova_trida)]
    
    if show_result:
        # Display query result
        if not query_result.empty:
            st.write("Query Results:")
            st.write(query_result)
        else:
            st.warning("No matching records found.")
    
    # Return the query result
    return query_result
