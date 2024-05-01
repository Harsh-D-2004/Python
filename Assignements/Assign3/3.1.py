from functools import reduce


def Add(Arr):
    
    Ans = 0
    for i in range(len(Arr)):
        Ans = Ans + Arr[i]

    return Ans

def main():

    Size = int(input('Enter the number of elements : '))

    Arr = list()

    for i in range(Size):

        No = int(input())
        Arr.append(No)

    Ans = Add(Arr)

    print("Ans : " , Ans)

if __name__ == "__main__":
    main()