import os

def main():
    print("Enter the name of file that you want to open for deleting purpose : ")
    Fname = input()

    if os.path.exists(Fname):

        os.remove(Fname)

        print("File successfully deleted")

    else:
        print("File is not present")

if __name__ == "__main__":
    main()