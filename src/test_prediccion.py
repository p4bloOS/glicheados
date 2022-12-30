import prediccion1 as p
import csv 
import json

"""
A continuación se realizan predicciones.

Método de partición de datos utilizado: 80% entrenamiento previo, 20% test
"""

#%% Ejecución particularizada de predicciones

jsonArray = []
arrayReliability = []

#Leemos el conjunto de test
print("Leyendo dataset...")
with open("./Datasets/batch_data_test.csv", encoding='utf-8') as csvf:

    csvReader = csv.DictReader(csvf)

    #hemos convertido cada fila del csv en un diccionario para agregarlo a jsonArray
    for i,row in enumerate(csvReader):
        #add this python dict to json array
        # Concatenamos un id que es el índice en el conjunto de test
        row = {'id': i} | row
        # y borramos reliability, guardando su valor
        fiabilidad = row.pop('reliability')
        # print("-                   Añadido al array json (indice ",i,") (reliability = ", fiabilidad,"): ", row)
        #jsonString = json.dumps(row, indent=4)
        jsonArray.append(row)
        arrayReliability.append(fiabilidad)


# Invocamos la predicción para cada muestra
print("Ejecutando predicciones. Ejemplos: ")
for i, (v, json_data) in enumerate(zip(arrayReliability, jsonArray)):

    #Invocamos la predicción
    #f = open(".muestra.json")
    resultado = p.prediccion1(json_data, "modelo1.pkl") #devuelve json que podríamos guardar como fichero
    #f.close()

    #Obtenemos los valores
    jsonCargado = json.loads(resultado)
    vPrediccion = jsonCargado["payload"][0]["value"]
    # vPrediccion = valor reliability calculado
    # v = valor reliability observado
    if i % 200 == 0:
        print("Muestra nº ", i,". Valor observado = ", v, ". Valor calculado = ", vPrediccion)


print("Test finalizado")
