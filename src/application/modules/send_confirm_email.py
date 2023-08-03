import smtplib
from email.message import EmailMessage
import streamlit as st

def send_confirmation_email(email, code):
    # Compose the email message
    subject = "Confirmation Email"
    body = f"Thank you for using our service!\n\nYour verification code is: {code}\n\nPlease enter this code in the app to proceed with file querying."
    sender_email = "zalesjan@gmail.com"
    recipient_email = email

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg.set_content(body)

    # Set up the SMTP connection
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = sender_email
    smtp_password = "mpzfssutfpcelqbm"

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send the email
        server.send_message(msg)

    st.warning("Confirmation email sent.")
    