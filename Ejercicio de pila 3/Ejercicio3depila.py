import ModuloEjercicio3pila  # Llama al módulo que contiene la clase PilaDonantes

# Función para mostrar el menú
def mostrar_menu(): 
    print("\n==== MENÚ DE DONANTES ====")
    print("1. Registrar donante")
    print("2. Eliminar último donante")
    print("3. Mostrar donante actual")
    print("4. Salir\n")

# Función para validar el teléfono (debe tener exactamente 8 dígitos)
def validar_telefono(telefono):
    if len(telefono) == 8 and telefono.isdigit():
        return True
    else:
        return False

# Función para validar si la edad es mayor de edad
def validar_edad(edad):
    try:
        edad = int(edad)
        if edad >= 18:
            return True, "Mayor de edad"
        elif edad<=18:
              return False, "Menor de edad"
    except ValueError:
          return False, "Edad inválida"

# Función principal
def main():
    pila = ModuloEjercicio3pila.PilaDonantes()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del donante: ")

            # Validar edad
            edad = input("Ingrese la edad del donante: ")
            es_mayor, mensaje_edad = validar_edad(edad)
            if not es_mayor:
                print(f"Error: {mensaje_edad}. Solo se permiten mayores de edad.")
                continue  # Si no es mayor de edad, salta al siguiente ciclo

            # Validar teléfono
            telefono = input("Ingrese el teléfono del donante (8 dígitos): ")
            if not validar_telefono(telefono):
                print("Error: El teléfono debe tener exactamente 8 dígitos.")
                continue  # Si el teléfono no es válido, salta al siguiente ciclo

            # Registrar donante
            mensaje = pila.registrar_donante(nombre, edad, telefono)
            print(mensaje)

        elif opcion == "2":
            mensaje = pila.eliminar_ultimo_donante()
            print(mensaje)

        elif opcion == "3":
            mensaje = pila.mostrar_donante_actual()
            print(mensaje)

        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

# Llamada a la función main para iniciar el programa
if __name__ == "__main__":
    main()
