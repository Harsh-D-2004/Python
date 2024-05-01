Ans = 1

def fact(No):

    global Ans

    if(No>= 1):

        Ans = Ans * No
        No = No - 1
        fact(No)

    return Ans

def main():

    No = int(input("Enter the number : "))

    Ans = fact(No)

    print("Ans = " , Ans)

if __name__ == "__main__":
    main()

