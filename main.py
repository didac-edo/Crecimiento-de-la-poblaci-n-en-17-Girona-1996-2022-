import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('2870.csv', sep=';')

data = data[data['Periodo'].notna() & data['Total'].notna()]

data['Total'] = pd.to_numeric(data['Total'], errors='coerce')
data = data[data['Total'].notna()]

data = data.sort_values('Periodo')

plt.figure(figsize=(10, 6))

plt.bar(data['Periodo'].astype(str), data['Total'], color='skyblue')

plt.xlabel('Año')
plt.ylabel('Población')
plt.title('Crecimiento de la población en 17 Girona (1996-2022)')

plt.xticks(rotation=45)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
