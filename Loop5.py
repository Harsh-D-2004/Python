def Display(no):

    if(no <= 0):
        print("Invalid Input")
        return

    i = 0

    while(i < no):
        print("Jay Ganesh..")
        i = i + 1

def main():

    No = int(input("Enter the number : "))

    Display(No)

if __name__ == "__main__":
    main()