import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os.path
import plotly.graph_objs as go
import plotly


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

    #Save cleaned CSV file
    data_clean.to_csv('data/googleplaystore_cleaned.csv',index=False)

