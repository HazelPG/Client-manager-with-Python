import os
import platform

#FUNCION AUXILIAR PARA LIMPIAR EN CUALQUIER SISTEMA OPERATIVO
def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

#FUNCION AUXILIAR PARA LEER Y VALIDAR EL TEXTO INGRESADO POR CONSOLA
def input_text(min_length, max_length):
    while True:
        text = input("> ")
        if len(text) >= min_length and len(text) <= max_length:
            return text

