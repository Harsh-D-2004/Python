import datetime
import hashlib
import sys
import os
import datetime
import pytz
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

import base64
from email import encoders
from email.mime.base import MIMEBase
import pickle
import socket

def hashfile(path , blocksize = 1024):

    fd = open(path , "rb")
    hasher  = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)

    fd.close()
    return hasher.hexdigest()

def calculateCheckSum(Dname):

    bval = os.path.isabs(Dname)
    exists = os.path.isdir(Dname)
    dups = {}

    if bval == False:
        Dname = os.path.abspath(Dname)

    if exists:

        for folder , dubfolder , filenames in os.walk(Dname):

            for fname in filenames:
                path = os.path.join(folder , fname)
                filehasher = hashfile(path)
                
                if filehasher in dups:
                    dups[filehasher].append(path)
                else:
                    dups[filehasher] = [path]
    else:
        print('Directory does not exists')

    return dups

def DisplayDuplicates():

    dups = calculateCheckSum(sys.argv[1])

    result = list(filter(lambda x : len(x) > 1 , dups.values()))

    return result

def DeleteDuplicates():

    dups = calculateCheckSum(sys.argv[1])

    result = list(filter(lambda x : len(x) > 1 , dups.values()))

    ret = []

    iCnt = 0

    if len(result) > 0:

        print('Deleting duplicates')

        for res in result:
            for subres in res:
                
                iCnt += 1

                if iCnt < 2:
                    os.remove(subres)
                    ret.append(subres)
            iCnt = 0

        print('Duplicates Deleted')

    return ret

def writeLogFile(FolderName = "Logs"):

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" " , "")
    timestamp = timestamp.replace(":" , "_")
    Fname = "Logs_%s" %timestamp
    FileName = os.path.join(FolderName , Fname)
    current_time = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))

    fd = open(FileName , "w")
    
    seperator = "-"*70

    fd.write(seperator + '\n')
    fd.write("DUPLICATE FILE CLEANER LOG FILE" + '\n')
    fd.write("Date/Time : " + current_time + '\n')
    fd.write(seperator + '\n')
    fd.write("Logs : " + '\n')
    fd.write(seperator + '\n')

    LogList = DisplayDuplicates()

    if len(LogList) > 0:

        fd.write('Duplicates found' + '\n')
        print("Duplicates found")

        for res in LogList:
            for subres in res:
                fd.write(subres + '\n')
                fd.write(" ")

        fd.write(seperator + '\n')

        fd.write("Deleted Files : " + '\n')

        LogList2 = DeleteDuplicates()
    
        for fname in LogList2:
            fd.write(fname + '\n')
        
        fd.write(seperator + '\n')
        print("Note : Logs written in log file with latest timestamp in folder named : " + FolderName)

    else:

        fd.write('Duplicates not found' + '\n')
        print("Duplicates not found")

    return [Fname , FileName]

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

        subject = "Duplicate File Deletion Logs"
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

    print('----------------------------------------------------------------------------------------')
    print('-----------------------------------Duplicates Cleaner-----------------------------------')
    print('----------------------------------------------------------------------------------------')

    if len(sys.argv) == 1:
        print("Invalid number of arguments")

    if sys.argv[1] == "-h" or sys.argv[1] == "-H":
        print("Help")
        print("This is the application to delete duplicate files in directory")

    if sys.argv[1] == "-u" or sys.argv[1] == "-U":
        print("Usage")
        print("Name_Of_Application Directory_name")

    else:

        try:          
            SendMail()

        except ValueError as vobj:
            print('Error : ' , vobj)

        except Exception as eobj:
            print('Error : ' , eobj)

    print('----------------------------------------------------------------------------------------')
    print('----------------------------------------------------------------------------------------')
    print('----------------------------------------------------------------------------------------')

if __name__ == "__main__":
    main()