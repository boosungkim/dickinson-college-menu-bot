import datetime
# import schedule
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from configparser import ConfigParser
import os
import subprocess

def main():
    # subprocess.run('')
    # Getting info to log in
    parser = ConfigParser()
    parser.read('config.ini')
    myEmail = str(parser.get('SensitiveData', 'myEmail'))
    myPassword = str(parser.get('SensitiveData', 'myPassword'))
    hostName = str(parser.get('SensitiveData', 'hostName'))
    smtpCode = int(parser.get('SensitiveData', 'smtpCode'))
    subject = "{} Dickinson Dining Menu".format("10/22/19's")

    recipientEmail = []
    with open('email.txt', 'r') as f:
        for line in f:
            line = line.strip()
            recipientEmail.append(str(line))
    # subject = "Today's Menu"
    msg = MIMEMultipart()
    msg['From'] = myEmail
    msg['To'] = ", ".join(recipientEmail)
    msg['Subject'] = subject

    message = ""
    with open('men.txt', 'r') as g:
        for ln in g:
            message = message + ln
    # print(message)
    msg.attach(MIMEText(message, 'plain'))
    
    server = smtplib.SMTP('127.0.0.1', smtpCode)
    server.starttls()
    server.login(myEmail, myPassword)
    text = msg.as_string()
    server.sendmail(myEmail, recipientEmail, text)
    server.quit()


if __name__ == "__main__":
    main()
