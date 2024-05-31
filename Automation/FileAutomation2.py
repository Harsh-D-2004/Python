import sys

def Addition(No1 , No2):
    return No1 + No2

def main():
    print("------------------------------------------------------------")
    print("--------------Automation to perform Addition----------------")
    print("------------------------------------------------------------")

    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
        print("The script is used to perform addition of 2 integrals")
        exit()

    if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
        print("Usage of script")
        print("Name_Of_File First_Argument Second_Argument")
        print("Note : Both arguments should be in integral format")
        exit()

    Ret = Addition(int(sys.argv[1]) , int(sys.argv[2]))

    print("Addition : " , Ret)

if __name__ == "__main__":
    main()