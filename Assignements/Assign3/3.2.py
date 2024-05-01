def Max(Arr):

    Max = 0
    for i in range(len(Arr)):

        if(Arr[i] > Max):
            Max = Arr[i]

    return Max

    
    
def main():

    Arr = list()

    Size = int(input("Enter number of elements : "))

    for i in range(Size):
        No = int(input())
        Arr.append(No)

    Ret = Max(Arr)

    print("Max : " , Ret)

if __name__ == "__main__":
    main()
    