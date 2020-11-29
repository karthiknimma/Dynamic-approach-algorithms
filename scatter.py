# Scatter plot of country Switzerland

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel (r'D:\Fall 2020\Data Visualisation\Assignment 2\World Bank CO2.xlsx', sheet_name='World Bank CO2 Cleaned')
df=df.dropna()
print(df)
# print(df)
temp1 = df.loc[df['Country Name'] == 'Switzerland']
y_data = temp1['CO2 (kt)']
print(y_data)

temp2 = df.loc[df['Country Name'] == 'Switzerland']
x_data = temp2['Year']
print(x_data)
plt.figure()
plt.title("World bank CO2")
plt.scatter(x_data, y_data)
plt.show()

