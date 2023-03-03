import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt



df = pd.read_csv('/home/raphael/Desktop/Lux/Exploratory-data-analysis-Python/assets/T Salary Survey EU 2019.csv')
# display the top 5 rows
print(df.head(5))

# display the bottom 5 rows
print(df.tail(5))

# number of rows and columns in the data
print(df.shape) 
# The data comprises of 991 observations and 23 characteristics



# display various summary statistics
print(df.describe())
# The mean value is less than the median value(50%) in the number of vacation days column 
# There is a large difference between the 75%tile and the max values of predictors "number 0f vacation days", "number of home office days per month", "yearly brutto salary".
# The above observations suggest that there are extreme values-outliers in the dataset.



# columns and corresponding data types
print(df.info())
# Data has float, integer and object values



# Finding null values in the dataset
print(df.isnull().sum())


# Dropping the null values
df = df.dropna() 
print(df.count())



# Checking for rows with duplicate data
duplicate_rows_df = df[df.duplicated()]
print(duplicate_rows_df.shape)


