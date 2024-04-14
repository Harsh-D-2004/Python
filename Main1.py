def Addition(No1 , No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():

    print("Inside main")
    
    A = int(input("Enter the No1 : "))
    B = int(input("Enter the No2 : "))

    Result = Addition(A , B)

    print("Addition : " , Result)

main()
print("End of application")