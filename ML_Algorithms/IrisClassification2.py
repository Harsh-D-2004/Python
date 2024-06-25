from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def main():
    print("----------------------Iris Flower Classification Case Study---------------------")

    # Load the Iris dataset
    iris = load_iris()

    # print(iris)

    # Extract features and labels
    Features = iris.data # type: ignore
    Labels = iris.target # type: ignore

    data_train, data_test, target_train, target_test = train_test_split(Features, Labels, test_size=0.5)

    obj = tree.DecisionTreeClassifier()

    obj.fit(data_train, target_train)

    output = obj.predict(data_test)

    print(output)

    Accuracy = accuracy_score(target_test, output)

    print("Accuracy : ", Accuracy * 100, "%")

if __name__ == "__main__":
    main()
