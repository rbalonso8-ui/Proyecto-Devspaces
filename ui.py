"""
Módulo de interfaz de usuario del sistema DEVSPACES.

Autor: Alonso Rodríguez Bolaños
Fecha: 24/06/2026
"""

import time
import utils
import controller

def ingresar_terminal():
    """
    Muestra el menu de ingreso para el usuario
    
    Returns: 
        str: opcion seleccionada por el usuario
    """
    utils.limpiar()
    print("Bienvenido a DevSpaces\n")
    print("Seleccione una opción: \n")
    print("1. Ingresar al sistema")
    print("2. Salir")
    opcion = input("\nIngrese el número de la opción deseada: ")
    return (opcion)

def login_terminal():
    """
    Mostrar el menú de ingreso para un usuario existente.
    
    Returns:
        tuple: (nombre_usuario, contraseña) ingresados por el usuario.
    """
    utils.limpiar()
    print("Ingresar al sistema\n")
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    return (nombre_usuario, contrasena)