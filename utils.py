"""
Módulo de utilidades del sistema DEVSPACES.

Autor: Alonso Rodríguez Bolaños
Fecha: 24/06/2026
"""

import os
import re
import time

#!=================
#!    COLORES
#!=================

RESET = "\033[0m"
VERDE = "\033[92m"
AZUL = "\033[94m"
AMARILLO = "\033[93m"
ROJO = "\033[91m"
CYAN = "\033[96m"

#!=================
#!    PALABRAS
#!=================

COLOR_1 = ["if", "else", "elif", "for","import", "while"]

COLOR_2 = ["True", "False", "None", "def", "and", "or", "not"]

COLOR_3 = ["print", "input"]

#!===================
#!     Esperar
#!===================

def esperar(segundos):
    """Pausa la ejecución durante un número específico de segundos.

    Args:
        segundos (int): Número de segundos a esperar.

    Returns:
        None
    """
    time.sleep(segundos)
    
    
#!=================
#!  TEXTO ANIMADO
#!=================

def animador(contenido):
    """Muestra texto línea por línea con pausa entre cada una.

    Args:
        contenido (str): Texto a mostrar animado.

    Returns:
        None
    """
    lineas = contenido.split("\n")
    for linea in lineas:
        for caracter in linea:
            print(caracter, end="", flush=True)
            esperar(0.05)
        print()
        esperar(0.5)

#!=================
#! TEXTO RESALTADO
#!=================

def resaltar(contenido):
    """Resalta palabras clave de Python en color para snippets de código.

    Args:
        contenido (str): Código Python a resaltar.

    Returns:
        None
    """
    for linea in contenido.split("\n"):
        for palabra in COLOR_1:
            linea = re.sub(r'\b' + palabra + r'\b', ROJO + palabra + RESET, linea)
        for palabra in COLOR_2:
            linea = re.sub(r'\b' + palabra + r'\b', AZUL + palabra + RESET, linea)
        for palabra in COLOR_3:
            linea = re.sub(r'\b' + palabra + r'\b', AMARILLO + palabra + RESET, linea)
        print(linea)
        
#!===================
#! Limpiar Terminal
#!===================

def limpiar():
    """Limpia la terminal para mejorar la experiencia de usuario.

    Returns:
        None
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
#!===================
#!     Invalido
#!===================

def invalido():
    """Imprime en rojo opcion no valida
    
    Returns:
        None
    """
    limpiar()
    print("Opción no válida.")
    esperar(2)