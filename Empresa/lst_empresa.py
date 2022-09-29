

from Empresa.nodo_empresa import NodoEmpresa

class LstEmpresa:
    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None

    def es_vacio(self):
        return self.primero == None
    
    def agregar(self, id_empresa, nombre_empresa, abreviatura_empresa):
        """agregar Modo Empresa"""
        empresa = NodoEmpresa(id_empresa, nombre_empresa, abreviatura_empresa)   #instancia del objeto
        
        if self.es_vacio():
            self.primero = self.ultimo = empresa             #si no hay ningún nodo en la lista se agrega a ultimo y primero
        else:                                                   #Si ya hay nodos 
            aux_empresa = self.ultimo 
            self.ultimo = aux_empresa.siguiente = empresa
    
    def buscar_empresa(self, id_empresa):
        aux_empresa = self.primero
        while aux_empresa != None:
            if aux_empresa.id_empresa == id_empresa:
                return aux_empresa
            aux_empresa = aux_empresa.siguiente
        return None
    def recorrer(self):
       aux = self.primero
       
       while aux != None:
           print(aux.id_empresa)
           print(aux.nombre_empresa)
           print(aux.abreviatura_empresa)
           print('----------------------Puntos atencion------------------')
           aux.lst_punto_atencion.recorrer()
           aux = aux.siguiente