import os
import sys

def DirectoryWatcher(Dname , Extension):

    exists = os.path.isdir(Dname)
    bVal = os.path.isabs(Dname)

    if bVal == False:

        Dname = os.path.abspath(Dname)

    if exists:

        for folder , subfolder , filename in os.walk(Dname):

            for fname in filename:

                File = os.path.join(folder , fname)

                if fname.lower().endswith(Extension):

                    print("File name" , fname)

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