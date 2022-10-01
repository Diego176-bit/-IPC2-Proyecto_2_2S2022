from Transacciones.nodo_transacciones import NodoTransacciones

class LstTransacciones:
    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None
    
    def es_vacio(self):
        return self.primero == None
    
    def agregar_transaccion(self, id_transaccion, nombre_transaccion, tiempo):
        """agregar NodoEscritorio"""
        transaccion = NodoTransacciones(id_transaccion,nombre_transaccion, tiempo)   #instancia del objeto
        
        if self.es_vacio():
            self.primero = self.ultimo = transaccion             #si no hay ningún nodo en la lista se agrega a ultimo y primero
        else:                                                   #Si ya hay nodos 
            aux_transaccion = self.ultimo 
            self.ultimo = aux_transaccion.siguiente = transaccion
        
    def recorrer(self):
       aux = self.primero
       
       while aux != None:
           print(aux.id_transaccion)
           print(aux.nombre_transaccion)
           print(aux.tiempo)
           aux = aux.siguiente
           
    def buscar_transaccion(self, id_transaccion):
        aux = self.primero
        while aux != None:
            if aux.id_transaccion == id_transaccion:
                return aux
            aux = aux.siguiente
        return None