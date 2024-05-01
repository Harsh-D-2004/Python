from functools import reduce


def ChkEven(No):
    return (No % 2 == 0)

def Increase(No):
    return No + 1

def Add(A , B):
    return A + B

ChkEvenX = lambda No : (No % 2 == 0)

IncreaseX = lambda No : (No + 1)

AddX = lambda A , B : (A + B)

def main():

    Data = [11 , 14 , 20 , 23 , 18 , 16 , 15 , 20]

    print("Data from input list : " , Data)

    FData = list(filter(ChkEvenX , Data))

    print("Data after filter activity : " , FData)

    MData = list(map(IncreaseX , FData))

    print("Data after map activity : " , MData)

    Sum = reduce(AddX , Data)

    print("Sum of elements : " , Sum)

if __name__ == "__main__":
    main()