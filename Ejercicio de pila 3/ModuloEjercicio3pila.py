"""
Buenos días profe, somos Allysson Palma, Nicole Ramsos y Andrés Porras.
Ejercicio 3.
09/05/2025
En una campaña de donación de sangre en un hospital de Estelí, los datos de los donantes se
almacenan en una pila según el orden en que se procesan. Si ocurre un problema técnico, se debe
revertir el último registro. Implementa un sistema para registrar donantes (push), eliminar el último
(pop), y mostrar el donante actual en proceso.
"""

# Creación de pila para almacenar los donantes 
class PilaDonantes:
    def __init__(self):
        self.pila = []

    # Método para registrar un donante
    def registrar_donante(self, nombre, edad, telefono):
        donante = {
            "nombre": nombre,
            "edad": edad,
            "telefono": telefono
        }
        self.pila.append(donante)
        return f"Donante '{nombre}' registrado correctamente."

    # Método para eliminar el último donante
    def eliminar_ultimo_donante(self):
        if self.pila:
            eliminado = self.pila.pop()
            return f"Se eliminó el último donante registrado: {eliminado['nombre']}"
        else:
            return "No hay donantes para eliminar."

    # Método para mostrar el donante actual en proceso
    def mostrar_donante_actual(self):
        if self.pila:
            actual = self.pila[-1]
            return f"Donante actual en proceso:\nNombre: {actual['nombre']}, Edad: {actual['edad']}, Teléfono: {actual['telefono']}"
        else:
            return "No hay donantes registrados."
