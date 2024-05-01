from functools import reduce


def ChkEven(No):
    return (No % 2 == 0)

def Increase(No):
    return No + 1

def Add(A , B):
    return A + B

def main():

    Data = [11 , 14 , 20 , 23 , 18 , 16 , 15 , 20]

    print("Data from input list : " , Data)

    FData = list(filter(ChkEven , Data))

    print("Data after filter activity : " , FData)

    MData = list(map(Increase , FData))

    print("Data after map activity : " , MData)

    Sum = reduce(Add , Data)

    print("Sum of elements : " , Sum)

if __name__ == "__main__":
    main()