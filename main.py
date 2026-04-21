"""
Módulo principal del sistema DevSpaces

Autor: Alonso Rodríguez Bolaños
Fecha: 24/06/2026
    """
import sys
sys.path.append('./API')
import devspace as ds
import time

#! ======================
#!     MENU INICIAL
#! ======================

def menu_ingresar_usuario():
    """Establecer el menú de opciones para el ingreso de un usuario existente en el sistema de DevSpace.

    Returns:
        tuple: (nombre_usuario, user_id) si el ingreso es exitoso, False si falla.
    """
    print("\033c", end="")
    print("Ingresar al sistema\n")

    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    resultado = ds.login(nombre_usuario, contrasena) 

    if resultado[0] == True:  
        user_id = resultado[1] 
        print(f"\nIngreso exitoso. Bienvenido, {nombre_usuario}.")
        time.sleep(2)
        return nombre_usuario, user_id
    else:
        print("Error al ingresar. Por favor, verifique su nombre de usuario y contraseña e intente nuevamente.")
        time.sleep(2)
        return False 
    
#! ======================
#!    MENU PRINCIPAL
#! ======================

def menu_principal():
    """Establecer el menú de opciones principales del sistema en terminal.

    Returns:
        None
    """
    while True:
        print("\033c", end="") 
        print("Bienvenido al sistema de DevSpace\n")
        print("Seleccione una opción: \n")
        print("1. Ingresar al sistema")
        print("2. Salir \n")

        respuesta_usuario = input("Ingrese el número de la opción deseada: ")

        if respuesta_usuario == "1":
            resultado = menu_ingresar_usuario()
            if resultado:
                nombre_usuario, user_id = resultado  
                print("\033c", end="")
                menu_sistema(nombre_usuario, user_id)
                
            else:
                print("\033c", end="")
                print("Usuario no válido. Por favor, intente nuevamente.")
                time.sleep(2)

        elif respuesta_usuario == "2":
            print("\033c", end="")
            print("Gracias por usar DevSpace. ¡Hasta luego!")
            time.sleep(2)
            print("\033c", end="")
            break 

        else:
            print("\033c", end="")
            print("Opción no válida. Por favor, seleccione una opción válida.")
            time.sleep(2)  
            
#! ======================
#!    MENU INTERNO
#! ======================
            
