import os
import sys

def main():

    F1 = sys.argv[1]
    F2 = sys.argv[2]

    fobj1 = open(F1 , "w")
    fobj2 = open(F2 , "w")

    Str = input("Enter the content for file1 : ")

    fobj1.write(Str)

    Str2 = input("Enter the content for file2 : ")

    fobj2.write(Str2)

    fobj1.close()
    fobj2.close()

    fobj1 = open(F1 , "r")
    fobj2 = open(F2 , "r")

    Str = fobj1.read()
    Str2 = fobj2.read()

    if Str == Str2:
    
        print("Success")
    
    else:
        
        print("Fail")

if __name__ == "__main__":
    main()