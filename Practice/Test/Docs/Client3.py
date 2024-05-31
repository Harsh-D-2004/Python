
import Marvellous as M

def main():
    print("Enter First Nimber : ")
    A = int(input())

    print("Enter Second Nimber : ")
    B = int(input())

    Ans = M.Addition(A , B)
    print("Addition is  : " , Ans)

    Ans = M.Multiplication(A , B)
    print("Multiplication is  : " , Ans)

main()