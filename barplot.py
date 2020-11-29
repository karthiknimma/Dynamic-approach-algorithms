import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel (r'D:\Fall 2020\Data Visualisation\Assignment 2\World Bank CO2.xlsx', sheet_name='World Bank CO2 Cleaned')
df=df.dropna()
print(df)
temp1 = df.loc[(df['Year'] == 1997) & (df['CO2 (kt)'] <= 1000)]
y_data = temp1['CO2 (kt)']
print(y_data)

temp2 = df.loc[(df['Year'] == 1997) & (df['CO2 (kt)'] <= 1000)]
x_data = temp2['Country Name']
print(x_data)
plt.figure()
plt.title("CO2 Emissions for the year 1997")
plt.bar(x_data, y_data)
plt.xticks(rotation='vertical')
plt.show()

