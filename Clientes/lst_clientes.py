from Clientes.nodo_cliente import NodoCliente
class LstClientes: 
    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None
    
    def es_vacio(self):
        return self.primero == None

    def agregar_cliente(self, dpi, nombre_cliente):
        """agregar NodoCliente"""
        cliente = NodoCliente(dpi,nombre_cliente)   #instancia del objeto
        
        if self.es_vacio():
            self.primero = self.ultimo = cliente             #si no hay ningún nodo en la lista se agrega a ultimo y primero
        else:                                                   #Si ya hay nodos 
            aux_cliente = self.ultimo 
            self.ultimo = aux_cliente.siguiente = cliente
    
    def buscar_cliente(self, dpi):
        aux_cliente = self.primero
        while aux_cliente != None:
            if aux_cliente.dpi == dpi:
                return aux_cliente
            aux_cliente = aux_cliente.siguiente
        return None