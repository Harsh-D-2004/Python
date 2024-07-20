import pandas as p
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as mpl
import numpy as np

def DiabetesPredictor():

    dataset = p.read_csv("CSV\\diabetes.csv")
    # print(dataset.head())

    newDataset = dataset.drop(columns=['Outcome'])
    # print(newDataset.head())

    Features = newDataset
    Labels = dataset['Outcome']

    Feature_train , Feature_test , Label_train , Label_test = train_test_split(Features , Labels , random_state=66 , test_size=0.4)

    obj = LogisticRegression()

    obj.fit(Feature_train , Label_train)
    Predictions = obj.predict(Feature_test)

    Accuracy = accuracy_score(Label_test , Predictions) * 100
    print("Accuracy score : " , Accuracy)

    print("Training Accuracy : " , obj.score(Feature_train , Label_train))
    print("Testing Accuracy : " , obj.score(Feature_test , Label_test))

    obj = LogisticRegression(C=0.01)

    obj.fit(Feature_train , Label_train)
    Predictions = obj.predict(Feature_test)

    Accuracy = accuracy_score(Label_test , Predictions) * 100
    print("Accuracy score : " , Accuracy)

    print("Training Accuracy : " , obj.score(Feature_train , Label_train))
    print("Testing Accuracy : " , obj.score(Feature_test , Label_test))

    print("Feature names : " , obj.feature_names_in_)

def main():

    print("Diabetes Dataset using Decision Tree Classifier")

    DiabetesPredictor()

if __name__ == "__main__":
    main()