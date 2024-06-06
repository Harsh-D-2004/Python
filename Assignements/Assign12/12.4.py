import base64
from email import encoders
from email.mime.base import MIMEBase
import pickle
import socket
import psutil
import os
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

def CreateLogFile(Foldername = "Logs"):

    if not os.path.exists(Foldername):
        os.mkdir(Foldername)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" " , "")
    timestamp = timestamp.replace(":" , "_")
    Fname = "ProcessLog_%s.log"  %{timestamp}
    FileName = os.path.join(Foldername , Fname)
    
    FileName = os.path.abspath(FileName)

    fd = open(FileName , "w")
    seperator = "-"*70

    fd.write(seperator  + "\n")
    fd.write("Proccess Log " + "\n")
    fd.write("Log file created at : " + time.ctime() + "\n")
    fd.write(seperator  + "\n")

    Arr = GetProcessInfo()
    
    fd.write("Contents of Log File : " + "\n")
    fd.write(seperator  + "\n")

    for data in Arr:
        fd.write("%s \n"  %data)

    print("Log file created")

    fd.write(seperator  + "\n")  
    fd.close()

    return [Fname , FileName]

def GetProcessInfo():

    ret = []

    for proc in psutil.process_iter(['pid' , 'name' , 'username']):
        ret.append(proc)

    return ret

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
        starttime = time.time()

        socket.getaddrinfo('localhost', 8080)

        subject = "Process Logs"
        body = "This email contains changes happened during script execution"
        sender_email = "test703800@gmail.com"
        recipent_email = "hdoshi319@gmail.com"
        FileNameList = CreateLogFile()
        FilePath = FileNameList[1]
        Fname = FileNameList[0]


        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = sender_email
        message['To'] = recipent_email
        message.attach(MIMEText(body , "plain"))

        with open(FilePath , 'rb') as attachment:
            part = MIMEBase("application" , "octet-stream")
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
        print(f"Email sent successfully: {send_message['id']}")

        endtime = time.time()

        reqTime = endtime - starttime
        print("Required Time for execution : " , reqTime)

    except Exception as eobj:
        print('Unable to send mail : ' , eobj)

def main():

    SendMail()

if __name__ == "__main__":
    main()