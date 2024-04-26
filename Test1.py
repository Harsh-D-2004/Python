def Display(no):

    if(no <= 0):
        print("Invalid Input")
        return

    for no in range(0 , no):
        print("Jay Ganesh.." , end = " ")

def main():

    No = int(input("Enter the number : "))

    Display(No)

if __name__ == "__main__":
    main()