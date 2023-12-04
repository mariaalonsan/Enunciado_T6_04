import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargamos el archivo csv
df = pd.read_csv('mpg.csv')

# Mostrarmos las primeras 5 filas
print(df.head())

#Creamos un gráfico de dispersión usando Matplotlib, donde el eje x es la potencia y el eje y es el consumo de combustible (mpg). 
plt.figure(figsize=(10, 6))
plt.scatter(df['horsepower'], df['mpg'])

# Etiquetas de los ejes
plt.title('Relación ent5re MPG y Caballos de fuerza')
plt.xlabel('Caballos de fuerza (Potencia)')
plt.ylabel('Consumo de combustible (MPG)')

# Mostrar el gráfico
plt.show()



