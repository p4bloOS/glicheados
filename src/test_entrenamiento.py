import entrenamiento1 as e
import pandas as pd

"""
Este programa entrena un modelo que se guarda en formato pickle (fichero modelo1.pkl)
usando las muestras almacenadas en batch_data.csv
"""

#%% Ejecución particularizada del entrenamiento

df = pd.read_csv ("./Datasets/batch_data_filtrado.csv")
df.to_json ("./Datasets/batch_data_train.json")

metricas = e.entrenamiento1("./Datasets/batch_data_train.json", "modelo1.pkl")

file = open("json_metrics.json", 'w')
file.write(metricas)
file.close()
print("json_metrics -> ", metricas)
