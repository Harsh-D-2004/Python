class Bank:

    Roi = 5

    def __init__(self , Amount , Name):

        self.Amount = Amount
        self.Name = Name

    def Withraw(self , Amt):

        self.Amount = self.Amount - Amt
    
    def Deposit(self , Amt):

       self.Amount  = self.Amount + Amt

    def Interest(self , Amt):

        CalInt = self.Amount * Bank.Roi

        print("Intersest : " , CalInt)

    def Display(self):

        print("Name : " , self.Name)
        print("Amount : " , self.Amount)

def main():

    obj1 = Bank(20000 , "Harsh")

    obj1.Withraw(10000)
    obj1.Deposit(50000)
    obj1.Interest(20000)
    obj1.Display()

if __name__ == "__main__":
    main()
