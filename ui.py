"""
Módulo de interfaz de usuario del sistema DEVSPACES.

Autor: Alonso Rodríguez Bolaños
Fecha: 24/04/2026
"""

import controller
import utils

#? ===================
#?     Ingresar
#? ===================

def ingresar_terminal():
    """Muestra el menu de ingreso para el usuario
    
    Returns: 
        str: opcion seleccionada por el usuario
    """
    utils.limpiar()
    print(utils.colorear("Bienvenido a DevSpaces\n", 2))
    print("Seleccione una opción: \n")
    print(utils.colorear("     1. Ingresar",4))
    print(utils.colorear("     2. Salir",1))
    opcion = input("\nSeleccione una opción: ")
    return (opcion)

#? ===================
#?       Login
#? ===================

def login_terminal():
    """Mostrar el menú de ingreso para un usuario existente.
    
    Returns:
        list: si funciona envia una lista con True y las credenciales del usuario
        bool: False si no funciono el proceso
    """
    utils.limpiar()
    print(utils.colorear("Ingresar al sistema\n",2))
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    resultado = controller.login(nombre_usuario, contraseña)
    if resultado:
        nombre_usuario, user_id = resultado
        print(utils.colorear(f"\nIngreso exitoso. Bienvenido, {nombre_usuario}.", 4))
        utils.esperar(2)
        return([True, nombre_usuario, user_id])
    else:
        print(utils.colorear("\nCredenciales incorrectas. Intente nuevamente.", 1))
        utils.esperar(2)
        return (False)
    
#? ===================
#?    Menú interno
#? ===================

def menu_interno(nombre_usuario):
    """Muestra el menú interno para un usuario autenticado.
    
    Args:
        nombre_usuario (str): Nombre del usuario autenticado.
    
    Returns:
        str: Opción seleccionada por el usuario.
    """
    utils.limpiar()
    print(utils.colorear("Funcionalidades del sistema DevSpace\n", 2))
    print("\t1. consulta de usuarios")
    print("\t2. Consulta de spaces")
    print("\t3. Seguir un space")
    print("\t4. Consulta de spaces seguidos")
    print("\t5. Consulta de seguidores de mis spaces")
    print("\t6. Gestionar seguidores")
    print("\t7. Consulta de post por space")
    print("\t8. Cerrar sesión \n")
    respuesta = input(utils.colorear("Seleccione una opción: ", 2))
    return (respuesta)

#? ===================
#?      Usuarios
#? ===================

def lista_usuarios_terminal():
    """Muestra la lista de usuarios en la terminal.
    
    Args:
        usuarios (list): Lista de usuarios a mostrar.
    """
    utils.limpiar()
    print(utils.colorear("Lista de usuarios:\n", 2))
    usuarios = controller.lista_usuarios()
    color = 0
    
    if usuarios:
        for usuario in usuarios:
            if color == 0:
                print(utils.colorear(f"Usuario: {usuario[0]} | Correo: {usuario[1]}", 4))
                color +=1
            else:
                print(utils.colorear(f"Usuario: {usuario[0]} | Correo: {usuario[1]}", 3))
                color -= 1
    else:
        print(utils.colorear("No se pudo obtener la lista de usuarios.", 1))
    
#? ===================
#?      Spaces
#? ===================

def lista_spaces_terminal():
    """Muestra todos los spaces disponibles en el sistema.

    Returns:
        None
    """
    utils.limpiar()
    print(utils.colorear("Lista de spaces:\n", 2))
    spaces = controller.lista_spaces()
    color = 0
    
    if spaces:
        for space in spaces:
            if color == 0:
                print(utils.colorear(f"ID: {space[0]} | Space: {space[1]} | Dueño: {space[2]}", 4))
                color += 1
            else:
                print(utils.colorear(f"ID: {space[0]} | Space: {space[1]} | Dueño: {space[2]}", 3))
                color -= 1
    else:
        print(utils.colorear("No hay spaces disponibles.", 1))
        
#? ===================
#?    Seguir Space
#? ===================

def seguir_space_terminal(nombre_usuario):
    """Muestra los spaces disponibles y permite seguir uno.

    Args:
        nombre_usuario (str): Nombre del usuario activo.

    Returns:
        None
    """
    lista_spaces_terminal()

    print("\n1. Seguir un space")
    print("2. Volver al menú principal")
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        space_id = input("Ingrese el ID del space que desea seguir: ")
        resultado = controller.seguir_spaces(nombre_usuario, int(space_id))
        if resultado:
            print(utils.colorear("Space seguido exitosamente.", 4))
            utils.esperar(2)
        else:
            print(utils.colorear("No se pudo seguir el space.", 1))
            utils.esperar(2)
    elif opcion == "2":
        input("\nPresione Enter para volver al menú...")
    else:
        utils.invalido()
        
