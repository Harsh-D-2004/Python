import threading

def EvenDisplay(No):
    x = 2
    for i in range(No):
        print("Even : " , x)
        x = x + 2

def OddDisplay(No):
    x = 1
    for i in range(No):
        print("Odd : " , x)
        x = x + 2

def main():

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