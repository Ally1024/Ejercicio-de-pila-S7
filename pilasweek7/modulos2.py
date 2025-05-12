""" Ejercicio 2 de la guia didactica sobr pilas:
Un sistema Sobre una panaderia la cual se agregan panes, se venden(eliminan) y muestra los 
panes listos para vender
grupo: Andres Porras,Genesis Ramos y Allysson palma
lo realice implementando listas enlazadas  
6/11/2025"""

class Nodo:
    def __init__ (self, pan ):
       self.pan = pan  
       self.siguiente = None
        
class Pila :
    def __init__ (self):
        self.cima = None 

#agregar pan a la bandeja con el push 
    def push(self, pan) : 
        nuevo = Nodo(pan)
        nuevo.siguiente = self.cima 
        self.cima = nuevo 


#eliminar pan de la bandeja con el pop 
    def pop (self):
        if self.cima is None:
            print("No hay panes en la bandeja")
            return None 
        eliminado = self.cima.pan
        self.cima = self.cima.siguiente 
        return eliminado 
    #metodo para mostrar el pna listo para vender 
    def peek (self ):
        if self.cima is None :
            print("No hay panes en la bandeja")
            return None 
        
        return self.cima.pan
    
    #metodo para mostrar todos los panes preparados y listitos para vender
    def mostrar (self):
        if self.cima is None :
            print("No hay panes en la bandeja")
            return None 
        else : 
            actual = self.cima 
            while actual is not None :
                print(actual.pan)
                actual = actual.siguiente 




    



