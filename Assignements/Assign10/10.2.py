import os
import sys

def DirectoryWatcher(Dname , Ex1 , Ex2):

    exists = os.path.isdir(Dname)
    bVal = os.path.isabs(Dname)

    if bVal == False:

        Dname = os.path.abspath(Dname)

    if exists:

        for folder , subfolder , filename in os.walk(Dname):

            for fname in filename:

                if fname.lower().endswith(Ex1):
                    File1 = os.path.join(folder , fname)
                    basename , _ = os.path.splitext(File1)
                    replaceName = basename + "." + Ex2
                    File2 = os.path.join(folder , replaceName)
                    os.rename(File1 , File2)

                    print("Change files : " , File2)

                    
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