def menu_sistema(nombre_usuario, user_id):
    """Menú principal interno del sistema DevSpace, al que se accede después de un login exitoso.
    
    Args:        
        nombre_usuario (str): El nombre de usuario del usuario que ha iniciado sesión.
        user_id (int): El ID del usuario que ha iniciado sesión.

    Returns:
        None
    """
    while True:
        print("\033c", end="")
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
        
        #? ======================
        #?  Consulta de Usuarios
        #? ======================
        
        if respuesta == "1":
            print("\033c", end="")
            print("Lista de usuarios:\n")
            success, data = ds.get_users()
    
            if success:
                for usuario in data:
                    print(f"ID: {usuario[0]} | Usuario: {usuario[1]}")
            else:
                print("No se pudo obtener la lista de usuarios.")
            input("\nPresione Enter para volver al menú...")
            
        #? ======================
        #?  Consulta de Spaces
        #? ======================
            
        elif respuesta == "2":
            print("\033c", end="")
            print("Lista de spaces:\n")
    
            success, usuarios = ds.get_users()
            if success:
                for user in usuarios:
                    success_s, spaces = ds.get_spaces_by_user(user[0])
                    if success_s:
                        for space in spaces:
                            print(f"ID: {space[0]} | Space: {space[1]} | Usuario: {user[0]}")

            input("\nPresione Enter para volver al menú...")      
            
        #? ======================
        #?   Seguir un Spaces
        #? ======================  
        
        elif respuesta == "3":
            print("\033c", end="")
            print("Seguir un space:\n")
    
            success, usuarios = ds.get_users()
            if success:
                for user in usuarios:
                    success_s, spaces = ds.get_spaces_by_user(user[0])
                    if success_s:
                        for space in spaces:
                            print(f"ID: {space[0]} | Space: {space[1]} | Usuario: {user[0]}")
                print("\nSeleccione una opcion del sistema:")
                print("\n1. Seguir un space")
                print("2. Volver al menú principal")
                respuesta = input("\nIngrese el número de la opción deseada: ")
                if respuesta == "1":
                    space_id = input("\nIngrese el ID del space que desea seguir: ")
                    success, message = ds.follow_space(user_id, space_id)
                    if success:
                        print("Space seguido exitosamente.")
                else:
                    print(f"Error al seguir el space: {message}")
                if respuesta == "2":
                    print("\033c", end="")
                    print("Volviendo al menú principal...")
                    time.sleep(2)
                else:
                    print("\033c", end="")
                    print("Opción no válida. Por favor, seleccione una opción válida.")
                    time.sleep(2)
                 
        #? ================================
        #?   Consulta de Spaces seguidos
        #? ================================
        
        elif respuesta == "4":  
            print("\033c", end="")
            print("Spaces que sigues:\n")
    
            success, data = ds.get_following_spaces(nombre_usuario)
    
            if success:
                if len(data) == 0:
                    print("No sigues ningún space.")
                else:
                    for space in data:
                        print(f"ID: {space[0]} | Space: {space[1]} | Usuario: {space[2]}")
            else:
                print("No se pudo obtener la lista.")
    
            input("\nPresione Enter para volver al menú...")
        
        #? =========================================
        #?   Consulta de segudiores de mis spaces
        #? =========================================
        elif respuesta == "5":
            print("\033c", end="")
            print("Seguidores de mis spaces:\n")
    
            success, data = ds.get_followers(nombre_usuario)
    
            if success:
                if len(data) == 0:
                    print("No tienes seguidores pendientes.")
                else:
                    for seguidor in data:
                        print(f"Seguidor: {seguidor[0]} | Space: {seguidor[2]}" )
            else:
                print("No se pudo obtener la lista de seguidores.")
    
            input("\nPresione Enter para volver al menú...")
            
        #? =========================
        #?   Gestionar seguidores
        #? =========================
        
        elif respuesta == "6":
            print("\033c", end="")
            print("Gestionar seguidores:\n")
    
            success, data = ds.get_followers(nombre_usuario)
    
            if success:
                if len(data) == 0:
                    print("No tienes solicitudes de seguidores pendientes.")
                    time.sleep(2)
            else:
                for seguidor in data:
                    print(f"Seguidor: {seguidor[0]} | Space: {seguidor[2]}")
                    print("\nSeleccione una opcion del sistema:")
                    print("\n1. Aceptar seguidor")
                    print("2. Rechazar seguidor")
                    decision = input("\nIngrese el número de la opción deseada: ")
                
                    if decision == "1":
                        success_s, data_s = ds.handle_follower(nombre_usuario, seguidor[1], seguidor[0], True)
                        if success_s:
                            print("Seguidor aceptado.")
                        else:
                            print("No se pudo aceptar.")
                    elif decision == "2":
                        success_s, data_s = ds.handle_follower(nombre_usuario, seguidor[1], seguidor[0], False)
                        if success_s:
                            print("Seguidor rechazado.")
                        else:
                            print("No se pudo rechazar.")
                            time.sleep(1)
                    else:
                        print("Opción no válida. Por favor, seleccione una opción válida.")
                        time.sleep(1)
                else:
                    print("No se pudo obtener la lista de seguidores.")
                    time.sleep(2)
        
        #? ================================
        #?   Consulta de post por space
        #? ================================
        
        elif respuesta == "7":
            pass
        
        #? ==================
        #?   Cerrar sesión
        #? ==================
        
        elif respuesta == "8":
            print("\033c", end="")
            print(f"Cerrando sesión. ¡Hasta luego, {nombre_usuario}!")
            time.sleep(2)
            print("\033c", end="")
            break
        else:
            print("\033c", end="")
            print("Opción no válida. Por favor, seleccione una opción válida.")
            time.sleep(2)
            

if False:
    success, data = ds.create_user("alonso", "rbalonso8@gmail.com", "12345")
    print(success, data)
    
menu_principal()