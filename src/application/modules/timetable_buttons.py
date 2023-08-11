import streamlit as st
import pandas as pd
available_counts = {"Učím": 1, "Nepřímá": 20, "Z domu": 20, "Dozor": 20, "Oběd": 20}

# Define days of the week and slots in Czech
days_of_week = ['Pondělí / Monday', 'Úterý / Tuesday', 'Středa / Wednesday', 'Čtvrtek / Thursday', 'Pátek / Friday']
time_slots = ['7:00','8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00','16:00', '17:00']

# Define the updated activities list
activities_list = ['Nic', 'Učím', 'Nepřímá', 'Doma', 'Dozor', 'Oběd']

# Create an empty data frame to represent the time table
time_table_data = pd.DataFrame(index=days_of_week, columns=time_slots)

# Create a dictionary to store activity counts
activity_counts = {activity: 0 for activity in activities_list}

# Display the time table using Streamlit
st.title("Rozvrh")

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

if count > available_counts.get(activity, 0):
    st.warning(f"Cannot select {activity}. Maximum count reached.")