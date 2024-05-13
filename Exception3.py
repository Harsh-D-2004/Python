def main():
    
    Ans = 0

    try:
        No1 = int(input("Enter the first number : "))
        No2 = int(input("Enter the second number : "))
        Ans = No1 / No2

    except ZeroDivisionError as zobj:

        print("Exception occured : " , zobj)

    except ValueError as vobj:

        print("Exception occured : " , vobj)

    except Exception as eobj:

        print("Exception Occured : " , eobj)

    print("Division is : " , Ans)

if __name__ == "__main__":
    main()