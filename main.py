"""
Módulo principal del sistema DevSpaces

Autor: Alonso Rodríguez Bolaños
Fecha: 24/06/2026
"""
import sys
import ui
import utils
import controller
sys.path.append('./API')

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
            nombre_usuario, contraseña = ui.login_terminal()
            resultado = controller.login(nombre_usuario, contraseña)

            if resultado:
                nombre_usuario, user_id = resultado
                print(f"\nIngreso exitoso. Bienvenido, {nombre_usuario}.")
                utils.esperar(2)
                menu_sistema(nombre_usuario, user_id)
            else:
                print("\nCredenciales incorrectas. Intente nuevamente.")
                utils.esperar(2)

        elif opcion == "2":
            utils.limpiar()
            print("Gracias por usar DevSpace. ¡Hasta luego!")
            utils.esperar(2)
            utils.limpiar()
            break

        else:
            utils.limpiar()
            print("Opción no válida.")
            utils.esperar(2)

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


if False:
    success, data = ds.create_user("alonso", "rbalonso8@gmail.com", "12345")
    print(success, data)
    success, data = ds.create_user("carlos", "carlos@gmail.com", "12345")
    print(success, data)
    success, data = ds.create_post(36, "pares", "def es_par(n):\n    if n % 2 == 0:\n        print('par')\n    else:\n        print('impar')", "snippet")
    print(success, data)

menu_principal()