def ChkDiv(No):

    if(No % 5 == 0):

        print("Divisible")

    else:
        
        print("Not divisible")

def main():

    print("Enter number")
    value = int(input())

    ChkDiv(value)

if __name__ == "__main__":
    main()