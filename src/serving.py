from flask import Flask, request, jsonify
import joblib
import pandas as pd
import xgboost
import os

# Inicializamos la aplicación Flask
app = Flask(__name__)

# Ubicamos el modelo
MODEL_PATH = "models/champion_model.pkl"

# Cargamos el modelo en memoria al iniciar el servidor
model = None
if os.path.exists(MODEL_PATH):
    try:
        model = joblib.load(MODEL_PATH)
        print(f"ÉXITO: Modelo cargado correctamente desde {MODEL_PATH}")
    except Exception as e:
        print(f"ERROR al cargar el modelo: {e}")
else:
    print(f"ERROR: No se encontró el modelo en {MODEL_PATH}")

@app.route('/', methods=['GET'])
def home():
    """Endpoint de salud para verificar que la API está viva"""
    return jsonify({
        "mensaje": "Bienvenido a la API de prediccion de Bank Churn",
        "estado_modelo": "Cargado" if model else "No encontrado"
    })

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint principal para realizar predicciones"""
    if not model:
        return jsonify({"error": "El modelo no está disponible en el servidor."}), 500
    
    try:
        # 1. Recibimos los datos del cliente en formato JSON
        data = request.get_json()

        # 2. Convertimos el JSON a un DataFrame (formato que entiende XGBoost)
        # Asumimos que se envía un solo cliente a la vez
        df = pd.DataFrame([data])

        # 3. Realizamos la predicción
        prediccion = model.predict(df)

        # 4. Extraemos el resultado numérico (0 = Se queda, 1 = Abandono)
        resultado = int(prediccion[0])

        # 5. Formatear y devolver la respuesta
        return jsonify({
            "prediccion": resultado,
            "interpretacion": "El cliente ABANDONARÁ el banco" if resultado == 1 else "El cliente se QUEDARÁ"  
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # Levantamos el servidor en el puerto 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
