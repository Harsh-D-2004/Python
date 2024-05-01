from MarvellousFMR import *

def main():

    Len = int(input("Enter nummber of elemnts : "))

    Data = list()

    print("Enter the elements : ")
    
    for i in range(0 , Len):
        No = int(input())
        Data.append(No)

    print("Data from input list : " , Data)

    FData = list(filterX(ChkEvenX , Data))

    print("Data after filter activity : " , FData)

    MData = list(mapX(IncreaseX , FData))

    print("Data after map activity : " , MData)

    Sum = reduceX(AddX , MData)

    print("Sum of elements : " , Sum)

if __name__ == "__main__":
    main()