import psutil
import time

def CreateLog(Fname = "Marvellous.log"):

    fd = open(Fname , "w")
    seperator = "-"*70

    fd.write(seperator  + "\n")
    fd.write("Marvellous Proccess Log " + "\n")
    fd.write("Log file created at : " + time.ctime() + "\n")
    fd.write(seperator  + "\n")
    
    fd.write("Contents of Log File : " + "\n")
    fd.write(seperator  + "\n")

def main():

    CreateLog()

if __name__ == "__main__":
    main()