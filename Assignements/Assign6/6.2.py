import threading

def evenFactor(No):
    Ans = 0
    for i in range(No , 0 , -1):
        if(i % 2 == 0):
            Ans = Ans + i

    print(Ans)

def oddFactor(No):
    Ans = 0
    for i in range(No , 0 , -1):
        if(i % 2 != 0):
            Ans = Ans + i

    print(Ans)


def main():
    
    No = int(input("Enter the number : "))

    t1 = threading.Thread(target=evenFactor , args=(No , ))
    t2 = threading.Thread(target=oddFactor , args=(No , ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()