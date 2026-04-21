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
        print("Ingreso exitoso. Bienvenido, {}.".format(nombre_usuario))
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
        print("Seleccione una opción:")
        print("1. Ingresar al sistema")
        print("2. Salir")

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
        print("8. Cerrar sesión")
        respuesta = input("Seleccione una opción: ")  
        
        if respuesta == "1":
            pass
        elif respuesta == "2":
            pass
        elif respuesta == "3":
            pass
        elif respuesta == "4":  
            pass
        elif respuesta == "5":
            pass
        elif respuesta == "6":
            pass
        elif respuesta == "7":
            pass
        elif respuesta == "8":
            print("\033c", end="")
            print("Cerrando sesión. ¡Hasta luego, {}!".format(nombre_usuario))
            time.sleep(2)
            print("\033c", end="")
            break
        else:
            print("\033c", end="")
            print("Opción no válida. Por favor, seleccione una opción válida.")
            time.sleep(2)