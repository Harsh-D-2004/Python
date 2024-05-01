def Freq(Arr , No):

    iCnt = 0

    for i in range(len(Arr)):

        if(Arr[i] == No):
            iCnt = iCnt + 1

    return iCnt

def main():

    Arr = list()

    Size = int(input("Enter number of elements : "))

    for i in range(Size):
        No = int(input())
        Arr.append(No)

    Target = int(input("Enter target element : "))

    Ret = Freq(Arr , Target)

    print("Freq : " , Ret)


if __name__ == "__main__":
    main()