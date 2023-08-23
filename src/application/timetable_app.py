import streamlit as st
from modules.query_file import display_timetable

def main():
    st.title("Timetable")
    st.write("This is the timetable page.")
    
    looked_first_name = "John"
    looked_name = "Doe"
    available_counts = {"Učím": 10, "Nepřímá": 8, "Z domu": 20, "Dozor": 20, "Oběd": 20}
    display_timetable(looked_first_name, looked_name, available_counts)

if __name__ == '__main__':
    main()
