import threading

def oddList(Arr):
    Ans = 0
    for i in Arr:
        if(i % 2 != 0):
            Ans = Ans + i

    print(Ans)

def evenList(Arr):
    Ans = 0
    for i in Arr:
        if(i % 2 == 0):
            Ans = Ans + i

    print(Ans)

def main():

    Arr = [10 , 21 , 30 , 41 , 50]

    t1 = threading.Thread(target = oddList , args = (Arr , ))
    t2 = threading.Thread(target = evenList , args = (Arr , ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main")

if __name__ == "__main__":
    main()