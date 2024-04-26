import sys

def main():
    print("Demonstration on command line arguments")
    print("Name of application : " , sys.argv[0])
    print("Datatype of argv : " , type(sys.argv))
    print("Number of command line arguments : " , len(sys.argv))

if __name__ == "__main__":
    main()