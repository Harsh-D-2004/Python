import os

def main():
    print("Enter the name of file that you want to open : ")
    Fname = input()

    if os.path.exists(Fname):
        fobj = open(Fname , "r")
        print("File successfully opened")
        print(fobj)

    else:
        print("File is not present")

if __name__ == "__main__":
    main()