import os

def main():
    print("Enter the name of file that you want to open for reading purpose : ")
    Fname = input()

    if os.path.exists(Fname):
        fobj = open(Fname , "r")
        print("File successfully opened in write mode")
        print(fobj)

        Str = fobj.read(5)

        print(Str)

    else:
        print("File is not present")

if __name__ == "__main__":
    main()