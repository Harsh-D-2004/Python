from copy import copy
import os
import shutil
import sys

def DirectoryWatcher(Dname , Ex1 , Ex2):

    exists = os.path.isdir(Dname)
    bVal = os.path.isabs(Dname)

    if bVal == False:

        Dname = os.path.abspath(Dname)

    if exists:

        for folder , subfolder , filename in os.walk(Dname):

            for fname in filename:
                copyfile()

                    
def main():

    if(len(sys.argv) == 4):

        try:
            DirectoryWatcher(sys.argv[1] , sys.argv[2] , sys.argv[3])

        except ValueError as vobj:

            print("Error : " , vobj)

        except Exception as eobj:

            print("Error : " , eobj)

if __name__ == "__main__":
    main()