import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargamos el archivo csv
df = pd.read_csv('mpg.csv')

# Generamos un histograma para la variable "cyliners"
plt.figure(figsize=(8, 6))
plt.hist(df['cylinders'], bins=range(1, df['cylinders'].max()+1), align='left', color='blue', edgecolor='black')

# Añadimos etiquetas de los ejes y título
plt.title('Distribución de cilindros')  
plt.xlabel('Cilindros')
plt.ylabel('Frecuencia')

# Mostramos el gráfico
plt.show()