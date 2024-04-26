

def main():

    No = int(input("Enter Number of elements : "))

    Arr = list()

    print("Enter the elements : ")

    for i in range(No):
        no = int(input())
        Arr.append(no)

    print(Arr)

if __name__ == "__main__":
    main()