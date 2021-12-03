import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os.path
import plotly.graph_objs as go
import plotly
import csv

def cleandata():
    #Read csv-file
    data = pd.read_csv('data/googleplaystore.csv', sep=",")

    #Dropping duplikates in data
    data_clean = data.drop_duplicates(subset=['App'])

    #Drop row with error
    data_clean = data_clean[data_clean.Reviews != "3.0M"]

    #Data cleaning for further calculations
    data_clean['Reviews'] = data_clean['Reviews'].apply(lambda x: int(x))
    data_clean['Installs'] = data_clean['Installs'].apply(lambda x: x.replace('+', '') if '+' in str(x) else x)
    data_clean['Installs'] = data_clean['Installs'].apply(lambda x: x.replace(',', '') if ',' in str(x) else x)
    data_clean['Installs'] = data_clean['Installs'].apply(lambda x: int(x))
    data_clean['Price'] = data_clean['Price'].apply(lambda x: str(x).replace('$', '') if '$' in str(x) else str(x))
    data_clean['Price'] = data_clean['Price'].apply(lambda x: float(x))
    data_clean['Size'] = data_clean['Size'].apply(lambda x: str(x).replace('Varies with device', 'NaN') if 'Varies with device' in str(x) else x)
    data_clean['Size'] = data_clean['Size'].apply(lambda x: str(x).replace('M', '') if 'M' in str(x) else x)
    data_clean['Size'] = data_clean['Size'].apply(lambda x: str(x).replace(',', '') if ',' in str(x) else x)
    data_clean['Size'] = data_clean['Size'].apply(lambda x: float(str(x).replace('k', '')) / 1000 if 'k' in str(x) else x)
    data_clean['Size'] = data_clean['Size'].apply(lambda x: float(x))
    data_clean['Size'] = data_clean['Size'].apply(lambda x: x.replace('NaN', '0') if 'NaN' in str(x) else x)

    #Save cleaned CSV file
    data_clean.to_csv('data/googleplaystore_cleaned.csv',index=False)

    tmp=data_clean['Category'].unique()
    list = []
    i=0
    for item in tmp:
        list.append([i, item])
        i=i+1
    i=0
    for item in list:
        data_clean['Category'] = data_clean['Category'].apply(lambda x: str(x).replace(list[i][1], str(list[i][0])) if list[i][1] in str(x) else str(x))
        i=i+1
    data_clean['Category'] = data_clean['Category'].apply(lambda x: int(x))
    with open("data/CatDic.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(list)

    tmp=data_clean['Type'].unique()
    list = []
    i=0
    for item in tmp:
        list.append([i, item])
        i=i+1
    i=0
    for item in list:
        data_clean['Type'] = data_clean['Type'].apply(lambda x: str(x).replace(str(list[i][1]), str(list[i][0])) if str(list[i][1]) in str(x) else str(x))
        i=i+1
    data_clean['Type'] = data_clean['Type'].apply(lambda x: int(x))
    with open("data/TypDic.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(list)

    tmp=data_clean['Genres'].unique()
    list = []
    i=0
    for item in tmp:
        list.append([i, item])
        i=i+1
    i=0
    for item in list:
        data_clean['Genres'] = data_clean['Genres'].apply(lambda x: str(x).replace(str(list[i][1]), str(list[i][0])) if str(list[i][1]) == str(x) else str(x))
        i=i+1
    data_clean['Genres'] = data_clean['Genres'].apply(lambda x: int(x))
    with open("data/GenDic.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(list)

    tmp=data_clean['Content Rating'].unique()
    list = []
    i=0
    for item in tmp:
        list.append([i, item])
        i=i+1
    i=0
    for item in list:
        data_clean['Content Rating'] = data_clean['Content Rating'].apply(lambda x: str(x).replace(str(list[i][1]), str(list[i][0])) if str(list[i][1]) == str(x) else str(x))
        i=i+1
    data_clean['Content Rating'] = data_clean['Content Rating'].apply(lambda x: int(x))
    with open("data/CRDic.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(list)
    
    def impute_median(series):
        return series.fillna(series.median())
    data_clean["Rating"]= data_clean["Rating"].transform(impute_median)
    data_clean["Size"]= data_clean["Size"].transform(impute_median)


    threshold= len(data_clean)*0.1
    data_clean.dropna(thresh=threshold,axis=1,inplace=True)



