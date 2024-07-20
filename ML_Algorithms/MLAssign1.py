import pandas as py

def DataUnderstanding():

    dataset = py.read_csv("CSV\\Advertising (1).csv")

    print(dataset.head())

    print(dataset.count())

    print(dataset.isnull().sum())

    print((dataset == 0).sum())

    slicedSubset = dataset.iloc[1:3 , 0:3]
    print(slicedSubset)

    subset = dataset.loc[0:3]
    print(subset)

    conditionalSubset = dataset[dataset['TV'] > 100]
    print(conditionalSubset)

    conditionalSubset2 = dataset.query('TV > 100 and radio < 40')
    print(conditionalSubset2)

    mean_of_column = dataset['TV'].mean()
    print(mean_of_column)

    mode_of_column = dataset['radio'].mode()
    print(mode_of_column)

    median_of_column = dataset['newspaper'].median
    print(median_of_column)

    print(dataset.describe())


def main():

    print("Assignement 1")

    DataUnderstanding()

if __name__ == "__main__":
    main()