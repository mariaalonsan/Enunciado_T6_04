import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargamos el archivo csv
df = pd.read_csv('mpg.csv')

# Agrupamos los datos por "model_year" y calculamos la media de mpg para cada año
avg_mpg_by_model_year = df.groupby('model_year')['mpg'].mean()

# Creamos un gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(avg_mpg_by_model_year.index, avg_mpg_by_model_year, color='red', edgecolor='black')

# Añadimos etiquetas de los ejes y título
plt.title('Consumo / Rendimiento medio por año')
plt.xlabel('Año')
plt.ylabel('Consumo medio (mpg)')

# Mostramos el gráfico
plt.show()