import os

def main():
    print("Enter the name of file that you want to create : ")
    Fname = input()

    if os.path.exists(Fname):
        print("Unable to create file as file already exists")

    else:
        open(Fname , "x")
        print("File is successfully created")

if __name__ == "__main__":
    main()