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
