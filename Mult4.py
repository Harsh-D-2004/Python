import multiprocessing
import multiprocessing.process

def EvenDisplay(No):
    x = 2
    print("List of Even Numbers : ")
    for i in range(No):
        print(x)
        x = x + 2
        

def OddDisplay(No):
    x = 1
    print("List of Odd Numbers : ")
    for i in range(No):
        print(x)
        x = x + 2

def main():

    No = 10

    p1 = multiprocessing.Process(target=EvenDisplay , args= (No , ))
    p2 = multiprocessing.Process(target=OddDisplay , args= (No , ))


    p1.start()
    p1.join()

    p2.start()
    p2.join()

    print("End of main process")

if __name__ == "__main__":
    main()