import sys

def Min(Arr):

    Min = sys.maxsize

    for i in range(len(Arr)):

        if(Arr[i] < Min):
            Min = Arr[i]

    return Min

    
    
def main():

    Arr = list()

    Size = int(input("Enter number of elements : "))

    for i in range(Size):
        No = int(input())
        Arr.append(No)

    Ret = Min(Arr)

    print("Min : " , Ret)

if __name__ == "__main__":
    main()
    