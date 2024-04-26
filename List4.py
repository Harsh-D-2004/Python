def Addition(Data):
    Sum = 0

    for no in Data:
        Sum = Sum + no

    return Sum

def main():

    No = int(input("Enter Number of elements : "))

    Arr = list()

    print("Enter the elements : ")

    for i in range(No):
        no = int(input())
        Arr.append(no)

    print(Arr)

    Result = Addition(Arr)
    print("Addition is : " , Result)

if __name__ == "__main__":
    main()