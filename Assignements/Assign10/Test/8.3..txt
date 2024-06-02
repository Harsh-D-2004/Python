class Numbers:

    def __init__ (self , No):
        self.No = No

    def ChkPerfect(self):

        Ans = 0

        for i in range(1 , self.No):

            if(self.No % i == 0):
                Ans = Ans + i

        if Ans == self.No:
            print("perfect")

        else:
            print("Not perfect")

    def ChkPrime(self):

        bval = True

        for i in range (2 , self.No):

            if(self.No % i == 0):
                bval = False
                break;

        if(bval == False):

            print("Not Prime")

        else:

            print("Prime")

    def Factors(self):

        print("Factors : ")

        for i in range(self.No , 0 , -1):
            print(i , end=" ")

        print()

    def SumFactors(self):

        print("Factors : ")
        Ans = 0
        for i in range(self.No , 0 , -1):
            Ans = Ans + i

        print(Ans)

def main():

    obj = Numbers(6)

    obj.ChkPerfect()
    obj.ChkPrime()
    obj.Factors()
    obj.SumFactors()

if __name__ == "__main__":
    main()
