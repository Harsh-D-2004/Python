import os
import sys

def DirectoryWatcher(Dname , Fname):

    exists = os.path.isdir(Dname)
    bVal = os.path.isabs(Dname)

    if(bVal == False):
        Dname = os.path.abspath(Dname)

    if exists:
        print("Absolute path : " , Dname)
        for folder , subfolder , filename in os.walk(Dname):

            for fname in filename:
                FilePath = os.path.join(folder , fname)
                
                if(fname == Fname):
                    os.remove(FilePath)
                    print("Deleted File : " , fname)
                    break

    else:
        print("Directory does not exists")
        

def main():

    print("------------------------------------------------------------")
    print("-----------------------Directory Watcher--------------------")
    print("------------------------------------------------------------")

    if(len(sys.argv) == 2):
       
        if sys.argv[1] == "-h" or sys.argv[1] == "-H" :
           print("Help : ")
           print("Application travels the directory")
           print()

        elif sys.argv[1] == "-u" or sys.argv[1] == "-U":
           print("Usage of application : ")
           print("Name_Of_Application Directory_Name Name_Of_File")
           print() 

    if(len(sys.argv) == 3):

            try: 

                DirectoryWatcher(sys.argv[1] , sys.argv[2])

            except ValueError as vobj:

                print("Value error occured : " , vobj)

            except Exception as eobj:

                print("There is some error in application : " , eobj)         

    else:
        print("Type -h for help")
        print("Type -u for usage")
        print()

    print("------------------------------------------------------------")
    print("-----------------------Developed by Harsh-------------------")
    print("------------------------------------------------------------")

if __name__ == "__main__":
    main()