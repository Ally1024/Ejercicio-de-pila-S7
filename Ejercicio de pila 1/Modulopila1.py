"""
Buenos días profe, somos Nicole Ramos, Allysson Palma y Andres Porras

este es el ejercicio sobre el uso de pilas correspondiente a la oficina de atención ciudadana en una alcaldía municipal.
En este ejercicio se simula la revisión de documentos, donde cada solicitud se apila en el orden en que llega.
Se permite agregar documentos, eliminar el último revisado y mostrar los documentos pendientes.
"""

# Clase para manejar la pila de documentos.
class PilaDocumentos:
    def __init__(self):
        self.pila = []

    # Metodo para agregar un nuevo documento
    def agregar_documento(self, descripcion):
        self.pila.append(descripcion)
        return f"Documento agregado: '{descripcion}'"

    # Metodo para eliminar el último documento agregado
    def eliminar_ultimo_documento(self):
        if self.pila:
            documento = self.pila.pop()
            return f"Documento eliminado: '{documento}'"
        else:
            return "No hay documentos para eliminar."

    # Metodo para mostrar los documentos pendientes
    def mostrar_pendientes(self):
        if self.pila:
            pendientes = "\n".join(f"- {doc}" for doc in reversed(self.pila))
            return f"Documentos pendientes:\n{pendientes}"
        else:
            return "No hay documentos pendientes."
