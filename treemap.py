import pandas as pd
import matplotlib.pyplot as plt
import squarify
import numpy as np

df = pd.read_excel(r'D:\Fall 2020\Data Visualisation\Assignment 2\World Bank CO2.xlsx',
                   sheet_name='World Bank CO2 Cleaned')
df = df.dropna()
print(df)
# print(df)
temp1 = df.loc[(df['Year'] == 1997) & (df['CO2 (kt)'] <= 1000) & (df['Country Name'].str.len() <= 7)]
sizes = temp1['CO2 (kt)']
# print(sizes)

temp2 = df.loc[(df['Year'] == 1997) & (df['CO2 (kt)'] <= 1000) & (df['Country Name'].str.len() <= 7)]
label = temp2['Country Name']
# print(label)

color = np.random.uniform(0,1,(len(sizes),3))
color.shape
squarify.plot(sizes=sizes, label=label,value =sizes, color=color, alpha=0.6 )
plt.axis('off')
plt.title("1997 CO2 emissions(in metric tons)")
plt.show()