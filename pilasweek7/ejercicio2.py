""" Ejercicio 2 de la guia didactica sobr pilas:
Un sistema Sobre una panaderia la cual se agregan panes, se venden(eliminan) y muestra los 
panes listos para vender
grupo: Andres Porras,Genesis Ramos y Allysson palma 
6/11/2025"""

from modulos2 import Pila

import os # es un modulo para limpiar pantallita

bandeja = Pila()
# menu que interactua con el usuario
def mostrar_menu():
    print("\n=== Panadería de León ===")
    print("1. Agregar pan a la bandeja")
    print("2. Vender pan")
    print("3. Ver pan listo para vender")
    print("4. Mostrar todos los panes en la bandeja")
    print("5. Salir")
 
# Función para agregar un pan a la pila (push)
def agregar_pan():
    print("\n** Agregar Pan **")
    pan = input("Ingrese el tipo de pan: ").strip()
    if pan:
        bandeja.push(pan)
        print(f"Se agregó '{pan}' a la bandeja.")
    else:
        print("No se ingresó ningún pan.")
    input("\nPresione una tecla para continuar...")
    os.system('cls')

# Función para vender el pan del tope (pop)
def vender_pan():
    print("\n** Vender Pan **")
    pan = bandeja.pop() # Quitamos el pan de la cima
    if pan:
        print(f"Se vendió el pan: {pan}")
    input("\nPresione una tecla para continuar...")
    os.system('cls') 

# Función para ver el pan que está en la cima (peek)
def ver_pan_tope():
    print("\n** Pan listo para vender **")
    pan = bandeja.peek()
    if pan:
        print(f"El pan listo para vender es: {pan}")
    input("\nPresione una tecla para continuar...")
    os.system('cls')  


def mostrar_bandeja():
    print("\n** Bandeja actual **")
    bandeja.mostrar() # Recorremos e imprimimos todos los panes desde la cima hacia abajo
    input("\nPresione una tecla para continuar...")
    os.system('cls') 

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("\nSeleccione una opción (1-5): ").strip()

    if opcion == "1":
        agregar_pan()
    elif opcion == "2":
        vender_pan()
    elif opcion == "3":
        ver_pan_tope()
    elif opcion == "4":
        mostrar_bandeja()
    elif opcion == "5":
        print("\n¡Gracias por usar el sistema de la panadería!")
        break
    else:
        print("Opción no válida. Por favor ingrese un número del 1 al 5.")



