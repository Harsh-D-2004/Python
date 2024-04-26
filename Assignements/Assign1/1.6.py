def ChkNum(No):

    if(No < 0):
        print("negavite")

    else:
        print("Positive")

def main():

    No = int(input("Enter the number : "))

    ChkNum(No)

if __name__ == "__main__":
    main()