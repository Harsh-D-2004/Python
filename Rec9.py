i = 1
Ans = 1
def DisplayR(No):

    global i
    global Ans

    if(No >= 1):

        Ans = Ans * No
        No = No - 1
        DisplayR(No)

    return Ans

def main():

    No = int(input("Enter the number : "))

    Ans = DisplayR(No)

    print("Answer : " , Ans)

if __name__ == "__main__":
    main()