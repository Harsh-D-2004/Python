from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def main():

    iris = load_iris()

    Features = iris.data # type: ignore
    Labels = iris.target # type: ignore

    data_train , data_test , target_train , target_test = train_test_split(Features , Labels , test_size=0.5)

    obj = tree.DecisionTreeClassifier()

    obj.fit(data_train , target_train)

    Output = obj.predict(data_test)

    print(Output)

    Accuracy = accuracy_score(target_test , Output)

    Accuracy = Accuracy * 100

    print("Accuracy : " , Accuracy , "%")


if __name__ == "__main__":
    main()