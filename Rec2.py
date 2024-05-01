import sys
import os

def main():

    print("Recursion limit : " , sys.getrecursionlimit())
    sys.setrecursionlimit(1500)
    print("Recursion limit : " , sys.getrecursionlimit())

if __name__ == "__main__":
    main()