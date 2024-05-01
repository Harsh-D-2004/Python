from functools import reduce

def main():

    Len = int(input("Enter nummber of elemnts : "))

    Data = list()

    for i in range(0 , Len):
        No = int(input())
        Data.append(No)

    print("Data from input list : " , Data)

    FData = list(filter((lambda No : (No % 2 == 0)) , Data))

    print("Data after filter activity : " , FData)

    MData = list(map((lambda No : (No + 1)) , FData))

    print("Data after map activity : " , MData)

    Sum = reduce((lambda A , B : (A + B)) , Data)

    print("Sum of elements : " , Sum)

if __name__ == "__main__":
    main()