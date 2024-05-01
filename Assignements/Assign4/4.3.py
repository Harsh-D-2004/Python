
from functools import reduce


More = lambda No : ((No >= 70) and (No < 90))

Increase =  lambda No : (No + 10)

Add = lambda No1 , No2 : No1 + No2

def main():

    Arr = list()

    Size = int(input("Enter the size of elements : "))

    for  i in range(Size):

        No = int(input())
        Arr.append(No)

    ModArr = list(filter(More , Arr))

    print(ModArr)

    Mod2Arr = list(map(Increase , ModArr))

    print(Mod2Arr)

    Mod3Arr = reduce(Add , Mod2Arr)

    print(Mod3Arr)

if __name__ == "__main__":
    main()