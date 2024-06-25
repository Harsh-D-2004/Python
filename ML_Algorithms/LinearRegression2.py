import numpy as np
import matplotlib.pyplot as plt


def LinearRegression():

    X = np.array([1 , 2 , 3 , 4 , 5])
    Y = np.array([3 , 4 , 2 , 4 , 5])

    X_mean = np.mean(X)
    Y_mean = np.mean(Y)

    m = 0
    numerator = 0
    denominator = 0

    for i in range(len(X)):

        numerator += ((X[i] - X_mean) * (Y[i] - Y_mean))
        denominator += ((X[i] - X_mean)**2)

    m = numerator/denominator

    print("Slope : " , m)

    C = 0
    C = Y_mean - (m * X_mean)

    print("Y intercept : " , C)

    x = np.linspace(1 , 6 , len(X))

    y = m * x + C
    y_pred = m * X + C

    plt.scatter(X , Y , color='#ca0c47' , label='scatter-plot')  
    plt.plot(x , y , color='#d0f625' , label='Regression-Line')
    plt.scatter(X , y_pred , color='#5636f5' , label='Ypred-plot')

    plt.xlabel('X - Independent Variable')
    plt.ylabel('Y - Dependent Variable')

    plt.legend()
    plt.show()

    numerator = 0
    denominator = 0
    Y_pred = 0

    for i in range(len(X)):

        Y_pred = m * X[i] + C
        numerator += (Y[i] - Y_pred)**2
        denominator += (Y[i] - Y_mean)**2

    r = 1 - (numerator/denominator)
    print("Goodness of fitness : " , r)

def main():

    print("Linear Regression : ")

    LinearRegression()

if __name__ == "__main__":
    main()