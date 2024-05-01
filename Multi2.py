import os
import multiprocessing

def Task1(No):
    print("Executing First Task")
    print("PID of task1 : " , os.getpid())
    print("PPID of task1 : " , os.getppid())

def Task2(No):
    print("Executing Second Task")
    print("PID of task1 : " , os.getpid())
    print("PPID of task1 : " , os.getppid())

def main():

    print("PID of running process is : " , os.getpid())
    print("PID of parent process ie command prompt : " , os.getppid())

    Value = 11

    p1 = multiprocessing.Process(target = Task1 , args = (Value,))
    p2 = multiprocessing.Process(target = Task2 , args = (Value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()