import pandas as pd
import numpy as np

def limpiar(df):

        print('Cantidad de Filas y columnas originales:',df.shape)
        #Cambiar los elementos vacíos por un NaN
        df = df.replace('',np.nan)
        #Borrar todas las columnas que tengan el mismo elemento
        df=df[[i for i in df if len(set(df[i]))>1]]
        #Borrar todas las filas que tengan algún NaN
        df = df.dropna(axis="rows",how="any")
        print('Cantidad de Filas y columnas tras la limpieza:',df.shape)
        df.to_csv("./Datasets/batch_data_filtrado.csv",index=False)
        #print("Generado batch_data_filtrado.csv")

        return df
