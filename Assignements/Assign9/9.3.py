import os
import sys

def main():

    Fname = sys.argv[1];
    Fname2 = sys.argv[2];

    if os.path.exists(Fname):
        print("File already exists")

        fobj = open(Fname , "r")
        print(fobj)

        Str = fobj.read()

        fobj2 = open(Fname2 , "w")

        fobj2.write(Str)

        fobj2.close()

        fobj2 = open(Fname2 , "r")

        Str2 = fobj2.read()

        print(Str2)

        fobj2.close()

    else:
        open(Fname , "x")
        print("File is created")

if __name__ =="__main__":
    main()