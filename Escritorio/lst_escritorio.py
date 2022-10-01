from Escritorio.nodo_escritorio import NodoEscritorio

class LstEscritorio:
    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None
    
    def es_vacio(self):
        return self.primero == None
    
    def agregar(self, id_escritorio, identificador, encargado):
        """agregar NodoEscritorio"""
        escritorio = NodoEscritorio(id_escritorio,identificador, encargado)   #instancia del objeto
        
        if self.es_vacio():
            self.primero = self.ultimo = escritorio             #si no hay ningún nodo en la lista se agrega a ultimo y primero
        else:                                                   #Si ya hay nodos 
            aux_escritorio = self.ultimo 
            self.ultimo = aux_escritorio.siguiente = escritorio
    
    def buscar_escritorio(self, id_escritorio):
        aux_escritorio = self.primero
        while aux_escritorio != None:
            if aux_escritorio.id_escritorio == id_escritorio:
                return aux_escritorio
            aux_escritorio = aux_escritorio.siguiente
        return None
    
    def recorrer(self):
       aux = self.primero
       
       while aux != None:
           print(aux.id_escritorio)
           print(aux.identificador)
           print(aux.encargado)
           print('----------------------')
           print('')
           print('')
           aux = aux.siguiente
    
    def escritorios_activos(self):
        aux = self.primero
        cantidad_escritorios_activos = 0
        while aux != None:
            if aux.esta_activo == True:
                cantidad_escritorios_activos +=1
            aux = aux.siguiente
        return cantidad_escritorios_activos

    def escritorios_desactivados(self):
        aux = self.primero
        cantidad_escritorios_desactivados = 0
        while aux != None:
            if aux.esta_activo == False:
                cantidad_escritorios_desactivados +=1
            aux = aux.siguiente
        return cantidad_escritorios_desactivados