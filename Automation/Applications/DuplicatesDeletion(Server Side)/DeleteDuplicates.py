import datetime
import hashlib
import sys
import os
import datetime
import pytz
import time

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

    FileName = os.path.join(FolderName , "Logs_%s" %timestamp)
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
            writeLogFile()

        except ValueError as vobj:
            print('Error : ' , vobj)

        except Exception as eobj:
            print('Error : ' , eobj)

    print('----------------------------------------------------------------------------------------')
    print('----------------------------------------------------------------------------------------')
    print('----------------------------------------------------------------------------------------')

if __name__ == "__main__":
    main()