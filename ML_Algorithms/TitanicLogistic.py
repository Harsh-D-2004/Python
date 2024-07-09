import pandas as p
import matplotlib.pyplot as mpl
import seaborn as s
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

def TitanicLogistic():

    dataset = p.read_csv("CSV\\MarvellousTitanicDataset.csv")

    print(dataset.head(5))
    print(len(dataset))

    print("Survuved and NonSurvived")
    mpl.figure()
    target = "Survived"
    s.countplot(data=dataset , x=target).set_title("Survived and NonSurvived")
    mpl.show()

    print("Survived and NonSurvived based on Sex")
    mpl.figure()
    target = "Survived"
    plot = s.countplot(data=dataset , x = target , hue="Sex")
    mpl.legend(title='Gender', labels=['Female', 'Male'])
    plot.set_xticklabels(['Did Not Survive', 'Survived'])
    mpl.title('Survival by Gender')
    mpl.show()

    print("Survived and NonSurvived based on Passenger Class")
    mpl.figure()
    target = "Survived"
    plot = s.countplot(data=dataset , x = target , hue="Pclass")
    plot.set_xticklabels(['Did Not Survive', 'Survived'])
    mpl.title('Survival by PClass')
    mpl.show()

    print("Survived and NonSurvived based on Age")
    mpl.figure()
    plot = dataset['Age'].plot.hist()
    mpl.title('Survival by Age')
    mpl.show()

    print("Survived and NonSurvived based on Fare")
    mpl.figure()
    plot = dataset['Fare'].plot.hist()
    mpl.title('Survival by Fare')
    mpl.show()

    dataset.drop('zero' , axis=1 , inplace=True)
    print(dataset.head(5))

    # print("Sex Dummies : ")
    # Sex = p.get_dummies(dataset['Sex'] , drop_first=True)
    # print(Sex.head(5))

    # print("PClass Dummies : ")
    # Pclass = p.get_dummies(dataset['Pclass'] , drop_first=True)
    # print(Pclass.head(5))

    # dataset = p.concat([dataset , Sex , Pclass] , axis=1)
    # print(dataset.head(5))

    dataset.drop(['Sex' , 'Embarked' , 'sibsp' , 'Parch'] , axis=1 , inplace=True)
    print(dataset.head(5))

    Features = dataset.drop(['Survived'] , axis=1)
    Label = dataset['Survived']

    Features_train , Features_test , Label_train , Label_test = train_test_split(Features , Label , test_size=0.5)

    obj = LogisticRegression()

    obj.fit(Features_train , Label_train)

    Ret = obj.predict(Features_test)

    Accuracy = accuracy_score(Label_test , Ret)
    Accuracy = Accuracy * 100
    print("Accuracy : " , Accuracy)

    print("Classification report : " , classification_report(Label_test , Ret))
    print("Classification report : " , confusion_matrix(Label_test , Ret))

def main():

    print("Titanic Survived Non survived")

    TitanicLogistic()

if __name__ == "__main__":
    main()