import smtplib
from email.message import EmailMessage
import streamlit as st
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
from io import StringIO

def send_confirmation_email(email, code):
    # Compose the email message
    subject = "Confirmation Email"
    body = f"Thank you for using our service!\n\nYour verification code is: {code}\n\nPlease enter this code in the app to proceed with file querying."
    sender_email = st.secrets["sender_email"]
    recipient_email = email

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg.set_content(body)

    # Set up the SMTP connection
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = st.secrets["sender_email"]
    smtp_password = st.secrets["smtp_password"]

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send the email
        server.send_message(msg)

    st.warning("Confirmation email sent.")
    
def send_instructions_email(bucket_name, file_name):
    # Read CSV data
    df = pd.read_csv(f"s3://{bucket_name}/{file_name}")
    neprima = celkem_hodin - prima
    
    # Iterate through employee data
    for _, row in df.iterrows():
        employee_name = row["Name"]
        employee_firstname = row["FirstName"]
        employee_email = row["Email"]
        prima = row["direct hours"]
        celkem_hodin = row["hours"]
        job = row["job"]
        dept = row["department"]

        # Email configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_username = st.secrets["sender_email"]
        smtp_password = st.secrets["smtp_password"]

        # Compose the email message
        subject = "Informační Email"
        body = f"Vážený zaměstnanče,\n\n Zde jsou důležité informace k vašemu úvazku. \n\n"
        # Add relevant details from the row
        body += f"Jméno: {employee_firstname}\n"
        body += f"Příjmení: {employee_name}\n"
        body += f"Pozice: {job}\n"
        body += f"Sekce/oddělení: {dept}\n"
        body += f"Úvazek celkem: {celkem_hodin}\n"
        body += f"Přímá ped. činnost: {prima}\n"
        body += f"Nepřímá: {neprima}\n\n"
        body += f"Evidenci pracovní doby vyplňte za použití nástroje na tomto odkazu, prosím:\n\n https://schools-evydcdn7dfd3z483bpeekb.streamlit.app/ \n\n"

        # Construct email message
        message = MIMEMultipart()
        message["Subject"] = subject
        message["From"] = smtp_username
        message["To"] = employee_email

        message.attach(MIMEText(body, "plain"))

        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, employee_email, message.as_string())

        st.warning(f"Email sent to {employee_firstname} at {employee_email}")

def clean_content(content):
    # Remove linefeed and carriage return characters
    return content.replace('\n', '').replace('\r', '')


def send_report_email(email, employee_name, time_table_data, activity_counts):

    # Convert the employee data row into a CSV file
    csv_filename = f"{employee_name}_timetable.csv"
    time_table_data.to_csv(csv_filename, index=False)

    # Compose the email message
    subject = f"Evidence pracovní doby {employee_name}"
    body = f"Evidence pracovní doby {employee_name} je v příloze.\n\n"

    # Append the activity counts to the email body
    body += "Součty aktivit:\n"
    for activity, count in activity_counts.items():
        body += f"{activity}: {count}\n"

    sender_email = st.secrets["ekonomka_email"]
    recipient_email = email

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg.set_content(body)

    # Attach the CSV file
    with open(csv_filename, "rb") as file:
        msg.add_attachment(file.read(), maintype="text", subtype="csv", filename=csv_filename)

    # Set up the SMTP connection
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = st.secrets["ekonomka_email"]
    smtp_password = st.secrets["smtp_password"]

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send the email
        server.send_message(msg)

    st.warning(f"Evidence prac. doby zaměstnance {employee_name} odeslána na {recipient_email}.\n Pokud se ti ekonomka neozve zpátky, asi je vše ok:)")







    

