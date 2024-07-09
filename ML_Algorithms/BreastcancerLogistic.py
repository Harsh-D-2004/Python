
import pandas as py
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

def remove_questionmark_fromdataset(data):

    df = py.DataFrame(data)

    return df[~df.apply(lambda row: row.astype(str).str.contains(r'\?').any(), axis=1)]

def BreastCancerPredictor():

    dataset = py.read_csv('CSV\\breast-cancer-wisconsin.csv')

    cleaned_data = remove_questionmark_fromdataset(dataset)

    Label = cleaned_data['CancerType']
    Features = cleaned_data.drop(columns=['CancerType' , 'CodeNumber'])

    Features_train , Features_test , Label_train , Label_test = train_test_split(Features , Label ,  test_size=0.5)

    obj = LogisticRegression()
    obj.fit(Features_train , Label_train)

    Predictions = obj.predict(Features_test)

    Accuracy = accuracy_score(Label_test , Predictions)
    Accuracy = Accuracy * 100
    print("Accuracy : " , Accuracy)

    ClassificationReport = classification_report(Label_test , Predictions)
    print("Classification Report : ")
    print(ClassificationReport)

    Confusion_Matrix = confusion_matrix(Label_test , Predictions)
    print("Confusion Matrix")
    print(Confusion_Matrix)

def main():

    print("Breastcancer Predictor using Logistic Regression")

    BreastCancerPredictor()


if __name__ == "__main__":
    main()