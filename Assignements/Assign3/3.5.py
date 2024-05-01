import MarvellousNum as M

def AddPrime(Arr):

    Ans = 0

    for i in range(len(Arr)):

        if(M.ChkPrime(Arr[i]) == True):

            Ans = Ans + Arr[i]

    return Ans

def main():

    Arr = list()

    Size = int(input("Enter number of elements : "))

    for i in range(Size):
        No = int(input())
        Arr.append(No)

    Ret = AddPrime(Arr)

    print("Addition : " , Ret)


if __name__ == "__main__":
    main()