import threading

def small(str):
    iCnt = 0
    for i in str:
        if i >= 'a' and i <= 'z':
            iCnt = iCnt + 1

    print(iCnt)
    print("ID : " , threading.get_ident())

def capital(str):
    iCnt = 0
    for i in str:
        if i >= 'A' and i <= 'Z':
            iCnt = iCnt + 1

    print(iCnt)
    print("ID : " , threading.get_ident())

def digits(str):
    iCnt = 0
    for i in str:
        if i >= '0' and i <= '9':
            iCnt = iCnt + 1

    print(iCnt)
    print("ID : " , threading.get_ident())

def main():

    str = input("Input String : ")

    t1 = threading.Thread(target=small , args=(str , ))
    t2 = threading.Thread(target=capital , args=(str , ))
    t3 = threading.Thread(target=digits , args=(str , ))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == '__main__':
    main()