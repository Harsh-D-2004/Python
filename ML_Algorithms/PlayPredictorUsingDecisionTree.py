import pandas
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
import sklearn
import sklearn.tree

def PlayPredictor(WeatherInput , TemperatureInput):

    dataset = pandas.read_csv("CSV\\PlayPredictor (2).csv" , usecols = ['Whether','Temperature','Play'])

    Whether = dataset.Whether
    Temperature = dataset.Temperature
    Target = dataset.Play

    le = preprocessing.LabelEncoder()

    Whether_Encoded = le.fit_transform(Whether)
    Temperature_Encoded = le.fit_transform(Temperature)
    Target_Encoded = le.fit_transform(Target)

    Features = list(zip(Whether_Encoded , Temperature_Encoded))

    obj = sklearn.tree.DecisionTreeClassifier()

    obj.fit(Features , Target_Encoded)

    if WeatherInput.lower() == 'sunny':
        WeatherInput = 2
    elif WeatherInput.lower() == 'rainy':
        WeatherInput = 1
    elif WeatherInput.lower() == 'overcast':
        WeatherInput = 0
    else:
        print('Enter proper weather')
        exit()

    if TemperatureInput.lower() == 'hot':
        TemperatureInput = 1
    elif TemperatureInput.lower() == 'mild':
        TemperatureInput = 2
    elif TemperatureInput.lower() == 'cool':
        TemperatureInput = 0
    else:
        print('Enter proper temperature')
        exit()

    Ret = obj.predict([[WeatherInput , TemperatureInput]])

    if Ret == 0:
        print("You cannot play")
    
    else:
        print("You can Play")
    
def main():

    print("Play predictor using decision tree classifier")

    Weather = input("Enter todays weather : (Rainy , Overcast , Sunny) : ")
    Temperature = input("Enter todays temperature : (Hot , Mild , Cool) : ")

    PlayPredictor(Weather , Temperature)

if __name__ == "__main__":
    main()