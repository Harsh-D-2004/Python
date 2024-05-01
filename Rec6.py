i = 1
def DisplayR(No):

    global i

    if(i <= No):

        print(i)
        i += 1
        DisplayR(No)

def main():

    No = int(input("Enter the number : "))

    DisplayR(No)

if __name__ == "__main__":
    main()