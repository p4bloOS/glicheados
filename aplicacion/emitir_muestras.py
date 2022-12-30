import csv 
import json
import time

#Simula un flujo periódico de muestras que se almacenan
# momentánemente en un archivo, el cualcambiará cada 4 segundos

#Leemos el conjunto de test
print("Leyendo dataset...")
with open("./Datasets/batch_data_test.csv", encoding='utf-8') as csvf:

    csvReader = csv.DictReader(csvf)

    #hemos convertido cada fila del csv en un diccionario para agregarlo a jsonArray
    for i,row in enumerate(csvReader):
        time.sleep(4)
        # Concatenamos un id que es el índice en el conjunto de muestras
        row = {'id': i} | row
        # print("-                   Añadido al array json (indice ",i,") (reliability = ", fiabilidad,"): ", row)
        #jsonString = json.dumps(row, indent=4)
        jsonString = json.dumps(row, indent = 4)
        jsonFile = open("./aplicacion/.muestra.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        print(".muestra.json generado")
        
print("Emisión de muestras finalizada")