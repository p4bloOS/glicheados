Proyecto para la Hackaton ZDMP

Lunes, 19 de diciembre
        a  
Miercoles, 21 de diciembre

Equipo: Glicheados
Autores: Germán Rodríguez Díez, Pablo Gimeno Hermán & Álvaro Pardo Ponce
-----------------------------------

BREVE DESCRIPCIÓN DEL PROBLEMA

Este proyeto consiste en desarrollar un modelo de IA que detecte piezas defectuosas en una linea de producción.

------------------------------

Instrucciones de ejecución:

1. Situarse en el directorio base del repositorio:   
    cd glicheados
2. Limpiar y dividir el dataset:
    python src/dividir_dataset.py
3. Ejecutar el entrenamiento:
    python src/test_entrenamiento.py
4. Ejecutar predicciones de prueba:
    python src/test_prediccion.py
5. Iniciar la aplicacion:
    python aplicacion/emitir_muestras.py &
    
    python aplicacion/app.py

------------------------------

Las bibliotecas de python necesarias se indican en:
requirements.txt
