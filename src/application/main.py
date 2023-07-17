import streamlit as st
from modules.file_operations_S3 import check_file_exists
from modules.file_operations_S3 import upload_file
from modules.query_file import query_file
<<<<<<< HEAD
from modules.query_form_P1c1_2023 import P1c01_23_count_people_by_department_stupen_trida
=======
from modules.query_file import show_certain_columns
>>>>>>> master
from modules.send_confirm_email import send_confirmation_email
from modules.validate_code import validate_code

def main():
<<<<<<< HEAD
    job = 'director'
    department = 'operation' 
    stupen = 8
    trida = 5
=======
>>>>>>> master
    bucket_name = "schoolworkhours"
    entered_code = None
    query_result = None
    email_sent = False  # Initialize email_sent variable
    st.title("CSV File Uploader to S3 Bucket")
    st.write("Please enter the school name and city.")

    # Get user input for school name and city
    school_name = st.text_input("School Name:")
    city = st.text_input("City:")
    # Generate the file name
    file_name = f"{school_name}_{city}_workhours.csv"

    if not check_file_exists(bucket_name, file_name):
        # File does not exist, prompt for file upload
        st.write("File does not exist. Please upload the file.")
        # Create a file uploader
        uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
        if uploaded_file is not None:
            if st.button("Upload"):
                # Upload the file to S3
                upload_file(uploaded_file, bucket_name, file_name)
                st.success("File uploaded successfully!")
            
    # Check if the file exists in S3
    if check_file_exists(bucket_name, file_name):
        # File exists, prompt for personal information
        st.warning("File found in the storage. Give your name and First Name")
        # Prompt for personal information
        name = st.text_input("Name:")
        first_name = st.text_input("First Name:")
        query_result = query_file(bucket_name, file_name, name, first_name)

        #If file was already uploaded
        #if query_result is not None:
        # Get the email from the query result
        if not query_result.empty:
            email = query_result["Email"].values[0]
        else:
            st.warning("No matching records found.")
            return  # Exit the function if no matching records are found

        # Generate the verification code (school name + random 2-digit number)
        import random
        code = f"{school_name}_{random.randint(10, 99)}"

        # Send the confirmation email with the code
        if not email_sent:
            send_confirmation_email(email, code)
            email_sent = True

        # Prompt for the code
        entered_code = st.text_input("Enter the code:")

        # Validate the code
        #if entered_code is not None:
        if validate_code(entered_code, school_name):
            st.success("Code validated! You can now query the files.")

            # Perform file querying
            if st.button("Query Files"):
                P1c01_23_count_people_by_department_stupen_trida(bucket_name, file_name, department, show_result=True)
                if not validate_code (entered_code, school_name):
                    st.warning("Invalid code. Please try again.")


if __name__ == '__main__':
    main()
