import Arithmetic as A 

def main():

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ans = A.Add(No1 , No2)
    print("The addition is : " , Ans)

    Ans = A.Subtract(No1 , No2)
    print("The subtraction is : " , Ans)

    Ans = A.Mult(No1 , No2)
    print("The multiplication is : " , Ans)

    Ans = A.Division(No1 , No2)
    print("The division is : " , Ans)

if __name__ == "__main__":
    main()