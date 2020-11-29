import pandas as pd
import matplotlib.pyplot  as plt
from pandas.plotting import parallel_coordinates


df = pd.read_excel(r'D:\Fall 2020\Data Visualisation\Assignment 2\World Bank CO2.xlsx',
                   sheet_name='World Bank CO2 Cleaned')
df = df.dropna()
temp1 = df.loc[df['Year'] == 1997]
# temp1 = temp1.drop('Country Code',axis = 1)
temp1 = temp1[1:12]
parallel_coordinates(temp1[['Country Name','CO2 (kt)', 'CO2 Per Capita (metric tons)']],"Country Name")
plt.title("Parallel coordinates of CO2 data")
plt.show()
