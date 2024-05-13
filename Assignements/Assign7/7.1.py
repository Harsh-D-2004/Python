class Demo:

    Value = 101

    def __init__(self , A , B):
        self.No1 = A
        self.No2 = B

    def Fun(self):
        print("Value of No1 : " , self.No1)
        print("Value of No2 : " , self.No2)
        print("Value of Value Variable : " , Demo.Value)

    def Gun(self):
        print("Value of No1 : " , self.No1)
        print("Value of No2 : " , self.No2)
        print("Value of Value Variable : " , Demo.Value)

def main():

    obj1 = Demo(11 , 21)
    obj2 = Demo(45 , 67)

    obj1.Fun()
    obj1.Gun()
    obj2.Fun()
    obj2.Gun()

if __name__ == "__main__":
    main()