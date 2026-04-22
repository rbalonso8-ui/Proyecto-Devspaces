"""
Módulo de utilidades del sistema DEVSPACES.

Autor: Alonso Rodríguez Bolaños
Fecha: 24/06/2026
"""

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

PALABRAS_CLAVE = ["def", "if", "else", "elif", "return", "import", "for", "while", "True", "False", "int", "str", "float", "and", "or", "not", "print", "input", "None", "in"]

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
            time.sleep(0.05)
        print()
        time.sleep(0.5)

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
        for palabra in PALABRAS_CLAVE:
            linea = linea.replace(palabra, VERDE + palabra + RESET)
        print(linea)
        
#!===================
#! Limpiar Terminal
#!===================

def limpiar():
    """Limpia la terminal para mejorar la experiencia de usuario.

    Returns:
        None
    """
    print("\033[H\033[J", end="")
    
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