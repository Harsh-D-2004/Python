import os

def main():
    print("Enter the name of file that you want to open for reading purpose : ")
    Fname = input()

    if os.path.exists(Fname):
        fobj = open(Fname , "r")
        print("File successfully opened in write mode")
        print(fobj)

        str1 = fobj.readline()
        str2 = fobj.readline()
        str3 = fobj.readline()
        str4 = fobj.readline()

        print(str1)
        print(str2)
        print(str3)
        print(str4)

    else:
        print("File is not present")

if __name__ == "__main__":
    main()