#? ===================
#?      Seguidos
#? ===================

def mostrar_spaces_seguidos(nombre_usuario):
    """Muestra los spaces que sigue el usuario.

    Args:
        nombre_usuario (str): Nombre del usuario activo.

    Returns:
        None
    """
    utils.limpiar()
    print(utils.colorear("Spaces que sigues:\n", 2))
    spaces = controller.lista_space_seguidos(nombre_usuario)
    color = 0
    
    if spaces:
        for space in spaces:
            if color == 0:
                print(utils.colorear(f"ID: {space[0]} | Space: {space[1]}",4))
                color += 1
            else:
                print(utils.colorear(f"ID: {space[0]} | Space: {space[1]}",3))
                color -= 1
    else:
        print(utils.colorear("No sigues ningún space.",1))
    input("\nPresione Enter para volver al menú...")

#? ===================
#?    Seguidores
#? ===================

def mostrar_seguidores(nombre_usuario):
    """Muestra los seguidores pendientes del usuario.

    Args:
        nombre_usuario (str): Nombre del usuario activo.

    Returns:
        None
    """
    utils.limpiar()
    print(utils.colorear("Seguidores de mis spaces:\n", 2))
    seguidores = controller.lista_seguidores(nombre_usuario)
    color = 0
    
    if seguidores:
        for seguidor in seguidores:
            if color == 0:
                print(utils.colorear(f"Seguidor: {seguidor[0]} | Space: {seguidor[2]}", 4))
                color += 1
            else:
                print(utils.colorear(f"Seguidor: {seguidor[0]} | Space: {seguidor[2]}", 3))
                color -= 1
    else:
        print("No tienes seguidores pendientes.")
    input("\nPresione Enter para volver al menú...")
    
#? ========================
#?  Gestionar Seguidores
#? ========================

def gestionar_seguidores(nombre_usuario):
    """Permite aceptar o rechazar seguidores pendientes.

    Args:
        nombre_usuario (str): Nombre del usuario activo.

    Returns:
        None
    """
    utils.limpiar()
    print(utils.colorear("Gestionar seguidores:\n", 2))
    seguidores = controller.lista_seguidores(nombre_usuario)

    if not seguidores:
        print(utils.colorear("No tienes solicitudes.", 1))
        utils.esperar(2)
        return

    for seguidor in seguidores:
        print(f"\nSeguidor: {seguidor[0]} | Space: {seguidor[2]}\n")
        print(utils.colorear("\t1. Aceptar", 4))
        print(utils.colorear("\t2. Rechazar",1))
        decision = input("\nOpción: ")

        if decision == "1":
            respuesta = controller.gestionar_seguidor(nombre_usuario, seguidor[1], seguidor[0], True)   
            if respuesta:
                print(utils.colorear("\nSeguidor aceptado.", 4))
            else:
                print(utils.colorear("\nNo se pudo aceptar.", 1))
        elif decision == "2":
            respuesta = controller.gestionar_seguidor(nombre_usuario, seguidor[1], seguidor[0], False)
            if respuesta:
                print(utils.colorear("\nSeguidor rechazado.", 1))
            else:
                print(utils.colorear("\nNo se pudo rechazar.", 1))
        utils.esperar(1)

    input("\nPresione Enter para volver al menú...")

#? ===================
#?       Posts
#? ===================

def mostrar_posts(nombre_usuario):
    """Permite ver los posts de un space con navegación.

    Args:
        nombre_usuario (str): Nombre del usuario activo.

    Returns:
        None
    """
    utils.limpiar()
    print(utils.colorear("Consulta de posts por space:\n", 2))

    lista_spaces_terminal()

    id_space = int(input("\nIngrese el ID del space: "))
    posts = controller.buscador_posts(id_space)

    if not posts:
        print(utils.colorear("No hay posts en este space.", 1))
        utils.esperar(2)
        return

    indice = 0
    while True:
        utils.limpiar()
        post = posts[indice]
        print(utils.colorear(f"Post {indice + 1} de {len(posts)}\n", 2))
        print(utils.colorear(f"Título: {post[1]}\n", 3))

        if post[3] == "post":
            utils.animador(post[2])
        else:
            utils.resaltar(post[2])

        print(utils.colorear("\n1. Primer post  2. Anterior  3. Siguiente  4. Último post  5. Salir", 2))
        nav = input(utils.colorear("\nOpción: ", 2))

        if nav == "1":
            utils.limpiar()
            indice = 0
        elif nav == "2":
            utils.limpiar()
            indice = max(indice - 1, 0)
        elif nav == "3":
            utils.limpiar()
            indice = min(indice + 1, len(posts) - 1)
        elif nav == "4":
            utils.limpiar()
            indice = len(posts) - 1
        elif nav == "5":
            break
        else:
            utils.invalido()

    input("\nPresione Enter para volver al menú...")