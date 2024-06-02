import psutil

def CreateLog(Fname = "Marvellous.log"):

    fd = open(Fname , "w")
    seperator = "-"*70

    fd.write(seperator  + "\n")
    fd.write("Marvellous Log " + "\n")
    fd.write(seperator  + "\n")
    
    fd.write("Contents of Log File : " + "\n")
    fd.write(seperator  + "\n")

def main():

    CreateLog()

if __name__ == "__main__":
    main()