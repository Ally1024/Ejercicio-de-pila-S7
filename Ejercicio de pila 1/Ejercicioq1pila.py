import Modulopila1  # Importa el modulo con la clase

# Menu para el usuario
def mostrar_menu():
    print("\n=== MENÚ DE DOCUMENTOS ===")
    print("1. Agregar documento")
    print("2. Eliminar último documento")
    print("3. Mostrar documentos pendientes")
    print("4. Salir")

# Funcion principal
def main():
    pila = Modulopila1.PilaDocumentos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción del documento: ")
            mensaje = pila.agregar_documento(descripcion)
            print(mensaje)

        elif opcion == "2":
            mensaje = pila.eliminar_ultimo_documento()
            print(mensaje)

        elif opcion == "3":
            mensaje = pila.mostrar_pendientes()
            print(mensaje)

        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
