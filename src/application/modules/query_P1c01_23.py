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



def P1c01_23_count_people_by_department_stupen_trida_NO_PIVOT(bucket_name, file_name, department, show_result=False):
    # Query the file
    df = pd.read_csv(f"s3://{bucket_name}/{file_name}")

    # Filter data for the specified department
    department_df = df[df['department'] == department]

    # Create an empty DataFrame to store the count result
    count_result = pd.DataFrame(columns=['department', 'stupen', 'trida', 'count'])

    # Iterate over each 'platovy stupen' from 1 to 12
    for stupen in range(1, 13):
        # Filter data for the current 'platovy stupen'
        stupen_df = department_df[department_df['stupen'] == stupen]

        # Iterate over each 'platova trida' from 1 to 12
        for trida in range(1, 13):
            # Filter data for the current 'platova trida'
            trida_df = stupen_df[stupen_df['trida'] == trida]

            # Count the number of people in the current 'platova trida'
            count = len(trida_df)

            # Append the count result to the DataFrame
            count_result = pd.concat([count_result, pd.DataFrame({'department': [department], 'stupen': [stupen], 'trida': [trida], 'count': [count]})], ignore_index=True)

    if show_result:
        # Display the count result
        if not count_result.empty:
            st.write("Count Results:")
            st.write(count_result)
        else:
            st.warning("No matching records found.")

    return count_result



def P1c01_23_count_people_first_PIVOT(bucket_name, file_name, department, show_result=False):
    # Query the file
    df = pd.read_csv(f"s3://{bucket_name}/{file_name}")
    
    # Filter the data for the specified department
    filtered_data = df[df['department'] == department]
    
    # Pivot the data to get separate columns for each platova trida
    pivot_table = filtered_data.pivot_table(index=['department', 'stupen'], columns='trida', values='count', aggfunc='sum', fill_value=0)
    
    if show_result:
        # Display the pivot table
        if not pivot_table.empty:
            st.write("Count Results:")
            st.write(pivot_table)
        else:
            st.warning("No matching records found.")
    
    return pivot_table


def P1c01_23_count_people_by_department_stupen_trida(bucket_name, file_name, department, show_result=False):
    # Query the file
    df = pd.read_csv(f"s3://{bucket_name}/{file_name}")
    
    # Filter the data for the specified department
    filtered_data = df[df['department'] == department]
    
    # Pivot the data to get separate columns for each platova trida
    pivot_table = filtered_data.pivot_table(index=['department', 'stupen'], columns='trida', values='total_count', aggfunc='sum', fill_value=0)
    
    if show_result:
        # Display the pivot table
        if not pivot_table.empty:
            st.write("Count Results:")
            st.write(pivot_table)
        else:
            st.warning("No matching records found.")
    
    return pivot_table
