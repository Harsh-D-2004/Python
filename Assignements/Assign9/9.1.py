import os

def main():

    Fname = input("Enter the name of file u want to open : ")

    if os.path.exists(Fname):
        print("File already exists")

    else:
        open(Fname , "x")
        print("File is created")

if __name__ =="__main__":
    main()