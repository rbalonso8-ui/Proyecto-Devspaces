"""
Módulo principal del sistema DevSpaces

Autor: Alonso Rodríguez Bolaños
Fecha: 24/06/2026
"""

import sys
sys.path.append('./API')
import devspace as ds

def login(nombre_usuario, contraseña):
    """Establecer el menú de opciones para el ingreso de un usuario existente en el sistema de DevSpace.

    Returns:
        tuple: (nombre_usuario, user_id) si el ingreso es exitoso, False si falla.
    """
    resultado = ds.login(nombre_usuario, contraseña)
    if resultado[0]:
        return (nombre_usuario, resultado[0])
    else:
        return (False)
    
