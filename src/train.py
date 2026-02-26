import pandas as pd
import os
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier

def train_model():
    print("Iniciando entrenamiento del modelo campeón (XGBoost)")

    # 1. Cargamos datos de entrenamiento
    train_df = pd.read_csv('data/training/train.csv')
    X_train = train_df.drop('Exited', axis=1)
    y_train = train_df['Exited']

    # 2. Definir preprocesamiento
    cat_cols = ['Geography', 'Gender']
    num_cols = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), num_cols),
            ('cat', OneHotEncoder(drop='first'), cat_cols)
        ]
    )

    # 3. Crear y entrenar el Pipeline
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', XGBClassifier(random_state=42, eval_metric='logloss', scale_pos_weight=3))
    ])

    pipeline.fit(X_train, y_train)

    # 4. Serializar (Guardar) el modelo
    model_path = os.path.join('models', 'champion_model.pkl')
    joblib.dump(pipeline, model_path)

    print(f"Modelo entrenado y guardado exitosamente en: {model_path}")

if __name__ == '__main__':
    train_model()