import streamlit as st
from modules.query_file import display_timetable, 
#add_time_range

def main():
    days_of_week = ['Pondělí', 'Úterý', 'Středa', 'Čtvrtek', 'Pátek']
    # Unused days 'Pondělí / Monday', 'Úterý / Tuesday', 'Středa / Wednesday', 'Čtvrtek / Thursday', 'Pátek / Friday'

    st.title("Rozvrh zaměstnance ZŠ Masarova")
    st.write("Rozvrh slouží k evidenci pracovní doby zaměstnanců")
    
    #looked_first_name = "ZŠ Masarova"
    #looked_name = "zaměstnance"
    available_counts = {"Učím": 10, "Nepřímá": 8, "Z domu": 20, "Dozor": 20, "Oběd": 20}

    # Define a dictionary to store the selected times for each day
    selected_times = {}
    
    display_timetable(available_counts, selected_times)

    # Loop through each day of the week
    #for day in days_of_week:
        #add_time_range(day, selected_times)

    # Display the selected time ranges
    #st.write("Selected Time Ranges:")
    #st.write(selected_times)

    #Add a button to dynamically add more time ranges
    #if st.button("Add Time Range"):
    #    new_day = st.selectbox("Select Day for the new time range:", days_of_week)    
  

if __name__ == '__main__':
    main()
