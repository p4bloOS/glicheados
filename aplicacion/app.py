#!/usr/bin/python

import PySimpleGUI as sg
import numpy as np
import prediccion1 as pred
import json

escuchando = 0
umbral = 0.5
mensaje = ""



# Personalización del tema
my_new_theme = {'BACKGROUND': '#1A1B2E',
                'TEXT': '#00BCD4',
                'INPUT': '#2E3052',
                'TEXT_INPUT': 'white',
                'SCROLL': '#00BCD4',
                'BUTTON': ('#00BCD4', '#2E3052'),
                'PROGRESS': ('#074CB3', '#D0D0D0'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}
sg.theme_add_new('MyNewTheme', my_new_theme)
sg.theme('My New Theme')
font = ("", 15)
sg.set_options(font=font)

# Cuadro de diálogo
# sg.popup_get_text('Hola, cuadro de diálogo') 

items = [ [sg.Text('____ DETECTOR DE PIEZAS DEFECTUOSAS ____', key='-TITULO-' )],
        [sg.Text('Umbral de fiabilidad:' ), sg.Input(key='-IN-'), sg.Button('Establecer')],
          [sg.Text('*Umbral actual = ' ), sg.Text('0.5',key='-UMBRAL-ACTUAL-')],
          [sg.Text('*(es una medida entre 0.0 y 1.0)')],
          [sg.Text(' ')],
          [sg.Button('COMENZAR PROCESO'), sg.Button('ACTUALIZAR')],
          [sg.Text("---------------------------------------------------------------------------------------------------------------------")],
          [sg.Text(" ", key='-MENSAJE-')],
          [sg.Text("---------------------------------------------------------------------------------------------------------------------")],
          [ sg.Button('Salir')] ]

#sg.Text(text_color ='white', key='-OUTPUT-') 

#window = sg.Window('Primera interfaz en Python', resizable=True, layout, finalize=True)
window = sg.Window('Detector de piezas defectuosas',
                resizable=True,
                layout=items,
                finalize=True)
# window['-IN-'].expand(True, False)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Salir':
        break
    if event == 'Establecer':
        # Update the "output" text element to be the value of "input" elementn
        umbral_in = values['-IN-']
        try:
            umbral_in = float(umbral_in)
            if umbral_in>=0 and umbral_in<=1:
                umbral = umbral_in
        except:
            print("No es número válido")
        window['-UMBRAL-ACTUAL-'].update(umbral)
    if event == 'COMENZAR PROCESO':
        print("Escuchando...")
        escuchando = 1
        window['-MENSAJE-'].update("Esperando nuevas muestras...")

    if event == 'ACTUALIZAR':

        if escuchando == 1:
            print("Comprobando")
            try:
                with open("./aplicacion/.muestra.json") as fJson:
                    muestra = json.load(fJson)
                resultado = pred.prediccion1(muestra, "modelo1.pkl")
                fiabilidad = json.loads(resultado)["payload"][0]["value"]
                mensaje = "Detectada una pieza con fiabilidad " + str(fiabilidad)
                if fiabilidad >= umbral:
                    mensaje = mensaje + "  >>>   ADMISIBLE"
                else:
                    mensaje = mensaje + "  >>>   DEFECTUOSA"
            except FileNotFoundError:
                print("ficheo no encontrado")

        window['-MENSAJE-'].update(mensaje)
        print("Mensaje interfaz", mensaje)

window.close()