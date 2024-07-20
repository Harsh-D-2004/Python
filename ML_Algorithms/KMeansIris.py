import pandas as p
import matplotlib.pyplot as mpl
from sklearn.cluster import KMeans

def Predictor():

    dataset = p.read_csv("CSV\\iris.csv")
    # print(dataset.head())

    Features = dataset
    # print(Features.head())

    wcss = []

    for i in range(1 , 11):
        obj = KMeans(n_clusters=i , init='k-means++' , max_iter=300 , n_init=10 , random_state=0)
        obj.fit(Features)
        wcss.append(obj.inertia_)

    mpl.figure(figsize=(5,5))
    mpl.plot(range(1 , 11) , wcss)
    mpl.xlabel("No of clusters")
    mpl.ylabel("Sum of Squared Error")
    mpl.show()

    obj = KMeans(n_clusters=3 , init='k-means++' , max_iter=300 , n_init=10 , random_state=0)
    Predictions = obj.fit_predict(dataset)

    mpl.scatter(Features.iloc[Predictions == 0 , 0] , Features.iloc[Predictions == 0 , 1] , s=100 , c = 'red' , label = 'iris-sentosa')
    mpl.scatter(Features.iloc[Predictions == 1 , 0] , Features.iloc[Predictions == 1 , 1] , s=100 , c = 'blue' , label = 'iris-virginica')
    mpl.scatter(Features.iloc[Predictions == 2 , 0] , Features.iloc[Predictions == 2 , 1] , s=100 , c = 'green' , label = 'iris-versicolor')

    mpl.scatter(obj.cluster_centers_[: , 0] , obj.cluster_centers_[: , 1] , s = 100 , c='yellow' , label = 'center')

    mpl.legend()

    mpl.show()

def main():

    print("K-Means on Iris dataset")

    Predictor()

if __name__ == "__main__":
    main()