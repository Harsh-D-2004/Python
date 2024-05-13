import multiprocessing
import multiprocessing.process
import os

def EvenDisplay(No):
    x = 2
    print("PID of even process : " , os.getpid())
    print("List of Even Numbers : ")
    for i in range(No):
        print(x)
        x = x + 2
        

def OddDisplay(No):
    x = 1
    print("PID of odd process : " , os.getpid())
    print("List of Odd Numbers : ")
    for i in range(No):
        print(x)
        x = x + 2

def main():

    print("PID of main process : " , os.getpid())

    No = int(input("Enter number : "))

    p1 = multiprocessing.Process(target=EvenDisplay , args= (No , ))
    p2 = multiprocessing.Process(target=OddDisplay , args= (No , ))


    p1.start()
    p1.join()

    p2.start()
    p2.join()

    print("End of main process")

if __name__ == "__main__":
    main()