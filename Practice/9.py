import sklearn
from sklearn import tree


# Rough 1
# Smooth 0

# Tennis 1
# Cricket 2

def Classifier(weight , surface):

    Features = [[35, 1], [47, 1], [90, 0], [48, 1], [90, 0], [35, 1], [92, 0],
                [35, 1], [35, 1], [35, 1]]
    
    Labels = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1]

    obj = tree.DecisionTreeClassifier()

    obj.fit(Features , Labels)

    if surface.lower() == "rough":
        surface = 1
    elif surface.lower() == "smooth":
        surface = 0

    Ret = obj.predict([[weight , surface]])

    if Ret == 1:
        Ret = "Tennis"
    else:
        Ret = "Cricket"

    print(Ret)

def main():

    weight = int(input("Enter the weight : "))
    surface = input("Enter the surface : ")

    Classifier(weight , surface)


if __name__ == "__main__":
    main()