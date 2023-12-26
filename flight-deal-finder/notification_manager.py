from dotenv import dotenv_values
import smtplib

# Load variables from .env file
config = dotenv_values(".env")

# Get the email address from .env file
MY_EMAIL = config.get("MY_EMAIL")  # Enter Your Email

# Set the email host (e.g., for Gmail: smtp.gmail.com)
EMAIL_HOST = 'smtp.gmail.com'  # Your email host, for example: smtp.gmail.com

# Get the password from .env file (if using Gmail, use your app password)
PASSWORD = config.get("PASSWORD")  # Your password (if using Gmail, check the smtplib documentation)

# Email address where you want to send the email
RECIPIENT_EMAIL  = config.get("RECIPIENT_EMAIL")  # The email address you want to send the email to

# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:
    def sent_mail(self, msg: str):
        with smtplib.SMTP(EMAIL_HOST) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECIPIENT_EMAIL ,
                msg=f'Subject:low-price flight\n\n{msg}'
            )

