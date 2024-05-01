# Name = lambda Parameters : Logic
# Name(___ , _____ , _____ ..........)

def Addition(A , B):
    return A+B

Add = lambda A , B : A + B

Cube = lambda A : A * A * A

def main():

    Ret = Add(10 , 11)
    print("Addition is : " , Ret)

    Ret = Cube(6)
    print("Cube is : " , Ret)

if __name__ == "__main__":
    main()