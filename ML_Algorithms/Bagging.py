
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier , VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def bagging():

    dataset = load_iris()

    Features = dataset['data']
    Labels = dataset['target']

    obj1 = RandomForestClassifier()
    obj2 = DecisionTreeClassifier()
    obj3 = LogisticRegression()

    Features_train , Features_test , Labels_train , Labels_test = train_test_split(Features , Labels , test_size=0.3)

    voting = VotingClassifier(estimators=[('rnd' , obj1) , ('dtc' , obj2) , ('lr' , obj3)] , voting='hard')

    voting.fit(Features_train , Labels_train)

    predictions = voting.predict(Features_test)

    print(predictions)

    Accuracy = accuracy_score(Labels_test , predictions)

    Accuracy = Accuracy * 100

    print("Testing Accuracy : " , Accuracy)

def main():

    print("Ensemble Machine Learning Bagging technique")

    bagging()

if __name__ == "__main__":
    main()