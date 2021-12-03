# First section for imports of dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os.path
import plotly.graph_objs as go
import plotly
import clean
#Data deklaration

if os.path.isfile('data/googleplaystore_cleaned.csv'):
    data = pd.read_csv('data/googleplaystore_cleaned.csv', sep=",")
else:
    clean.cleandata()
    data = pd.read_csv('data/googleplaystore_cleaned.csv', sep=",")



#Read csv-file
#data = pd.read_csv('data/googleplaystore.csv', sep=",")

#Describe data
print(data.describe(include='all'))
print(data.info())

#Data figures for the Essay
"""
#plt.figure(figsize=(40,10))
#data['Category'].value_counts().plot(kind='pie')
#plt.show()
#plt.figure(figsize=(40,10))
#data['Category'].value_counts().plot(kind='bar')
#plt.xlabel('Category')
#plt.ylabel('freq.')
#plt.grid()
#plt.show()
#print(data.loc[data['Category']=="FAMILY"])
"""

#Data Korrelation after cleaning
"""
data_df1=data_clean.loc[data_clean['Type'] == 'Free']

Rating = data_df1['Rating']
Size = data_df1['Size']
Installs = data_df1['Installs']
Reviews = data_df1['Reviews']
Type = data_df1['Type']
Price = data_df1['Price']

plotgraph = sns.pairplot(pd.DataFrame(list(zip(Rating, np.log(Reviews), Size, np.log(Installs), Price, Type)), 
                        columns=['Rating', 'Reviews', 'Size', 'Installs', 'Price', 'Type']), hue='Type', palette="pastel")

plotgraph.savefig('diagrams/TypeFree.png')

data_df2=data_clean.loc[data_clean['Type'] == 'Paid']

Rating = data_df2['Rating']
Size = data_df2['Size']
Installs = data_df2['Installs']
Reviews = data_df2['Reviews']
Type = data_df2['Type']
Price = data_df2['Price']

plotgraph = sns.pairplot(pd.DataFrame(list(zip(Rating, np.log(Reviews), Size, np.log(Installs), Price, Type)), 
                        columns=['Rating', 'Reviews', 'Size', 'Installs', 'Price', 'Type']), hue='Type', palette="pastel")

plotgraph.savefig('diagrams/TypePaid.png')
"""



