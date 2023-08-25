import smtplib
from email.message import EmailMessage
import streamlit as st
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

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
    
    # Iterate through employee data
    for _, row in df.iterrows():
        employee_name = row["Name"]
        employee_firstname = row["FirstName"]
        employee_email = row["Email"]
        prima = row["direct hours"]
        celkem_hodin = row["hours"]
        job = row["job"]
        dept = row["department"]
        employee_email = row["Email"]

    # Compose the email message
    subject = " TEST Informační Email"
    body = f"Thank you"
    sender_email = st.secrets["sender_email"]
    recipient_email = employee_email

    # Email configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = sender_email
    smtp_password = st.secrets["smtp_password"]

    # Construct email message
    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = recipient_email

    # Add email body
    body += f"Hello {employee_name},\n\nHere is your employee information:\n\n"
    # Add relevant details from the row
    body += f"{employee_name}\n"
    # Add other details

    message.attach(MIMEText(body, "plain"))

    # Send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, employee_email, message.as_string())

    st.warning(f"Email sent to {employee_name} at {employee_email}")
