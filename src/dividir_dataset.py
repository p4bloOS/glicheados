import pandas as pd
import numpy as np
import limpieza as lim
from sklearn.model_selection import train_test_split

df = pd.read_csv("./Datasets/batch_data.csv")
df = lim.limpiar(df)
muestras_entrenamiento,muestras_testeo = train_test_split(df, test_size=0.2,random_state=25)
print("Muestras entrenamiento: ", muestras_entrenamiento.shape[0])
print("Muestras testeo: " ,muestras_testeo.shape[0])
muestras_entrenamiento.to_csv("./Datasets/batch_data_train.csv",index=False)
muestras_testeo.to_csv("./Datasets/batch_data_test.csv",index=False)
