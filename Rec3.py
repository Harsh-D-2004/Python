def fun():

    iCnt = 1
    print("Inside fun" , iCnt)
    iCnt = iCnt + 1
    fun()

def main():

    fun()


if __name__ == "__main__":
    main()