import sys

def Addition(No1 , No2):
    return No1 + No2

def main():

    Ret = Addition(int(sys.argv[1]) , int(sys.argv[2]))

    print("Addition : " , Ret)

if __name__ == "__main__":
    main()