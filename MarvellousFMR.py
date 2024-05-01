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