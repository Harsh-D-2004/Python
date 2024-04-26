import LoopModule

def Display(no):

    if(no <= 0):
        print("Invalid Input")
        return

    LoopModule.Display(no)

def main():
    
    No = int(input("Enter the number : "))

    Display(No)

if __name__ == "__main__":
    main()