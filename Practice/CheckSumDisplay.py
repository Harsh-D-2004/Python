import hashlib
import sys
import os
from turtle import update

def hashfile(path , blocksize = 1024):

    fd = open(path , "rb")
    hasher  = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)

    fd.close()
    return hasher.hexdigest()

def DisplayCheckSum(Dname):

    bval = os.path.isabs(Dname)
    exists = os.path.isdir(Dname)

    if bval == False:
        Dname = os.path.abspath(Dname)

    if exists:

        for folder , dubfolder , filenames in os.walk(Dname):

            print('Current directory : ' , folder)

            for fname in filenames:
                path = os.path.join(folder , fname)
                print(path)
                filehasher = hashfile(path)
                print(filehasher)
                print(" ")

def main():

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

            DisplayCheckSum(sys.argv[1])

        except ValueError as vobj:
            print('Error : ' , vobj)

        except Exception as eobj:
            print('Error : ' , eobj)


if __name__ == "__main__":
    main()