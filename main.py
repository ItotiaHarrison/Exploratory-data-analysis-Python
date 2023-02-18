# import pandas as pd
import numpy as np

import csv
import matplotlib as plt
from matplotlib import rcParams
import seaborn as sns

plt.style.use("ggplot")
rcParams['figure.figsize'] = (12,6)

# df = pd.read_csv(r'F:/Python assignment/assets/Survey2020.csv')
# print(df)

with open("F:\Python assignment\assets\Survey2020.csv") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)