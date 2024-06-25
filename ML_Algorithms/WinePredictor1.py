
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def WinePredictor():

    dataset  = load_wine()

    Features = dataset.data
    Label = dataset.target

    data_train , data_test , target_train , target_test = train_test_split(Features , Label , test_size=0.5)

    obj = KNeighborsClassifier(n_neighbors= 3)

    obj.fit(data_train , target_train)

    Predictions = obj.predict(data_test)

    Accuracy = accuracy_score(target_test , Predictions)

    Accuracy = Accuracy * 100

    print("Accuracy for wine predictor is : " , Accuracy)

def main():

    print("Wine Predictor using KNN")

    WinePredictor()

if __name__ == "__main__":
    main()