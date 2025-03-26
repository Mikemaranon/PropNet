import pandas as pd
import numpy as np

# Cargar el dataset
df = pd.read_csv('/home/mike/Escritorio/codes/projects/PropNet/PropNet-project/2_Data_Processing/correlation_analysis/transformed_data.csv')  # Cambia por el archivo correcto

# Función para detectar y eliminar outliers utilizando el método IQR
def eliminar_outliers(df):
    # Calcular el rango intercuartílico (IQR) para cada columna numérica
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    
    # Definir límites para identificar outliers
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    
    # Eliminar filas que contienen outliers
    df_sin_outliers = df[~((df < limite_inferior) | (df > limite_superior)).any(axis=1)]
    
    return df_sin_outliers

# Llamar a la función para eliminar outliers
df_limpio = eliminar_outliers(df)

# Exportar el dataset limpio a un archivo CSV
df_limpio.to_csv('/home/mike/Escritorio/codes/projects/PropNet/PropNet-project/2_Data_Processing/correlation_analysis/clean_dataset.csv', index=False)
# Calcular el número de outliers eliminados
outliers_eliminados = len(df) - len(df_limpio)
print(f"            Se han eliminado {outliers_eliminados} outliers.")
print('===========================================================================')
print("El dataset limpio se ha exportado correctamente a 'clean_dataset.csv'.")
