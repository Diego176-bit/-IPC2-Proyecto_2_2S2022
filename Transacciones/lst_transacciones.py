from Transacciones.nodo_transacciones import NodoTransacciones

class LstTransacciones:
    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None
    
    
    def agregar(self, id_transaccion, identificador, encargado):
        """agregar NodoEscritorio"""
        transaccion = NodoTransacciones(id_transaccion,identificador, encargado)   #instancia del objeto
        
        if self.es_vacio():
            self.primero = self.ultimo = transaccion             #si no hay ningún nodo en la lista se agrega a ultimo y primero
        else:                                                   #Si ya hay nodos 
            aux_transaccion = self.ultimo 
            self.ultimo = aux_transaccion.siguiente = transaccion