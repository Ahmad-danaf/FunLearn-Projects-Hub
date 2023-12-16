import smtplib

# Fill in your private information below:
MY_EMAIL = ''  # Enter Your Email
EMAIL_HOST = ''  # Your email host, for example: smtp.gmail.com
PASSWORD = ''  # Your password (if using Gmail, use your app password). Refer to the smtplib documentation.
EMAIL_ADDRS = ''  # The email you want to send to



# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:
    def sent_mail(self, msg: str, url: str):
        with smtplib.SMTP(EMAIL_HOST) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=EMAIL_ADDRS,
                msg=f"Subject:Amazon Price Alert!\n\n{msg}\n{url}".encode("utf-8")
            )

