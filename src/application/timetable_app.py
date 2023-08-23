import streamlit as st
from modules.query_file import display_timetable

def main():
    st.title("Timetable")
    st.write("This is the timetable page.")

    display_timetable(looked_first_name, looked_name, available_counts)

if __name__ == '__main__':
    main()
