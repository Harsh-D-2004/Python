
import pandas as p
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as mpl
from sklearn.metrics import r2_score

def HeadBrainPredictor():

    dataset = p.read_csv("CSV\\MarvellousHeadBrain.csv")

    HeadSize = dataset["Head Size(cm^3)"].values.reshape(-1 , 1)
    BrainWeight = dataset["Brain Weight(grams)"]

    obj = LinearRegression()
    obj.fit(HeadSize , BrainWeight)

    Predicted = obj.predict([[3640]])
    print(Predicted)

    Predicted_values = obj.predict(HeadSize)
    
    Deviation = r2_score(BrainWeight , Predicted_values)
    print("Deviation : " , Deviation)

    mpl.plot(HeadSize , Predicted_values , color = '#d51a24' , label='Regression-line')
    mpl.scatter(HeadSize , BrainWeight , color='#5e33ce' , label='Scatter-Points')

    mpl.xlabel("Independant variable (HeadSize)")
    mpl.ylabel("Dependent variable(BrainWeight)")
    mpl.title("HeadSize vs BrainWeight")

    mpl.legend()
    mpl.show()

def main():

    print("Head Brain Cae study using Regression")

    HeadBrainPredictor()

if __name__ == "__main__":
    main()