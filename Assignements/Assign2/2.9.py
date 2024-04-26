def Dig(No):
    Digit = 0
    iCnt = 0
    while No != 0:
        Digit = No % 10
        print(Digit)
        iCnt = iCnt + 1
        No = No // 10
    
    return iCnt

def main():

    No = int(input("Enter Number : "))

    Count = Dig(No)

    print("Number of digits are : " , Count)

if __name__ == "__main__":
    main()
        