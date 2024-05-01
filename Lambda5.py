# Name = lambda Parameters : Logic
# Name(___ , _____ , _____ ..........)

Even = lambda A : (A % 2 == 0)

def main():

    Ret = Even(11)

    if(Ret == Even):
        print("Even")
    else:
        print("Odd")

if __name__ == "__main__":
    main()