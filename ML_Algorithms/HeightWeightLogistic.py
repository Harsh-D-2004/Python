
import pandas as p
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier

def MyPredictor():
    dataset = p.read_csv("CSV\\weight-height.csv")

    Labels = dataset['Gender']

    le = LabelEncoder()
    encoded_labels = le.fit_transform(dataset['Gender'])
    Features = dataset[['Height' , 'Weight']]

    obj = LogisticRegression(C=0.1, random_state=42)
    # obj = DecisionTreeClassifier()
    
    Feature_train , Feature_test , Label_train , Label_test = train_test_split(Features , encoded_labels , test_size=0.5)

    obj.fit(Feature_train , Label_train)

    Predicted = obj.predict(Feature_test)

    Accuracy = accuracy_score(Label_test , Predicted)
    Accuracy = Accuracy * 100
    print("Accuracy of Model : " , Accuracy)

    print("Confusion Matrix : " , confusion_matrix(Label_test , Predicted))
    print("Classification report : ")
    print(classification_report(Label_test , Predicted))

def main():

    print("Height Weight Gender Predictor")

    MyPredictor()

if __name__ == "__main__":
    main()