def Calculations(No1 , No2):
    
    def Addition(X , Y):
        return X + Y
    
    def Subtraction(X , Y):
        return X - Y
    
    Ans1 = Addition(No1 , No2)
    Ans2 = Subtraction(No1 , No2)
    return Ans1 , Ans2

print("Enter First Number : ")
A = int(input())

print("Enter Second Number : ")
B = int(input())

Result1 , Result2 = Calculations(A , B)

print("Addition is : " , Result1)
print("Subtraction is : " , Result2)
