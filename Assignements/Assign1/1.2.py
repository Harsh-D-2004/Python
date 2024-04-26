def ChkNum(No):

    if(No % 2 == 0):
        print("Even Number")

    else:
        print("Odd Number")

def main():

    No = int(input("Enter the number : "))

    ChkNum(No)

if __name__ == "__main__":
    main()