import sys
import os
import time

def DirectoryWatcher(Dname):
    flag = os.path.isabs(Dname)

    if(flag == False):
        print("Path is not absolute path")
        Dname = os.path.abspath(Dname)
        print("Converted path : " , Dname)
       
    exist = os.path.isdir(Dname)

    if(exist):
        for folder , subfolder , filenames in os.walk(Dname):
            for fname in filenames:
                print("File path is : " , os.path.join(folder , fname))

    else:
        print("No such directory")

def main():
    print("------------------------------------------------------------")
    print("--------------Directory Watcher----------------")
    print("------------------------------------------------------------")

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("The script is used to perform directory traversal")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of script")
            print("Name_Of_File Name_of_Directory")
            exit()

        try:
            starttime = time.time()
            DirectoryWatcher(sys.argv[1])
            endtime = time.time()

            print("Required time : " , endtime - starttime)

        except ValueError as obj1:
            print("Invalid type of arguments ")

        except Exception as obj2:
            print("Unable to perform task due to " , obj2)
    else:
        print("Use --h option to get help and --u option to get usage of application")
        print("Invalid Option")
        exit()

    print("--------------------------------------------------------")
    print("---------------------ThankYou For using out script------")
    print("----------------------Marvellous Infosystems------------")
    print("--------------------------------------------------------")


if __name__ == "__main__":
    main()