import os
import shutil
import sys

def DirectoryWatcher(Dname1 , Dname2):

    exists = os.path.isdir(Dname1)
    bVal = os.path.isabs(Dname1)
    fileList = []

    if bVal == False:

        Dname1 = os.path.abspath(Dname1)

    if exists:

        for folder , subfolder , filename in os.walk(Dname1):

            for fname in filename:
                FilePath = os.path.join(folder , fname)
                fileList.append(FilePath)

        os.mkdir(Dname2)
        exists = os.path.isdir(Dname2)
        bVal = os.path.isabs(Dname2)
        
        if bVal == False:
            Dname2 = os.path.abspath(Dname2)

        if exists:

            for fpath in fileList:
                shutil.copy(fpath , Dname2)
                    
def main():

    if(len(sys.argv) == 3):

        try:
            DirectoryWatcher(sys.argv[1] , sys.argv[2])

        except ValueError as vobj:

            print("Error : " , vobj)

        except Exception as eobj:

            print("Error : " , eobj)

if __name__ == "__main__":
    main()