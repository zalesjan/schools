import streamlit as st
from modules.timetable_modules import display_timetable
#add_time_range

def main():
    days_of_week = ['Pondělí', 'Úterý', 'Středa', 'Čtvrtek', 'Pátek']
    # Unused days 'Pondělí / Monday', 'Úterý / Tuesday', 'Středa / Wednesday', 'Čtvrtek / Thursday', 'Pátek / Friday'

    st.title("Rozvrh zaměstnance ZŠ Masarova")
    st.write("Rozvrh slouží k evidenci pracovní doby zaměstnanců")
    
    #looked_first_name = "ZŠ Masarova"
    #looked_name = "zaměstnance"
    available_counts = {"Učím": 22, "Nepřímá": 18, "Z domu": 18, "Dozor": 20, "Oběd": 20}

    # Define a dictionary to store the selected times for each day
    #selected_times = {}
    
    # Loop through each day of the week
    #for day in days_of_week:
        #add_time_range(day, selected_times)

    # Display the selected time ranges
    #st.write("Selected Time Ranges:")
    #st.write(selected_times)

    #Add a button to dynamically add more time ranges
    #if st.button("Add Time Range"):
    #    new_day = st.selectbox("Select Day for the new time range:", days_of_week)    
  
    display_timetable(available_counts, days_of_week)
    
    #new_day = st.selectbox("Select Day for the new time range:", days_of_week)

    #for day in days_of_week:
    #    selected_times = cols_add_time_range(day, selected_times)

    #st.write(f"You previously selected doba od:   do  selected_times {selected_times}")

    # Display the selected time ranges
    #st.write("Selected Time Ranges:")
    #st.write(selected_times)
  
if __name__ == '__main__':
    main()
