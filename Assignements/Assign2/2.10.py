def Dig(No):
    Digit = 0
    iCnt = 0
    Ans = 0
    while No != 0:
        Digit = No % 10
        Ans = Ans + Digit
        iCnt = iCnt + 1
        No = No // 10
    
    return Ans

def main():

    No = int(input("Enter Number : "))

    Count = Dig(No)

    print("Addition of digits is : " , Count)

if __name__ == "__main__":
    main()
        