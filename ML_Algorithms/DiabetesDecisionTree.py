import pandas as p
from sklearn.tree import DecisionTreeClassifier
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

    obj = DecisionTreeClassifier()

    obj.fit(Feature_train , Label_train)
    Predictions = obj.predict(Feature_test)

    Accuracy = accuracy_score(Label_test , Predictions) * 100
    print("Accuracy score : " , Accuracy)

    print("Training Accuracy : " , obj.score(Feature_train , Label_train))
    print("Testing Accuracy : " , obj.score(Feature_test , Label_test))

    obj = DecisionTreeClassifier(max_depth=3 , random_state=0)

    obj.fit(Feature_train , Label_train)
    Predictions = obj.predict(Feature_test)

    Accuracy = accuracy_score(Label_test , Predictions) * 100
    print("Accuracy score : " , Accuracy)

    print("Training Accuracy : " , obj.score(Feature_train , Label_train))
    print("Testing Accuracy : " , obj.score(Feature_test , Label_test))

    print("Feature Importance : " , obj.tree_.compute_feature_importances())

    print("Feature names : " , obj.feature_names_in_)

    Diabetes_Feature_Importance_plot(obj)

def Diabetes_Feature_Importance_plot(Model):

    mpl.figure(figsize=(8,6))
    mpl.barh(range(8) , Model.tree_.compute_feature_importances() , align="center")
    mpl.yticks(np.arange(8) , Model.feature_names_in_)
    mpl.xlabel("Importance")
    mpl.ylabel("Feature name")
    mpl.title("Feature Importance")
    mpl.ylim(-1 , 8)
    mpl.show()

def main():

    print("Diabetes Dataset using Decision Tree Classifier")

    DiabetesPredictor()

if __name__ == "__main__":
    main()