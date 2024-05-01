
i = 1

def Display():

    global i

    if(i <= 5):

        print(i , end = " ")
        i = i + 1
        Display()

def main():

    Display()


if __name__ == "__main__":
    main()