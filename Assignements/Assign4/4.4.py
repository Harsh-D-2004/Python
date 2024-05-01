
from functools import reduce


Even = lambda No : (No % 2 == 0)

Square =  lambda No : No**2

Add = lambda No1 , No2 : No1 + No2

def main():

    Arr = list()

    Size = int(input("Enter the size of elements : "))

    for  i in range(Size):

        No = int(input())
        Arr.append(No)

    ModArr = list(filter(Even , Arr))

    print(ModArr)

    Mod2Arr = list(map(Square , ModArr))

    print(Mod2Arr)

    Mod3Arr = reduce(Add , Mod2Arr)

    print(Mod3Arr)

if __name__ == "__main__":
    main()