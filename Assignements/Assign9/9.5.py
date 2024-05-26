import os

def main():

    iCnt = 0

    Fname = input("Enter the name of file : ")

    fobj = open(Fname , "r")

    Str = input("Enter the word u want to search : ")

    for line in fobj:
        if line.find(Str):
            iCnt = iCnt + 1

    print("Freq : " , iCnt)

    fobj.close()

if __name__ == "__main__":
    main()