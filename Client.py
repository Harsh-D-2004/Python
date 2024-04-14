
import Marvellous

def main():
    print("Enter First Nimber : ")
    A = int(input())

    print("Enter Second Nimber : ")
    B = int(input())

    Ans = Marvellous.Addition(A , B)
    print("Addition is  : " , Ans)

    Ans = Marvellous.Multiplication(A , B)
    print("Multiplication is  : " , Ans)

main()