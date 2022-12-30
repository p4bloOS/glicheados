# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import json
import pickle
import limpieza

def entrenamiento1(json_data,
          s_model):
    """
    
    Parámetros
    ----------
    csv_data : string
        Fichero csv con los datos de entrenamiento.
    s_model : string
        La ruta donde se almacenará el modelo.
    
    Returns
    ----------
    json_metrics : string (JSON)
        a JSON with the following metrics:
            - R2 (r-squared)
    
    """
    
    #%% DON'T touch the following lines
    # Read data
    print("Leyendo dataset...")
    df = pd.read_json(json_data)
    print("Lectura finalizada")

    # Limpieza de datos
    #df=limpieza.limpiar(df)

    train,test = train_test_split(df, test_size=0.2,random_state=25)

    
    # By conventionm "response" is the last column in the dataset
    response = df.columns.values.tolist()[-1]
    #response_train = train.columns.values.tolist()[-1]
    #response_test = test.columns.values.tolist()[-1]
    # Get predictors as the rest of data
    predictors = df.columns.values.tolist()
    predictors.remove(response)
    #predictors_train = train.columns.values.tolist()
    #predictors_test = test.columns.values.tolist()
    #predictors_train.remove(response_train)
    #predictors_test.remove(response_test)
    
    
    
    #%% Start your code here
    
    # df -> contiene los datos de entrenamiento
    # response_train -> es la última columna del dataset (etiqueta asociada a cada muestra del entrenamiento)
    # response_test -> es la última columna del dataset (etiqueta asociada a cada muestra del test)
    # predictors_train -> "predictor variables" (variables de predicción de muestras para entrenar)
    # predictors_test -> "predictor variables" (variables de predicción de muestras para testear)

    # Preprocesamiento 
    scaler = StandardScaler()
    X_train = scaler.fit_transform(df[predictors])
    #X_train = scaler.fit_transform(train[predictors_train])
    #X_test = scaler.fit_transform(test[predictors_test])
    # Entrenamiento
    y_train = df[response].values
    #y_train = train[response_train].values
    #y_test = test[response_test].values
    #print("y_train[30] -> ", y_train[30])
    #model = LinearRegression()
    model = DecisionTreeRegressor()
    #model = RandomForestRegressor()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_train)
    #y_pred = model.predict(X_test)
    
    # Almacena cualquier cosa que necesitemos en tiempo de predicción...
    #model.response = response_train
    #model.predictors = predictors_train
    model.response = response
    model.predictors = predictors
    model.scaler = scaler
    
    print("R2 que da: ",r2_score(y_train, y_pred))
    
    #%% DON'T touch the following lines
    dict_metrics = [{'name': 'R2', 'value': r2_score(y_train, y_pred)}]
    model.train_metrics = dict_metrics
    json_metrics = json.dumps(dict_metrics, indent = 4)
    
    # Create model pickle file
    with open(s_model, 'wb') as file:
        pickle.dump(model, file)
        
    print("Finalizando entrenamiento1 con éxito. Generado modelo1.pkl")
    return json_metrics
