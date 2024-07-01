import schedule # type: ignore
import time
import smtplib
from email.message import EmailMessage
from django.core.mail import send_mail # type: ignore


def demo(self):
    msg="This is a test email sent every 1 minute!"
    Subject= "Test Email"
    From= "kundatwadshubhangi@gmail.com"
    To = ["aasma.shaikh2406@gmail.com"]

    send_mail(Subject, msg
              , From,To)
schedule.every(1).minutes.do(demo)  # Run every 1 minute



# Create your views here.
