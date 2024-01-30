# importations
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 

def readCSV(file_path):
    df = pd.read_csv(file_path)
    return df

def decribeData(df):
    print("----------------")
    print("OverView Of Data")
    print("----------------")
    print(df.head())
    print("Data Types")
    print("----------------")
    print(df.dtypes)
    print("DataFrame Shape")
    print("----------------")
    print(df.shape)

def summaryOfData(df):
    print("Statistical Summary of data")
    print(df.describe())

#  Checking for Outliers and Null Values
    
def  checkNullValues(df):
    print("Null Values Present in Data")
    print(df.isna().sum() * 100 / len(df))


# checking for outliers based on box plot and Inter Quartile Range

def checkOutliersIQR(df):
    Q1 = np.percentile(df, 25, method='midpoint')
    Q3 = np.percentile(df, 75, method='midpoint')
    IQR = Q3 - Q1
    print(f"Inter Quartile Range: {IQR}")

    # Calculating Lower & Upper Bounds
    lowerBound = Q1 - 1.5*IQR
    upperBound = Q3 + 1.5*IQR 

    print(f"Lower Bound: {lowerBound}")
    print(f"Upper Bound: {upperBound}")


def checkOutliersBoxplot(df):
    sns.boxplot(df)