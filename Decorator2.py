
def Sub(A , B):
    print(A - B)


def SmartSub(fptr):
    def inner(A, B):
        if A < B:
            A , B = B , A

        return fptr(A , B)
    return inner

Sub = SmartSub(Sub)

def main():
    No1 = int(input("Enter the No1 : "))
    No2 = int(input("Enter the No2 : "))

    Sub(No1 , No2)              

if __name__ == "__main__":
    main()