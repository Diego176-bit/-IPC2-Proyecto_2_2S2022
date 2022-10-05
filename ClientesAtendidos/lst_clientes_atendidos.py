class LstClientesAtendidos:
    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None
    
    def es_vacio(self):
        return self.primero == None
    
    def agregar(self, cliente):
        
        if self.es_vacio():
            self.primero = self.ultimo = cliente             #si no hay ningún nodo en la lista se agrega a ultimo y primero
        else:                                                   #Si ya hay nodos 
            aux_cliente = self.ultimo 
            self.ultimo = aux_cliente.siguiente = cliente
    
    def conteo_clientes(self) -> int:
        """ Cuenta cuantos clientes han sido atendidos por el escritorio """
        aux = self.primero
        conteo_clientes = 0
        while aux != None:
            conteo_clientes += 1
            aux = aux.siguiente
        return conteo_clientes

    def promedio_atencion(self) -> int:
        """ Retorna el promedio de atencion del escritorio """
        aux = self.primero
        suma_atencion = 0
        
        while aux != None:
            suma_atencion += aux.tiempo_transaccion
            aux = aux.siguiente
        return (suma_atencion/self.conteo_clientes())
    
    def tiemp_max_transaccion(self) -> int:
        aux = self.primero
        tiempo_max = 0
        while aux != None:
            if aux.tiempo_transaccion > tiempo_max:
                tiempo_max = aux.tiempo_transaccion
            aux = aux.siguiente
        return tiempo_max
    
    def tiemp_min_transaccion(self) -> int:
        aux = self.primero
        tiempo_min = 0
        while aux != None:
            if aux.tiempo_transaccion < tiempo_min:
                tiempo_min = aux.tiempo_transaccion
            aux = aux.siguiente
        return tiempo_min
    
    def imprimir(self):
        print(f'tiempo Promedio atencion{self.promedio_atencion()}')