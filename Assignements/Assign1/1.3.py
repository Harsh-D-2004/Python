def Add(No1 , No2):

    return No1 + No2

def main():

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ans = Add(No1 , No2)

    print("Addition : " , Ans)

if __name__ == "__main__":
    main()