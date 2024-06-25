
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

def WinePredictor():

    dataset  = load_wine()

    Features = dataset.data
    Label = dataset.target

    data_train , data_test , target_train , target_test = train_test_split(Features , Label , test_size=0.5)

    obj = DecisionTreeClassifier()

    obj.fit(data_train , target_train)

    Predictions = obj.predict(data_test)

    Accuracy = accuracy_score(target_test , Predictions)

    Accuracy = Accuracy * 100

    print("Accuracy for wine predictor is : " , Accuracy)

def main():

    print("Wine Predictor using Decision Tree Classifier")

    WinePredictor()

if __name__ == "__main__":
    main()