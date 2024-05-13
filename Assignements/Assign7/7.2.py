class Circle:

    Pi = 3.14

    def __init__(self):
        self.radius = 0.0
        self.Circumference = 0.0
        self.Area = 0.0

    def Accept(self):
        print("Enter the radius of the circle")
        self.radius = float(input())

    def Calculate(self):
        self.Circumference = 2 * Circle.Pi * self.radius
        self.Area = Circle.Pi * self.radius * self.radius

    def Display(self):
        print("radius : " , self.radius)
        print("area : " , self.Area)
        print("circumference : " , self.Circumference)

def main():

    c1 = Circle()
    c2 = Circle()

    c1.Accept()
    c1.Calculate()
    c1.Display()

    c2.Accept()
    c2.Calculate()
    c2.Display()

if __name__ == "__main__":
    main()