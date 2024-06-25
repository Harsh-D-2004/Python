from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def main():
    print("----------------------Iris Flower Classification Case Study---------------------")

    # Load the Iris dataset
    iris = load_iris()

    print(iris)

    # Extract features and labels
    Features = iris.data # type: ignore
    Labels = iris.target # type: ignore

    data_train , data_test , target_train , target_test = train_test_split(Features , Labels , test_size=0.5)


if __name__ == "__main__":
    main()
