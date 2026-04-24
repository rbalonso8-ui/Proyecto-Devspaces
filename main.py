"""
Módulo principal del sistema DevSpaces

Autor: Alonso Rodríguez Bolaños
Fecha: 24/06/2026
"""
import ui
import utils

#! ======================
#!     MENU INICIAL
#! ======================

def menu_principal():
    """Establece el menú principal del sistema.

    Returns:
        None
    """
    utils.limpiar()
    while True:
        opcion = ui.ingresar_terminal()

        if opcion == "1":
            resultado = ui.login_terminal()
            if resultado:
                nombre_usuario, user_id = resultado[1], resultado[2]
                menu_sistema(nombre_usuario, user_id)
            else:
                input("\npresiona enter para volver al menu principal ")
        elif opcion == "2":
            utils.limpiar()
            print("Gracias por usar DevSpace. ¡Hasta luego!")
            utils.limpiar()
            utils.esperar(2)
            break
        else:
            utils.invalido

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
        opcion = ui.menu_interno(nombre_usuario)
        if opcion == "1":
            ui.lista_usuarios_terminal()
        elif opcion == "2":
            ui.lista_spaces_terminal()
        elif opcion == "3":
            ui.seguir_space_terminal(nombre_usuario)
        elif opcion == "4":
            ui.mostrar_spaces_seguidos(nombre_usuario)
        elif opcion == "5":
            ui.mostrar_seguidores(nombre_usuario)
        elif opcion == "6":
            ui.gestionar_seguidores(nombre_usuario)
        elif opcion == "7":
            ui.mostrar_posts(nombre_usuario)
        elif opcion == "8":
            utils.limpiar()
            print(f"Cerrando sesión. ¡Hasta luego, {nombre_usuario}!")
            utils.esperar(2)
            utils.limpiar()
            break
        else:
            utils.limpiar()
            print("Opción no válida. Por favor, seleccione una opción válida.")
            utils.esperar(2)
            
menu_principal()