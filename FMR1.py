from functools import reduce


print("Demonstration of Filter Map Reduce")

def ChkEven(No):
    return(No % 2 == 0)

def Increase(No):
    return No + 2

def Add(A , B):
    return A + B

arr = [8 , 9 , 5 , 16 , 2 , 4 , 21 , 30 , 11]

evenArr = list(filter(ChkEven , arr))

print("Filtered Data : " , evenArr)

ModArray = list(map(Increase , evenArr))

print("Mapped result : " , ModArray)

sum = reduce(Add , ModArray)

print("Sum of mapped elements : " , sum)