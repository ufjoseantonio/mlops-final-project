import pandas as pd
import os
import joblib
import mlflow
import mlflow.sklearn
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

    # Creamos un experimento oficial para producción
    mlflow.set_experiment("Bank_Churn_Production_Training")

    with mlflow.start_run() as run:
        # Entrenamos el modelo
        pipeline.fit(X_train, y_train)

        # 4A. Guardamos localmente en la bóveda física .pkl
        model_path = os.path.join('models', 'champion_model.pkl')
        joblib.dump(pipeline, model_path)

        # 4B. REGISTRO
        # Guardamos y registramos el modelo oficial en la vitrina de MLflow
        mlflow.sklearn.log_model(
            sk_model=pipeline,
            artifact_path="xgboost_pipeline",
            registered_model_name="BankChurn_ChampionModel"
        )

        print(f" Modelo entrenado y guardado localmente en: {model_path}")
        print(f" Modelo Registrado en MLflow como: 'BankChurn_ChampionModel'")

if __name__ == '__main__':
    train_model()