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
        cliente.siguiente = None 
        if self.es_vacio():
            self.primero = cliente
            self.ultimo = cliente             #si no hay ningún nodo en la lista se agrega a ultimo y primero
        else:                                                   #Si ya hay nodos 
            self.ultimo.siguiente = cliente
            self.ultimo = cliente
    
    def atender(self):
        if self.es_vacio() == False:
            aux = self.primero
            if self.primero == self.ultimo:
                self.primero = None
                self.ultimo = None
            
            else:
                aux_cliente_dos = self.primero.siguiente
                
                #Actualizar tiempos en cola 
                while aux_cliente_dos != None:
                    aux_cliente_dos.tiempo_en_cola -= aux.tiempo_total
                    aux_cliente_dos = aux_cliente_dos.siguiente
                    
                self.primero = self.primero.siguiente
            return (aux)


    def buscar_cliente(self, dpi):
        aux_cliente = self.primero
        while aux_cliente != None:
            if aux_cliente.dpi == dpi:
                return aux_cliente
            aux_cliente = aux_cliente.siguiente
        return None
    
    def clientes_en_espera(self):
        aux_cliente = self.primero
        contador_clientes_en_espera = 0
        while aux_cliente != None:
            if aux_cliente.atendido == False:
                contador_clientes_en_espera += 1
            aux_cliente = aux_cliente.siguiente
        return contador_clientes_en_espera

    
    
    def tiempo_cola(self, dpi):
        aux_cliente = self.primero
        tiempo_cola = 0
        while aux_cliente != None:
            if aux_cliente == self.primero and aux_cliente.dpi == dpi:
                return 0
            if aux_cliente.dpi == dpi:
                return int(tiempo_cola)
            tiempo_cola += aux_cliente.tiempo_total
            aux_cliente = aux_cliente.siguiente
            
    """ TIEMPOS ESPERA """
    def tiempo_promedio_espera(self):
        aux_cliente = self.primero
        tiempo_promedio_espera = 0
        clientes = 0
        while aux_cliente != None:
            
            clientes += 1
            tiempo_promedio_espera += aux_cliente.tiempo_total
            aux_cliente = aux_cliente.siguiente
        return float(tiempo_promedio_espera/clientes)

    def tiempo_max_espera(self):
        aux_cliente = self.primero
        tiempo_max_espera = 0
        while aux_cliente != None:
            if aux_cliente.tiempo_en_cola > tiempo_max_espera:
                tiempo_max_espera = aux_cliente.tiempo_en_cola
                aux_cliente = aux_cliente.siguiente
            else: 
                aux_cliente = aux_cliente.siguiente
        return float(tiempo_max_espera)
    
    def tiempo_min_espera(self):
        aux_cliente = self.primero
        tiempo_min_espera = 0
        while aux_cliente != None:
            if aux_cliente.tiempo_en_cola < tiempo_min_espera:
                tiempo_min_espera = aux_cliente.tiempo_en_cola
                aux_cliente = aux_cliente.siguiente
            else: aux_cliente = aux_cliente.siguiente
        
        return float(tiempo_min_espera)
    
    """ TIEMPOS ATENCION """
    
    def tiempo_promedio_atencion(self):
        aux_cliente = self.primero
        tiempo_promedio_atencion = 0
        clientes= 0
        while aux_cliente != None:
            clientes += 1
            tiempo_promedio_atencion += aux_cliente.tiempo_transaccion
            aux_cliente = aux_cliente.siguiente
        return float(tiempo_promedio_atencion/clientes)
    
    def tiempo_max_atencion(self):
        aux_cliente = self.primero
        tiempo_max_atencion = 0
        while aux_cliente != None:
            if aux_cliente.tiempo_transaccion > tiempo_max_atencion:
                tiempo_max_atencion = aux_cliente.tiempo_transaccion
                aux_cliente = aux_cliente.siguiente
            else: aux_cliente = aux_cliente.siguiente
        return float(tiempo_max_atencion)
    
    def tiempo_min_atencion(self):
        aux_cliente = self.primero
        tiempo_min_atencion = 0
        while aux_cliente != None:
            if aux_cliente.tiempo_transaccion < tiempo_min_atencion:
                tiempo_min_atencion = aux_cliente.tiempo_transaccion
                aux_cliente = aux_cliente.siguiente
            else: aux_cliente = aux_cliente.siguiente
        return float(tiempo_min_atencion)
            
        
    
    #de momento
    def tiempo_total(self):
        aux = self.primero
        while aux != None:
            print('tiempo espera => ', aux.tiempo_en_cola)
            print('tiempo total =>',aux.tiempo_total)
            
            #print('tiempo max cola =>', aux.tiempo_max_cola)
            aux = aux.siguiente
    
    def listar(self):
        aux = self.primero
        while aux != None:
            print('nombre_cliente => ', aux.nombre_cliente)
            aux = aux.siguiente