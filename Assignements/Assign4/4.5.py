
from functools import reduce


Prime = lambda No : all(No % i != 0 for i in range(2 , No))

Mult =  lambda No : No*2

Max = lambda No1 , No2 : (No1 if(No1 > No2) else No2)

def main():

    Arr = list()

    Size = int(input("Enter the size of elements : "))

    for  i in range(Size):

        No = int(input())
        Arr.append(No)

    ModArr = list(filter(Prime , Arr))

    print(ModArr)

    Mod2Arr = list(map(Mult , ModArr))

    print(Mod2Arr)

    Mod3Arr = reduce(Max , Mod2Arr)

    print(Mod3Arr)

if __name__ == "__main__":
    main()