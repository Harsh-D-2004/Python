# Types of functional arguments :
#     1 : Positional Arguments
#     2 : KeyWord Arguments
#     3 : Default  Arguments 
#     4 : Variable No of Arguments

def Information(Name , Age , Salary):

    print("Name : " , Name)
    print("Age : " , Age)
    print("Salary : " , Salary)
    print()

Information("Harsh" , 32 , 90000)
Information("Amit" , 23 , 80000)
Information(25 , "Sagar" , 80000)


Information(Age=31 , Salary=45000 , Name="Harish")