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
        return (nombre_usuario, resultado[1])
    else:
        return (False)
    
def lista_usuarios():
    """Obtiene la lista de usuarios del sistema.

    Returns:
        list: Lista de usuarios o lista vacía si falla.
    """
    resultado, data = ds.get_users()
    if resultado:
        return (data)
    return []

def lista_spaces():
    """Obtiene la lista de spaces.
    
    Returns:
        list: Lista de spaces con (id, nombre, dueño) o lista vacía si falla.
    """
    usuarios = lista_usuarios()
    spaces = []
    for user in usuarios:
        resultado, data = ds.get_spaces_by_user(user[0])
        if resultado:
            for space in data:
                spaces.append((space[0], space[1], user[0]))
    return (spaces)

def seguir_spaces(nombre_usuario, space_id):
    """Permite a un usuario seguir un space.

    Args:
        nombre_usuario (str): Nombre del usuario que desea seguir el space.
        space_id (int): ID del space que se desea seguir.

    Returns:
        bool: True si funciono o False si falla.
    """
    resultado = ds.follow_space(nombre_usuario, space_id)
    return (resultado[0])

def lista_space_seguidos(nombre_usuario):
    """Obtiene la lista de spaces que un usuario sigue.

    Args:
        nombre_usuario (str): Nombre del usuario.

    Returns:
        list: Lista de spaces seguidos con (id, nombre, dueño) o lista vacía si falla.
    """
    resultado, data = ds.get_following_spaces(nombre_usuario)
    if resultado:
        return (data)
    return []

def lista_seguidores(nombre_usuario):
    """Obtiene los seguidores pendientes del usuario.

    Args:
        nombre_usuario (str): Nombre del usuario.

    Returns:
        list: Lista de seguidores pendientes o lista vacía si falla.
    """
    resultado, data = ds.get_followers(nombre_usuario)
    if resultado:
        return data[1]
    return []

def gestionar_seguidor(nombre_usuario, space_id, seguidor, aceptar):
    """Acepta o rechaza un seguidor.

    Args:
        nombre_usuario (str): Nombre del dueño del space.
        space_id (int): ID del space.
        seguidor (str): Nombre del seguidor.
        aceptar (bool): True para aceptar, False para rechazar.

    Returns:
        bool: True si fue exitoso o False si falló.
    """
    resultado, data = ds.handle_follower(nombre_usuario, int(space_id), seguidor, aceptar)
    return (resultado)

def buscador_posts(id_space):
    """Obtiene los posts de un space buscando su dueño automáticamente.

    Args:
        id_space (int): ID del space.

    Returns:
        list: Lista de posts o lista vacía si falla.
    """
    spaces = lista_spaces()
    dueño = None
    for space in spaces:
        if space[0] == id_space:
            dueño = space[2]

    if not dueño:
        return []

    resultado, data = ds.get_posts(id_space, dueño)
    if resultado:
        return (data[1])
    return []