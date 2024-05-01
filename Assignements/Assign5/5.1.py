
i = 0

def Display():

    global i

    if(i <= 5):

        print("*" , end = " ")
        i = i + 1
        Display()

def main():

    Display()


if __name__ == "__main__":
    main()