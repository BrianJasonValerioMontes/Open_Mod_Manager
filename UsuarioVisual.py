import os
import hashlib

# Base de datos simple (en memoria)
usuarios = {}

# Función para encriptar contraseñas
def encriptar_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función de registro
def registrarse():
    limpiar_pantalla()
    print("=== Registro de Usuario ===")
    usuario = input("Ingrese un nombre de usuario: ")
    if usuario in usuarios:
        print("El nombre de usuario ya existe. Intente con otro.")
        input("Presione Enter para continuar...")
        return
    contraseña = input("Ingrese una contraseña: ")
    usuarios[usuario] = encriptar_contraseña(contraseña)
    print("Registro exitoso.")
    input("Presione Enter para continuar...")

# Función de inicio de sesión
def iniciar_sesion():
    limpiar_pantalla()
    print("=== Inicio de Sesión ===")
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuario in usuarios and usuarios[usuario] == encriptar_contraseña(contraseña):
        print("Inicio de sesión exitoso. Bienvenido,", usuario)
    else:
        print("Usuario o contraseña incorrectos.")
    input("Presione Enter para continuar...")

# Menú principal
def menu():
    while True:
        limpiar_pantalla()
        print("=== Menú Principal ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrarse()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida, intente de nuevo.")
            input("Presione Enter para continuar...")

# Iniciar el programa
menu()
