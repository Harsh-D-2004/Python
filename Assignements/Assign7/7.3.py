class Arithmetic:

    def __init__(self):
        self.a = 0.0
        self.b = 0.0

    def Accept(self):
        self.a = float(input("Enter the first number : "))
        self.b = float(input("Enter the second number : "))

    def Addition(self):
        print("Addition : " ,  self.a + self.b)
    
    def Subtraction(self):
        print("Subtraction : " ,  self.a - self.b)
    
    def Multiplication(self):
        print("Multiplication : " ,  self.a * self.b)
    
    def Division(self):
        print("Division : " ,  self.a / self.b)
    
def main():

    obj1 = Arithmetic()

    obj1.Accept()
    obj1.Addition()
    obj1.Subtraction()
    obj1.Multiplication()
    obj1.Division()

    obj2 = Arithmetic()

    obj2.Accept()
    obj2.Addition()
    obj2.Subtraction()
    obj2.Multiplication()
    obj2.Division()

if __name__ == "__main__":
    main()