from PuntosAtencion.nodo_punto_atencion import NodoPuntoAtencion

class LstPuntoAtencion:
    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None
    
    def es_vacio(self):
        return self.primero == None
    
    def agregar(self, id_punto_atencion, nombre_punto_atencion, direccion_punto_atencion):
        """agregar NodoPuntoAtencion"""
        punto_atencion = NodoPuntoAtencion(id_punto_atencion, nombre_punto_atencion, direccion_punto_atencion)   #instancia del objeto
        
        if self.es_vacio():
            self.primero = self.ultimo = punto_atencion             #si no hay ningún nodo en la lista se agrega a ultimo y primero
        else:                                                   #Si ya hay nodos 
            aux_punto_atencion = self.ultimo 
            self.ultimo = aux_punto_atencion.siguiente = punto_atencion
    
    def buscar_punto_atencion(self, id_punto_atencion):
        aux_punto_atencion = self.primero
        while aux_punto_atencion != None:
            if aux_punto_atencion.id_punto_atencion == id_punto_atencion:
                return aux_punto_atencion
            aux_punto_atencion = aux_punto_atencion.siguiente
        return None

    def recorrer(self):
       aux = self.primero
       
       while aux != None:
           print(aux.id_punto_atencion)
           print(aux.nombre_punto_atencion)
           print(aux.direccion_punto_atencion)
           print('-------------------escritorio---------------')
           aux.lst_escritorio.recorrer()
           aux = aux.siguiente