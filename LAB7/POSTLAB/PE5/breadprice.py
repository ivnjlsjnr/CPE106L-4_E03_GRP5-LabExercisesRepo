import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/juliu/CPE106L-4_E03_GRP5-LabExercisesRepo/LAB7/POSTLAB/breadprice.csv')

df = df.dropna(subset=['Year'])
df['Price'] = df.iloc[:, 1:].mean(axis=1, skipna=True)
df['Year'] = df['Year'].astype(int)
df = df.sort_values('Year')

plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['Price'], marker='o')
plt.title('Average Price of Bread by Year')
plt.xlabel('Year')
plt.ylabel('Average Price (USD)')
plt.grid(True)
plt.tight_layout()
plt.show()
