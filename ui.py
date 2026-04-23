"""
Módulo de interfaz de usuario del sistema DEVSPACES.

Autor: Alonso Rodríguez Bolaños
Fecha: 24/06/2026
"""

import controller
import utils

def ingresar_terminal():
    """Muestra el menu de ingreso para el usuario
    
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
    """Mostrar el menú de ingreso para un usuario existente.
    
    Returns:
        tuple: (nombre_usuario, contraseña) ingresados por el usuario.
    """
    utils.limpiar()
    print("Ingresar al sistema\n")
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    return (nombre_usuario, contrasena)

def menu_interno(nombre_usuario):
    """Muestra el menú interno para un usuario autenticado.
    
    Args:
        nombre_usuario (str): Nombre del usuario autenticado.
    
    Returns:
        str: Opción seleccionada por el usuario.
    """
    utils.limpiar()
    print("Funcionalidades del sistema DevSpace\n")
    print("1. consulta de usuarios")
    print("2. Consulta de spaces")
    print("3. Seguir un space")
    print("4. Consulta de spaces seguidos")
    print("5. Consulta de seguidores de mis spaces")
    print("6. Gestionar seguidores")
    print("7. Consulta de post por space")
    print("8. Cerrar sesión \n")
    respuesta = input("Seleccione una opción: ")
    return (respuesta)

def lista_usuarios_terminal():
    """Muestra la lista de usuarios en la terminal.
    
    Args:
        usuarios (list): Lista de usuarios a mostrar.
    """
    utils.limpiar()
    print("Lista de usuarios:\n")
    usuarios = controller.lista_usuarios()
    
    if usuarios:
        for usuario in usuarios:
            print(f"Usuario: {usuario[0]} | Correo: {usuario[1]}")
    else:
        print("No se pudo obtener la lista de usuarios.")
    input("\nPresione Enter para volver al menú...")
    
def lista_spaces_terminal():
    """Muestra todos los spaces disponibles en el sistema.

    Returns:
        None
    """
    utils.limpiar()
    print("Lista de spaces:\n")
    spaces = controller.lista_spaces()
    if spaces:
        for space in spaces:
            print(f"ID: {space[0]} | Space: {space[1]} | Dueño: {space[2]}")
    else:
        print("No hay spaces disponibles.")
    input("\nPresione Enter para volver al menú...")


def seguir_space_terminal(nombre_usuario):
    """Muestra los spaces disponibles y permite seguir uno.

    Args:
        nombre_usuario (str): Nombre del usuario activo.

    Returns:
        None
    """
    utils.limpiar()
    print("Seguir un space:\n")
    spaces = controller.lista_spaces()
    if spaces:
        for space in spaces:
            print(f"ID: {space[0]} | Space: {space[1]} | Dueño: {space[2]}")

    print("\n1. Seguir un space")
    print("2. Volver al menú principal")
    opcion = input("\nIngrese el número de la opción deseada: ")

    if opcion == "1":
        space_id = input("Ingrese el ID del space que desea seguir: ")
        resultado = controller.seguir_spaces(nombre_usuario, int(space_id))
        if resultado:
            print("Space seguido exitosamente.")
            utils.esperar(2)
        else:
            print("No se pudo seguir el space.")
            utils.esperar(2)
    elif opcion == "2":
        input("\nPresione Enter para volver al menú...")
    else:
        print("Opción no válida.")
        utils.esperar(1)


def mostrar_spaces_seguidos(nombre_usuario):
    """Muestra los spaces que sigue el usuario.

    Args:
        nombre_usuario (str): Nombre del usuario activo.

    Returns:
        None
    """
    utils.limpiar()
    print("Spaces que sigues:\n")
    spaces = controller.lista_space_seguidos(nombre_usuario)
    if spaces:
        for space in spaces:
            print(f"ID: {space[0]} | Space: {space[1]}")
    else:
        print("No sigues ningún space.")
    input("\nPresione Enter para volver al menú...")


def mostrar_seguidores(nombre_usuario):
    """Muestra los seguidores pendientes del usuario.

    Args:
        nombre_usuario (str): Nombre del usuario activo.

    Returns:
        None
    """
    utils.limpiar()
    print("Seguidores de mis spaces:\n")
    seguidores = controller.lista_seguidores(nombre_usuario)
    if seguidores:
        for seguidor in seguidores:
            print(f"Seguidor: {seguidor[0]} | Space: {seguidor[2]}")
    else:
        print("No tienes seguidores pendientes.")
    input("\nPresione Enter para volver al menú...")


def gestionar_seguidores(nombre_usuario):
    """Permite aceptar o rechazar seguidores pendientes.

    Args:
        nombre_usuario (str): Nombre del usuario activo.

    Returns:
        None
    """
    utils.limpiar()
    print("Gestionar seguidores:\n")
    seguidores = controller.lista_seguidores(nombre_usuario)

    if not seguidores:
        print("No tienes solicitudes pendientes.")
        utils.esperar(2)
        return

    for seguidor in seguidores:
        print(f"\nSeguidor: {seguidor[0]} | Space: {seguidor[2]}")
        print("1. Aceptar")
        print("2. Rechazar")
        decision = input("\nOpción: ")

        if decision == "1":
            respuesta = controller.gestionar_seguidor(nombre_usuario, seguidor[1], seguidor[0], True)   
            if respuesta:
                print("Seguidor aceptado.")
            else:
                print("No se pudo aceptar.")
        elif decision == "2":
            respuesta = controller.gestionar_seguidor(nombre_usuario, seguidor[1], seguidor[0], False)
            if respuesta:
                print("Seguidor rechazado.")
            else:
                print("No se pudo rechazar.")
        utils.esperar(1)

    input("\nPresione Enter para volver al menú...")


def mostrar_posts(nombre_usuario):
    """Permite ver los posts de un space con navegación.

    Args:
        nombre_usuario (str): Nombre del usuario activo.

    Returns:
        None
    """
    utils.limpiar()
    print("Consulta de posts por space:\n")

    spaces = controller.lista_spaces()
    for space in spaces:
        print(f"ID: {space[0]} | Space: {space[1]} | Dueño: {space[2]}")

    id_space = int(input("\nIngrese el ID del space: "))
    posts = controller.buscador_posts(id_space)

    if not posts:
        print("No hay posts en este space.")
        utils.esperar(2)
        return

    indice = 0
    while True:
        utils.limpiar()
        post = posts[indice]
        print(f"Post {indice + 1} de {len(posts)}\n")
        print(f"Título: {post[1]}\n")

        if post[3] == "post":
            utils.animador(post[2])
        else:
            utils.resaltar(post[2])

        print("\n1. Primer post  2. Anterior  3. Siguiente  4. Último post  5. Salir")
        nav = input("\nOpción: ")

        if nav == "1":
            utils.limpiar
            indice = 0
        elif nav == "2":
            utils.limpiar
            indice = max(indice - 1, 0)
        elif nav == "3":
            utils.limpiar
            indice = min(indice + 1, len(posts) - 1)
        elif nav == "4":
            utils.limpiar
            indice = len(posts) - 1
        elif nav == "5":
            break
        else:
            print("Opción no válida.")
            utils.esperar(1)

    input("\nPresione Enter para volver al menú...")