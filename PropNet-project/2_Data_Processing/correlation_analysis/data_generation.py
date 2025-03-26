import pandas as pd
import numpy as np

# Leer el archivo original
file_path = '/home/mike/Escritorio/codes/projects/PropNet/PropNet-project/2_Data_Processing/correlation_analysis/transformed_data.csv'
df_original = pd.read_csv(file_path)

# Supongamos que ya tienes la función augment_data definida como antes:
def augment_data(X, y, num_samples=1000):
    np.random.seed(42)
    
    # Interpolación entre puntos reales
    idx1 = np.random.randint(0, len(X), num_samples)
    idx2 = np.random.randint(0, len(X), num_samples)
    
    alpha = np.random.uniform(0, 1, num_samples).reshape(-1, 1)
    X_aug = alpha * X.iloc[idx1].values + (1 - alpha) * X.iloc[idx2].values
    y_aug = alpha.flatten() * y.iloc[idx1].values + (1 - alpha.flatten()) * y.iloc[idx2].values
    
    # Agregar ruido gaussiano
    noise_X = np.random.normal(0, 0.01, X_aug.shape)
    noise_y = np.random.normal(0, 0.01, y_aug.shape)
    
    X_aug += noise_X
    y_aug += noise_y
    
    X_aug = pd.DataFrame(X_aug, columns=X.columns)
    y_aug = pd.Series(y_aug, name=y.name)
    
    return X_aug, y_aug

# Dividir los datos en características (X) y etiquetas (y)
X = df_original.drop(columns='price')  # Asumimos que 'price' es la columna de etiquetas
y = df_original['price']

# Generar datos aumentados
X_aug, y_aug = augment_data(X, y, num_samples=2500)

# Concatenar los datos originales con los aumentados
df_augmented = pd.concat([df_original, pd.concat([X_aug, y_aug], axis=1)], axis=0, ignore_index=True)

# Convertir todas las columnas a enteros (si es aplicable)
df_augmented = df_augmented.astype(int)

# Guardar el nuevo archivo CSV con los datos generados como números enteros
output_path = '/home/mike/Escritorio/codes/projects/PropNet/PropNet-project/2_Data_Processing/correlation_analysis/generated_data.csv'
df_augmented.to_csv(output_path, index=False)

print(f"Archivo generado con éxito: {output_path}")
