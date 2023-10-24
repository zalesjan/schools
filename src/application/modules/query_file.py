import pandas as pd
import streamlit as st
from modules.send_email import send_report_email

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

def display_timetable(available_counts):

    # Define days of the week and slots in Czech
    days_of_week = ['Pondělí / Monday', 'Úterý / Tuesday', 'Středa / Wednesday', 'Čtvrtek / Thursday', 'Pátek / Friday']
    time_slots = ['7:00','8:00', '8:55', '10:00', '10:55', '12:45', '14:00', '14:50', '15:40','16:30', '17:20']

    # Define the updated activities list
    activities_list = ['Nic', 'Učím', 'Nepřímá', 'Doma', 'Dozor', 'Oběd']

    # Create an empty data frame to represent the time table
    time_table_data = pd.DataFrame(index=days_of_week, columns=time_slots)

    # Create a dictionary to store activity counts
    activity_counts = {activity: 0 for activity in activities_list}

    # Display the time table using Streamlit st.title(f"Rozvrh {looked_first_name} {looked_name} ")
    st.title(f"Zvol pro každý den a hodinu svou přímou (=učíš), nebo nepřímou pracovní dobu nebo praci z domu.\n Zvol taky, kdy máš oběd a kdy dozor.")

    # Info for users
    st.title(f"POZOR: KONTROLUJ SOUČTY DOLE\n MUSÍ ODPOVÍDAT TOMU, KOLIK MÁŠ PŘÍMÉ NEBO NEPŘÍMÉ PRACOVNÍ DOBY")
    
    #Employee inputs their name
    employee_name = st.text_input("Sem zadej své příjmení:")

    # Create a grid to display the time table
    for day in days_of_week:
        st.write(f"### {day}")
        cols = st.columns(len(time_slots))
        for time_slot in time_slots:
            activity = cols[0].radio(time_slot, activities_list, key=f"{day}_{time_slot}")
            time_table_data.loc[day, time_slot] = activity
            activity_counts[activity] += 1
            cols = cols[1:] + cols[:1]  # Shift columns to create a horizontal layout

    # Display the updated time table
    st.write("Aktualizovaný rozvrh")
    st.dataframe(time_table_data)
    
    # Display the activity counts
    st.write("Počet aktivit")
    for activity, count in activity_counts.items():
        st.write(f"{activity}: {count}")

    if st.button("KLIKNI SEM PRO ULOŽENÍ ROZVRHU A JEHO ODESLÁNÍ EKONOMCE"): 
        send_report_email(st.secrets["ekonomka_email"], employee_name, time_table_data, activity_counts)

    if count > available_counts.get(activity, 0):
        st.warning(f"Cannot select {activity}. Maximum count reached.")
