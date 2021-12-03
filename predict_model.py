# First section for imports of dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os.path
import train_model
import pickle

# Importing pickle dependency for saving and loading trained models
import pickle
def predict():
    if os.path.isfile('models/kNNCModel.pickle'):
        model=pickle.load( open( "models/kNNCModel.pickle", "rb" ) )
    else:
        train_model.train_data()
        model=pickle.load( open( "models/kNNCModel.pickle", "rb" ) )

    print(model.predict([[25,4.5,142,1,26,10,90]]))
    print(model.predict([[19,3.5,5,1,900,50,84]]))
    print(model.predict([[26,4.8,5,1,350,99,0]]))
    print(model.predict([[17,3.9,50,1,350,199,36]]))
    print(model.predict([[17,2.7,170,1,20,299,0]]))
