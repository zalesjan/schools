import pandas as pd
import streamlit as st

def P1c01_23_count_people_by_department_stupen_trida(bucket_name, file_name, show_result=False):
    # Query the file
    df = pd.read_csv(f"s3://{bucket_name}/{file_name}")

    # Filter data for the specified department
    #department_df = df[df['department'] == department]

    # Group by 'stupen' and 'trida' and calculate the count
    count_result = df.groupby(['department', 'stupen', 'trida']).size().reset_index(name='count')

    # Create the pivot table to rearrange the 'trida' values as columns
    pivot_table = count_result.pivot_table(index=['department', 'stupen'], columns='trida', values='count', aggfunc='sum', fill_value=0)

    # Reset the index to convert the 'stupen' back to a regular column
    pivot_table = pivot_table.reset_index()

    if show_result:
        # Display the count result
        if not pivot_table.empty:
            st.write("Count Results:")
            st.write(pivot_table)
        else:
            st.warning("No matching records found.")

    return pivot_table