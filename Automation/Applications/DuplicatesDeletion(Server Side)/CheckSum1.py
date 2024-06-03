import os
import sys
import hashlib

def hashfile(path , blocksize = 1024):

    afile = open(path , 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf)  > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)

    afile.close()
    return hasher.hexdigest()

def DisplayChecksum(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for dirName , subdirs , fileList in os.walk(path):
            print("Current folder is : " + dirName)

            for filen in fileList:
                path = os.path.join(dirName , filen)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print(' ')

    else:
        print("Invalid path")


def main():
    print("--------Marvellus Systems-----------------")

    print("Application name : " + sys.argv[0])

    if(len(sys.argv) == 1):
        print("Error : Invalid number of arguments")
        exit()

    if(sys.argv[1] == "-h") or (sys.argv[1] == "-H"):
        print("This script is used tot traverse directory and display checksum of files")
        exit()

    if(sys.argv[1] == "-u") or (sys.argv[1] == "-U"):
        print("usage : Name_Of_Application AbsolutePathofDirectory Extension")
        exit()

    try:
        arr = DisplayChecksum(sys.argv[1])

    except ValueError as vobj:
        print("Error : " , vobj)

    except Exception as E:
        print("Error : " , E)

if __name__ == "__main__":
    main()