
import pandas as p
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as mp

def AdvertisingPredictor():

    dataset = p.read_csv("CSV\\Advertising (1).csv" , usecols=["TV" , "radio" , "newspaper" , "sales"])

    # TV = dataset.TV.values.reshape(-1 , 1)
    # radio = dataset.radio.values.reshape(-1 , 1)
    # newspaper = dataset.newspaper.values.reshape(-1 , 1)

    # Y
    Target = dataset.sales
    # X
    Features = p.DataFrame({'TV': dataset.TV, 'radio': dataset.radio, 'newspaper': dataset.newspaper})

    obj = LinearRegression()
    obj.fit(Features , Target)

    
    Predictions = obj.predict([[44.5,39.3,45.1]])
    print(Predictions)
    
    training_preds = obj.predict(Features)

    Deviation = r2_score(Target, training_preds)
    print("Deviation : " , Deviation)
    print("Intercept:", obj.intercept_)
    
    TV_only = p.DataFrame({'TV': dataset.TV, 'radio': [0]*len(dataset), 'newspaper': [0]*len(dataset)})
    TV_preds = obj.predict(TV_only)

    mp.scatter(dataset.TV , Target , color='#6062f4' , label='Scatter points')
    mp.plot(dataset.TV , TV_preds , color='#d52943' , label = 'Regression line')

    mp.xlabel('X - Independent Variable(TV)')
    mp.ylabel('Y - Dependent Variable(Sales)')
    mp.title("TV vs Sales")

    TV_sales_Deviation = r2_score(Target , TV_preds)
    print("Deviation of TV : " , TV_sales_Deviation)

    mp.legend()
    mp.show()

    newspaper_only = p.DataFrame({'TV': [0]*len(dataset), 'radio': [0]*len(dataset), 'newspaper': dataset.newspaper})
    newspaper_preds = obj.predict(newspaper_only)

    mp.scatter(dataset.newspaper, Target, color='#6062f4', label='Scatter points')
    mp.plot(dataset.newspaper, newspaper_preds, color='#d52943', label='Regression line')

    mp.xlabel('X - Independent Variable(newspaper)')
    mp.ylabel('Y - Dependent Variable(Sales)')
    mp.title("Newspaper vs Sales")

    newspaper_sales_Deviation = r2_score(Target, newspaper_preds)
    print("Deviation of Newspaper : ", newspaper_sales_Deviation)

    mp.legend()
    mp.show()

    radio_only = p.DataFrame({'TV': [0]*len(dataset), 'radio': dataset.radio, 'newspaper': [0]*len(dataset)})
    radio_preds = obj.predict(radio_only)

    mp.scatter(dataset.radio , Target , color='#6062f4' , label='Scatter points')
    mp.plot(dataset.radio , radio_preds , color='#d52943' , label = 'Regression line')

    mp.xlabel('X - Independent Variable(radio)')
    mp.ylabel('Y - Dependent Variable(Sales)')

    radio_sales_Deviation = r2_score(Target , radio_preds)
    print("Deviation of Radio : " , radio_sales_Deviation)
    mp.title("Radio vs Sales")

    mp.legend()
    mp.show()

def main():

    print("Advertising predictor using regression")

    AdvertisingPredictor()

if __name__ == "__main__":
    main()