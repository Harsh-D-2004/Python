import psutil
import time
import schedule

def CreateLog(Fname = "Marvellous.log"):

    fd = open(Fname , "a")
    seperator = "-"*70

    fd.write(seperator  + "\n")
    fd.write("Marvellous Proccess Log " + "\n")
    fd.write("Log file created at : " + time.ctime() + "\n")
    fd.write(seperator  + "\n")

    Arr = GetProcessInfo()
    
    fd.write("Contents of Log File : " + "\n")
    fd.write(seperator  + "\n")

    for data in Arr:
        fd.write("%s \n"  %data)

    fd.write(seperator  + "\n")  

    fd.close()

    print("Log file created")

def GetProcessInfo():

    listprocess = []

    for proc in psutil.process_iter(['pid' , 'name' , 'username']):
        listprocess.append(proc.info)

    return listprocess

def main():

    schedule.every(2).minutes.do(CreateLog)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()