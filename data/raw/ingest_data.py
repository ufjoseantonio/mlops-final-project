import pandas as pd
import os

def download_data():
    print("Iniciando la descarga del dataset de Bank Customer Churn")

    # URL del dataset público de Bank Customer Churn
    url = "http://raw.githubusercontent.com/sharmaroshan/Churn-Modelling-Dataset/master/Churn_Modelling.csv"

    try: 
        # Leemos directamente desde la web
        df = pd.read_csv(url)

        # Eliminamos columnas que no aportan al ML (como ID  del cliente o Apellido)
        df = df.drop(columns=['RowNumber', 'CustomerId', 'Surname'])

        # Guardamos en nuestra carpeta local
        output_path = os.path.join("data", "raw", "churn_data.csv")
        df.to_csv(output_path, index=False)

        print(f"´Dataset descargado y guardado en: {output_path}")
        print(f"Total de filas: {df.shape[0]}, Total de columnas: {df.shape[1]}")

    except Exception as e:
        print(f"Error al descargar los datos: {e}")

if __name__ == "__main__":
    download_data()