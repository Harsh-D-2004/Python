import sys

def Add(No1 , No2):

    Ans = 0
    Ans = No1 + No2
    return Ans

def main():

    print("Welcome to application : " , sys.argv[0])

    Ans = 0

    if(len(sys.argv) != 3):
        print("Please provide two numbers")
        return

    Ans = Add(int(sys.argv[1]) , int(sys.argv[2]))

    print("Addition is : " , Ans)

if __name__ == "__main__":
    main()