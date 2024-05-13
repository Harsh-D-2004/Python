import os
import time

def Fun(No):
    Sum = 0
    print("PID is : " , os.getpid())
    for i in range(No):
        Sum = Sum + (No**3)
    return Sum

def main():

    startTime = time.time()

    Arr = [100000 , 200000 , 300000 , 400000 , 500000 , 600000 , 700000 , 80000000]
    Result = []

    for val in Arr:
        Result.append(Fun(val))

    endTime = time.time()

    print("Time : " , (endTime - startTime))

    print(Result)

if __name__ == "__main__":
    main()