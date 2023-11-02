import streamlit as st
from modules.query_file import display_timetable, select_indirect_activity

def main():
    st.title("Rozvrh zaměstnance ZŠ Masarova")
    st.write("Rozvrh slouží k evidenci pracovní doby zaměstnanců")
    
    #looked_first_name = "ZŠ Masarova"
    #looked_name = "zaměstnance"
    available_counts = {"Učím": 10, "Nepřímá": 8, "Z domu": 20, "Dozor": 20, "Oběd": 20}

    # Define a dictionary to store the selected times for each day
    selected_times = {}
    
    display_timetable(available_counts, selected_times)
    select_indirect_activity(available_counts, selected_times)
    
  

if __name__ == '__main__':
    main()
