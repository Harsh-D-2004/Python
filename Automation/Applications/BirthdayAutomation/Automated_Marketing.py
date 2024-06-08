import base64
import csv
import datetime
import os
import pickle
import socket
import time
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pytz
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from twilio.rest import Client


def ReadCSV():
    FilePath = os.path.join("Test", "Data.csv")

    Data = []

    with open(FilePath, mode='r') as file:
        csv_reader = csv.DictReader(file)

        for lines in csv_reader:
            Data.append(lines)

    return Data


def EmailList():
    Data = ReadCSV()
    BDayEmailList = dict()
    BDayMobileList = dict()

    today = datetime.now().strftime('%m-%d')

    for line in Data:
        name = line.get('Name')
        birthday = line.get('Birthdate')
        mobile = line.get('MobileNo')
        email = line.get('Email')

        if birthday == today:
            BDayEmailList[name] = email
            BDayMobileList[name] = mobile

    return BDayEmailList, BDayMobileList


SCOPES = ['https://www.googleapis.com/auth/gmail.send']


def get_credentials():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds


def SendMail():
    try:

        BdayEmailList, _ = EmailList()
        receivermail = []
        name = []

        if len(BdayEmailList) == 0:
            print("No ones bday today")
            return

        for key, value in BdayEmailList.items():
            name.append(key)
            receivermail.append(value)

        for i in range(len(name)):
            socket.getaddrinfo('localhost', 8080)

            subject = "Happy Birthday !!"
            body = '''Dear %s,

🎉 Happy Birthday! 🎂

 We hope your special day is filled with joy, laughter, and everything you love. Thank you for being a valued part of our family. Enjoy your day to the fullest!

Warm wishes,
Team''' % (name[i].upper())

            sender_email = "test703800@gmail.com"
            recipent_email = receivermail[i]

            message = MIMEMultipart()
            message['Subject'] = subject
            message['From'] = sender_email
            message['To'] = recipent_email
            message.attach(MIMEText(body, "plain"))

            raw = base64.urlsafe_b64encode(message.as_string().encode("utf-8"))
            raw = raw.decode("utf-8")

            creds = get_credentials()
            service = build('gmail', 'v1', credentials=creds)
            message = {'raw': raw}

            send_message = service.users().messages().send(userId="me", body=message).execute()
            print(f"Birthday Email sent successfully: {send_message['id']}")

        return True

    except Exception as eobj:
        print('Unable to send mail : ', eobj)
        return False


def sendWpMsg():
    try:

        _, BdayMobileList = EmailList()

        account_sid = 'ACa09094216067a484f566ae616529022e'
        auth_token = '8c0a21abf96198659a3f7ca31309a7ac'
        client = Client(account_sid, auth_token)

        for key, value in BdayMobileList.items():
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body='''Dear %s,

🎉 Happy Birthday! 🎂

We hope your special day is filled with joy, laughter, and everything you love. Thank you for being a valued part of our family. Enjoy your day to the fullest!

Warm wishes,
Team''' % key,
                to='whatsapp:+91%s' % value
            )

            print("Msg sent successfully with msg id : ", message.sid)

        return True

    except Exception as eobj:
        print("Error : ", eobj)

        return False


def writeLogFile(FolderName="Logs"):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ", "")
    timestamp = timestamp.replace(":", "_")

    FileName = "Logs_%s" % timestamp

    FilePath = os.path.join(FolderName, FileName)
    current_time = str(datetime.now(pytz.timezone('Asia/Kolkata')))

    fd = open(FilePath, "w")

    seperator = "-" * 70

    fd.write(seperator + '\n')
    fd.write("AUTOMATED MARKETING SCRIPT LOG FILE" + '\n')
    fd.write("Date/Time : " + current_time + '\n')
    fd.write(seperator + '\n')
    fd.write("Logs : " + '\n')
    fd.write(seperator + '\n')

    BdayEmailList, BdayMobileList = EmailList()

    if len(BdayEmailList) == 0:
        fd.write("No ones bday today" + '\n')

    bVal1 = SendMail()
    bVal2 = sendWpMsg()

    if bVal1:

        for key, value in BdayEmailList.items():
            fd.write("Email sent to %s on email %s" % (key, value) + '\n')
            fd.write(" ")

    if bVal2:

        for key, value in BdayMobileList.items():
            fd.write("Message sent successfully to %s on Mobile Number : %s" % (key, value) + '\n')
            fd.write(" ")

    else:
        fd.write("Some error occured" + '\n')
        fd.write(" ")

    fd.write(seperator + '\n')
    print("Note : Logs written in log file with latest timestamp in folder named : " + FolderName)

    return [FileName, FilePath]


def SendLogMail():
    try:
        starttime = time.time()

        socket.getaddrinfo('localhost', 8080)

        subject = "Automated Marketing Script Logs"
        body = "This email contains changes happened during script execution"
        sender_email = "test703800@gmail.com"
        recipent_email = "hdoshi319@gmail.com"
        FileNameList = writeLogFile()
        FilePath = FileNameList[1]
        Fname = FileNameList[0]

        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = sender_email
        message['To'] = recipent_email
        message.attach(MIMEText(body, "plain"))

        with open(FilePath, 'rb') as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)

        part.add_header("Content-Disposition", f"attachment; filename= {Fname}")

        message.attach(part)

        raw = base64.urlsafe_b64encode(message.as_string().encode("utf-8"))
        raw = raw.decode("utf-8")

        creds = get_credentials()
        service = build('gmail', 'v1', credentials=creds)
        message = {'raw': raw}

        send_message = service.users().messages().send(userId="me", body=message).execute()
        print(f"Log Email sent successfully: {send_message['id']}")

        endtime = time.time()

        reqTime = endtime - starttime
        print("Required Time for execution : ", reqTime)

    except Exception as eobj:
        print('Unable to send mail : ', eobj)


def main():
    # schedule.every().day.at("00:00").do(SendLogMail)

    # while(True):
    #     schedule.run_pending()

    SendLogMail()


if __name__ == "__main__":
    main()
