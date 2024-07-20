
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

def Boosting():

    dataset = load_iris()

    Features = dataset['data']
    Labels = dataset['target']

    Features_train , Features_test , Labels_train , Labels_test = train_test_split(Features , Labels , test_size=0.3)

    obj = DecisionTreeClassifier()
    adc = AdaBoostClassifier(obj)
    adc = AdaBoostClassifier(obj , n_estimators=100 , learning_rate=1)

    adc.fit(Features_train , Labels_train)

    Testing_Accuracy = adc.score(Features_test , Labels_test)
    Training_Accuracy = adc.score(Features_train , Labels_train)

    print("Training accuracy : " , Training_Accuracy * 100)
    print("Testing accuracy : " , Testing_Accuracy * 100)

def main():

    print("Ensemble Machine Learning using Boosting Algorithm")

    Boosting()


if __name__ == '__main__':
    main()