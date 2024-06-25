from sklearn import tree


# Rough 1
# Smooth 0

# Tennis 1
# Cricket 2

def MarvellousClassifier():

    # Feature Encoding
    Features = [[35, 1], [47, 1], [90, 0], [48, 1], [90, 0], [35, 1], [92, 0],
                [35, 1], [35, 1], [35, 1]]

    # Label Encoding
    Labels = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1]

    # Decide the Algorithm
    obj = tree.DecisionTreeClassifier()

    # Train the Algorithm
    obj.fit(Features, Labels)

    # Test the model
    Ret = obj.predict([[96, 0]])

    if Ret == 1:
        print("Your object looks like Tennis Ball")
    
    elif Ret == 2:
        print("Your object looks like Cricket Ball")

def main():
    print("----------------Ball Type Classification Case Study---------------------------")

    MarvellousClassifier()


if __name__ == "__main__":
    main()
