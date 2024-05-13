import threading

def Odd():
    j = 1
    for i in range(10):
        print(j)
        j = j + 2

def Even():
    j = 2
    for i in range(10):
        print(j)
        j = j + 2

def main():

    t1 = threading.Thread(target=Odd )
    t2 = threading.Thread(target=Even )

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()