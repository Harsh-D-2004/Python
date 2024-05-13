import os;

def Cube(No):
    print("PID is : " , os.getpid())
    return No**3


def main():

    Arr = [10 , 20 , 30 , 40]
    Result = []

    for val in Arr:
        Result.append(Cube(val))

    print(Result)

if __name__ == "__main__":
    main()
