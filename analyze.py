# First section for imports of dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read csv-file
data = pd.read_csv('data/googleplaystore.csv', sep=",")

print(data.describe(include='all'))
