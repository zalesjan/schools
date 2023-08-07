import streamlit as st
from modules.file_operations_S3 import check_file_exists, upload_file
from modules.query_file import query_file, show_certain_columns, query_someone
from modules.query_form_P1c1_2023 import P1c01_23_count_people_by_department_stupen_trida
from modules.send_confirm_email import send_confirmation_email
from modules.validate_code import split_names, old_validate_code

def main():
    department = 'operation'
    bucket_name = "schoolworkhours"
    sent_code = None
    entered_code = None
    query_result = None
    st.title("PAM")
    st.write("Prosím zadejte jméno školy a město/Please enter the school name and city.")

    # Get user input for school name and city
    school_name = st.text_input("Jméno školy/School Name:")
    city = st.text_input("Město/City:")
    # Generate the file name
    file_name = f"{school_name}_{city}_workhours.csv"

    if not check_file_exists(bucket_name, file_name):
        # File does not exist, prompt for file upload
        st.write("Seznam PAM je třeba nahrát. / School not found. Please upload.")
        # Create a file uploader
        uploaded_file = st.file_uploader("Nahrej seznam PAM. / Upload a CSV file", type="csv")
        if uploaded_file is not None:
            if st.button("Nahrej/Upload"):
                # Upload the file to S3
                upload_file(uploaded_file, bucket_name, file_name)
                st.success("Nahrávání poroběhlo úspěšně! / File uploaded successfully!")
            
    # Check if the file exists in S3
    if check_file_exists(bucket_name, file_name):
        # File exists, prompt for personal information
        st.warning("Soubor nalezen. Zajete své jméno. / File found. Give your name.")
        # Prompt for personal information
        name = st.text_input("Příjmení: / Name:")
        first_name = st.text_input("Jméno: / First Name:")
        query_result = query_file(bucket_name, file_name, name, first_name)
        
        name_and_surname = st.text_input("Jméno a příjmení hledané osoby: / Name and surname of looked person:")
        looked_name, looked_first_name = split_names(name_and_surname)
        
        # Extract the email adress and job from the query result
        if not query_result.empty:
            email = query_result["Email"].values[0]
            job = query_result["job"].values[0]
        else:
            st.warning("No matching records found.")
            return  # Exit the function if no matching records are found

        import random
        sent_code = f"{school_name}_{random.randint(10, 99)}"

        # Send the confirmation email with the code
        if st.button("Pošli potvrzovací mail. / Send me confirmation email"):
            # Generate the verification code (school name + random 2-digit number)
            send_confirmation_email(email, sent_code)

        # Prompt for the code
        entered_code = st.text_input("Zadej kód z mailu. / Enter the code:")    

        # Validate the code
        if old_validate_code(sent_code, entered_code):
            st.success("Code validated! You can now query the files.")

            # Check if the job is equal to "director"
            if job.lower() != "director":
                # Let non/priviledged user query himself
                if st.button("Ukaž moje podrobnosti. / Show my data."):
                    query_someone(bucket_name, file_name, name, first_name, show_result=True)
                
            # Perform file querying for the director
            else:
                # Perform query for specific froms 
                if st.button("Vypocitej P1c01_23"):
                    P1c01_23_count_people_by_department_stupen_trida(bucket_name, file_name, department, show_result=True)

                # Let director query all employees
                if st.button("Hledat cloveka. / Find employee."):
                    query_someone(bucket_name, file_name, looked_name, looked_first_name, show_result=True)    

                if not old_validate_code (sent_code, entered_code):
                    st.warning("Invalid code. Please try again.")
        else:
            st.warning("Invalid code. Please try again.")

if __name__ == '__main__':
    main()
