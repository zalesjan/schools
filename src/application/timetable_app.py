import streamlit as st
from modules.query_file import display_timetable

def main():
    st.title("Rozvrh zaměstnance ZŠ Masarova")
    st.write("Rozvrh slouží k evidenci pracovní doby zaměstnanců")
    
    looked_first_name = "ZŠ Masarova"
    looked_name = "zaměstnance"
    available_counts = {"Učím": 10, "Nepřímá": 8, "Z domu": 20, "Dozor": 20, "Oběd": 20}
    
    display_timetable(looked_first_name, looked_name, available_counts)
    
  

if __name__ == '__main__':
    main()
