from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_excel(r'D:\Fall 2020\Data Visualisation\Assignment 2\World Bank CO2.xlsx',
                   sheet_name='World Bank CO2 Cleaned')
temp = df.dropna()
temp = temp.loc[df['Country Name'] == 'Libya']
plot1 = temp['CO2 Per Capita (metric tons)']

temp = df.loc[df['Country Name'] == 'Liberia']
plot2 = temp['CO2 Per Capita (metric tons)']


x_data = temp['Year']

print(x_data)

plt.subplot(2,1,1)
plt.plot(x_data,plot1)
plt.title("CO2 per capita for Libia")

plt.subplot(2, 1, 2)
plt.plot(x_data,plot2)
plt.title("CO2 per capita for Liberia")
plt.show()