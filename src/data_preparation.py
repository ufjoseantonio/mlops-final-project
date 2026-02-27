import pandas as pd
import os
from sklearn.model_selection import train_test_split

def prepare_data():
    print("Iniciando preparación de los datos")

    # 1. Cargamos los datos crudos
    df = pd.read_csv('data/raw/churn_data.csv')

    # 2. Dividimos en Entrenamiento (80%) y Prueba (20%)
    # Usamos stratify para mantener la proporción de abandono
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df['Exited'])

    # 3. Guardar los datasets finales
    train_path = os.path.join('data', 'training', 'train.csv')
    test_path = os.path.join('data', 'training', 'test.csv')

    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)

    print(f"Datos preparados exitosamente.")
    print(f"Train guardado en: {train_path} ({len(train_df)} filas)")
    print(f"Test guardado en: {test_path} ({len(test_df)} filas)")

if __name__ == '__main__':
    prepare_data()