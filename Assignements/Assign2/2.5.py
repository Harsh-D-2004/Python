def ChkPrime(No):

    for i in range(2 , No):

        if(No % i == 1):

            return ("It is prime")
        else:

            return ("It is not prime")

def main():
    print("Enter the number")
    Value = int(input())

    Ret = ChkPrime(Value)
    print(Ret)

if __name__ == "__main__":
    main()