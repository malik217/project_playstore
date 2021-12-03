# First section for imports of dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.neighbors import NearestCentroid
import os.path
import clean
import pickle
from graphviz import Source

import plotly.graph_objs as go
import plotly

def train_data():
    if os.path.isfile('data/googleplaystore_cleanednum.csv'):
        data = pd.read_csv('data/googleplaystore_cleanednum.csv', sep=",")
    else:
        clean.cleandata()
        data = pd.read_csv('data/googleplaystore_cleanednum.csv', sep=",")

    Resultlist=[]
    Resultlist2=[]
    #Specifing the Classifiers in variables
    kNN=KNeighborsClassifier(n_neighbors=50)
    SVM=SVC()
    DTC=tree.DecisionTreeClassifier()

    kNNR=NearestCentroid()
    sVR=SVR()
    DTR=tree.DecisionTreeRegressor()

    data2=data.loc[data['Type'] == 1]

    X = data[["Category","Rating","Reviews","Type","Size","Price","Genres"]]
    X=np.nan_to_num(X)
    y = data.Installs

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=1)
    kNN.fit(X_train, y_train)
    Resultlist.append(["K-Nearest-Neigbor-Classfier",str(kNN.score(X_test,y_test))])
    file_to_store = open("models/kNNCModel.pickle", "wb")
    pickle.dump(kNN, file_to_store)

    SVM.fit(X_train, y_train)
    Resultlist.append(["Super-Vector-Machines-Classifier",str(SVM.score(X_test,y_test))])
    file_to_store = open("models/SVMCModel.pickle", "wb")
    pickle.dump(SVM, file_to_store)

    DTC.fit(X_train, y_train)
    Resultlist.append(["DecisionTreeClassifier",str(DTC.score(X_test,y_test))])
    file_to_store = open("models/DTCModel.pickle", "wb")
    pickle.dump(DTC, file_to_store)

    kNNR.fit(X_train, y_train)
    Resultlist.append(["K-Nearest-Neigbor-Regressor",str(kNNR.score(X_test,y_test))])
    file_to_store = open("models/KNNRModel.pickle", "wb")
    pickle.dump(kNNR, file_to_store)

    sVR.fit(X_train, y_train)
    Resultlist.append(["Super-Vector-Machines-Regressor",str(sVR.score(X_test,y_test))])
    file_to_store = open("models/SVRModel.pickle", "wb")
    pickle.dump(sVR, file_to_store)

    DTR.fit(X_train, y_train)
    Resultlist.append(["DecisionTreeRegressor",str(DTR.score(X_test,y_test))])
    file_to_store = open("models/DTRModel.pickle", "wb")
    pickle.dump(DTR, file_to_store)

    i=0
    for item in Resultlist:
        print(Resultlist[i][0]," has an accurancy of ",Resultlist[i][1])
        i=i+1

    X = data2[["Category","Rating","Reviews","Type","Size","Price","Genres"]]
    X=np.nan_to_num(X)
    y = data2.Installs

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=1)
    kNN.fit(X_train, y_train)
    Resultlist2.append(["K-Nearest-Neigbor-Classfier",str(kNN.score(X_test,y_test))])
    file_to_store = open("models/kNNCModelPaid.pickle", "wb")
    pickle.dump(kNN, file_to_store)

    SVM.fit(X_train, y_train)
    Resultlist2.append(["Super-Vector-Machines-Classifier",str(SVM.score(X_test,y_test))])
    file_to_store = open("models/SVMCModelPaid.pickle", "wb")
    pickle.dump(SVM, file_to_store)

    DTC.fit(X_train, y_train)
    Resultlist2.append(["DecisionTreeClassifier",str(DTC.score(X_test,y_test))])
    file_to_store = open("models/DTCModelPaid.pickle", "wb")
    pickle.dump(DTC, file_to_store)

    kNNR.fit(X_train, y_train)
    Resultlist2.append(["K-Nearest-Neigbor-Regressor",str(kNNR.score(X_test,y_test))])
    file_to_store = open("models/KNNRModelPaid.pickle", "wb")
    pickle.dump(kNNR, file_to_store)

    sVR.fit(X_train, y_train)
    Resultlist2.append(["Super-Vector-Machines-Regressor",str(sVR.score(X_test,y_test))])
    file_to_store = open("models/SVRModelPaid.pickle", "wb")
    pickle.dump(sVR, file_to_store)

    DTR.fit(X_train, y_train)
    Resultlist2.append(["DecisionTreeRegressor",str(DTR.score(X_test,y_test))])
    file_to_store = open("models/DTRModelPaid.pickle", "wb")
    pickle.dump(DTR, file_to_store)

    i=0
    for item in Resultlist2:
        print(Resultlist2[i][0]," has an accurancy of ",Resultlist2[i][1], " for Paid Applications")
        i=i+1