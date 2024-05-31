
from Marvellous import Addition
from Marvellous import Multiplication

def main():
    print("Enter First Nimber : ")
    A = int(input())

    print("Enter Second Nimber : ")
    B = int(input())

    Ans = Addition(A , B)
    print("Addition is  : " , Ans)

    Ans = Multiplication(A , B)
    print("Multiplication is  : " , Ans)

main()