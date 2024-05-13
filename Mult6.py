import os
import threading

def EvenDisplay(No):
    x = 2
    print("PID of even process : " , os.getpid())
    print("TID of even thread : " , threading.get_ident())
    print("List of Even Numbers : ")
    for i in range(No):
        print(x)
        x = x + 2

def OddDisplay(No):
    x = 1
    print("PID of odd process : " , os.getpid())
    print("TID of odd thread : " , threading.get_ident())
    print("List of Odd Numbers : ")
    for i in range(No):
        print(x)
        x = x + 2

def main():

    print("PID of main process : " , os.getpid())
    print("TID of main thread : " , threading.get_ident())

    No = int(input("Enter number : "))

    p1 = threading.Thread(target=EvenDisplay , args= (No , ))
    p2 = threading.Thread(target=OddDisplay , args= (No , ))


    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main process")

if __name__ == "__main__":
    main()