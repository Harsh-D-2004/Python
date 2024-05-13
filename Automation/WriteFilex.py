import os

def main():
    print("Enter the name of file that you want to open for writing purpose : ")
    Fname = input()

    if os.path.exists(Fname):
        fobj = open(Fname , "a")
        print("File successfully opened in write mode")
        print(fobj)

        print("Enter data that u want to write in file")
        Data = input()

        fobj.write(Data)

    else:
        print("File is not present")

if __name__ == "__main__":
    main()