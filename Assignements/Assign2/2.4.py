def Fact(No):

    Ans = 1

    for i in range(No , 1 , -1):

        Ans = Ans + i

    return Ans

def main():
    
    No = int(input("Enter the number : "))

    Ans = Fact(No)

    print("Answer : " , Ans)

if __name__ == "__main__":
    main()