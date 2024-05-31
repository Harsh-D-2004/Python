import sys

def Addition(No1 , No2):
    return No1 + No2

def main():
    print("------------------------------------------------------------")
    print("--------------Automation to perform Addition----------------")
    print("------------------------------------------------------------")

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("The script is used to perform addition of 2 integrals")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of script")
            print("Name_Of_File First_Argument Second_Argument")
            print("Note : Both arguments should be in integral format")
            exit()

        else:
            print("Invalid Option")
            print("Use --h option to get help and --u option to get usage of application")
            exit()

    if(len(sys.argv) == 3):
        try:
            Ret = Addition(int(sys.argv[1]) , int(sys.argv[2]))
            print("Addition : " , Ret)
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