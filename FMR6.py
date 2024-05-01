from functools import reduce

ChkEvenX = lambda No : (No % 2 == 0)
IncreaseX = lambda No : (No + 1)
AddX = lambda A , B : A + B

def filterX(Task , Elements):
    Result = []
    for no in Elements:
        if(Task(no) == True):
            Result.append(no)

    return Result

def mapX(Task , Elements):
    Ans = []
    for no in Elements:
        Ans.append(Task(no))

    return Ans

def reduceX(Task , Elements):
    Ans = 0
    for no in Elements:
        Ans = Task(Ans , no)
    return Ans

def main():

    Data = [11 , 14 , 20 , 23 , 18 , 16 , 15 , 20]

    print("Data from input list : " , Data)

    FData = list(filterX(ChkEvenX , Data))

    print("Data after filter activity : " , FData)

    MData = list(mapX(IncreaseX , FData))

    print("Data after map activity : " , MData)

    Sum = reduceX(AddX , MData)

    print("Sum of elements : " , Sum)

if __name__ == "__main__":
    main()