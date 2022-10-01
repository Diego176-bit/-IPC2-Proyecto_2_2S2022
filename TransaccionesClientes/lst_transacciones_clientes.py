from TransaccionesClientes.nodo_transaccion_cliente import NodoTransaccionCliente

class LstTransaccionesClientes:
    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None
    
    
    def es_vacio(self):
        return self.primero == None

    def agregar_transaccion_cliente(self, dpi, nombre_transaccion_cliente):
        """agregar Nodotransaccion_cliente"""
        transaccion_cliente = NodoTransaccionCliente(dpi,nombre_transaccion_cliente)   #instancia del objeto
        
        if self.es_vacio():
            self.primero = self.ultimo = transaccion_cliente             #si no hay ningún nodo en la lista se agrega a ultimo y primero
        else:                                                   #Si ya hay nodos 
            aux_transaccion_cliente = self.ultimo 
            self.ultimo = aux_transaccion_cliente.siguiente = transaccion_cliente
    
    