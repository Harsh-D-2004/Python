
Ans = 0

def SumDigits(No):
    global Ans
    if (No > 0):
        Digit = No % 10
        Ans = Ans + Digit
        No = No // 10
        SumDigits(No)

    return Ans

def main():

    No = int(input('Enter the number : '))

    Ans = SumDigits(No)

    print("Sum = " , Ans)

if __name__ == "__main__":
    main()