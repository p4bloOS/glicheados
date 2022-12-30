# -*- coding: utf-8 -*-

import pandas as pd
import pickle
import json
from datetime import datetime

def prediccion1(json_data,s_model):
    """Calcula predicciones para nuevos datos

    Parámetros
    ----------
    json_data : str
        Fichero JSON con datos para hacer la predicción.

    s_model: str
        La ruta donde está almacenado el modelo.
    
        
    Returns
    ----------
        A JSON with the following information:
            "id": data identifier (index) 
            "timestamp": time in which the prediction is done
            "payload": contains the following information:
                "name": name of the response variable
                "value": predicted value for the response variable
            "raw_data": the data used for the prediction
        
    """
    
    #%% DON'T touch the following lines
    # Load model
    with open(s_model, 'rb') as file:
        model = pickle.load(file)
    # Load data
    df = pd.DataFrame(json_data, index=[0])
    # We will assume that the first column is the index (timestamp, serial  number, ...)
    df.set_index(df.columns.values[0], inplace=True)
    
    
    
    #%% Start your code here
    
    # Preprocessing
    X_pred = model.scaler.transform(df[model.predictors])
    
    # Make predictions
    y_pred = model.predict(X_pred)
    
    # There should be just one observation at a time
    y_pred = float(y_pred[0]) # prediction should be passed as a float
    
    # End your code here
    
    
    
    #%% DON'T touch the following lines
    # export results as JSON
    data = {"id": str(df.index[0]),
            "timestamp": datetime.now().isoformat(timespec='milliseconds')+'Z',
            "payload": [
                        {
                            "name": model.response,
                            "value": y_pred
                        },
                    ],
            "raw_data": json_data
            }
    #print(data)
    json_results = json.dumps(data, indent=4)
    return json_results
