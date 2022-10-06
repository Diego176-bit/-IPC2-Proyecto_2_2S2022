import os

class LstClientesAtendidos:
    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None
    
    def es_vacio(self):
        return self.primero == None
    
    def agregar(self, cliente):
        cliente.siguiente = None
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
    
    def graficar(self,  id_escritorio):
        """ nodo_empresa = self.lst_empresa.buscar_empresa(id_empresa)
        nodo_punto_atencion = nodo_empresa.lst_punto_atencion.buscar_punto_atencion(id_punto_atencion) """
        aux = self.primero
        contador = 0
        archivo = open(f'escritorio_{id_escritorio}.dot', 'w')
        cadena = '''
            digraph G {
            rankdir="LR"
            subgraph cluster_0 {
            style=filled;
            fontsize=42;
            color= lightgray;
            node [style=filled,fontsize=32,color=skyblue, shape= box,width=2.5,height = 2.5];
            
            
        '''
        cadena = cadena + f'label = "Id Escritrorio: {id_escritorio} \n Tiempo Promedio: {self.promedio_atencion()} \n Tiempo min: {self.tiemp_min_transaccion()} \n Tiempo max: {self.tiemp_max_transaccion()}";'
        while aux != None:
            
            cadena = cadena + f' a{contador}[label = "{aux.nombre_cliente}  tiempo total: {aux.tiempo_total}", style=filled,fontsize=32,color=white, shape= box]\n'
            contador +=1
            aux = aux.siguiente
        
        
        while contador >= 0:
            cadena = cadena + f'a{contador} -> a{contador -1}->'
            contador -=2
            if contador <= 0:
                contador = 0
                cadena = cadena + f' a{contador}'
                break
        cadena = cadena + '\n } \n }'
        
        archivo.write(cadena)
        archivo.close()
        os.system(f'dot -Tpng escritorio_{id_escritorio}.dot -o escritorio_{id_escritorio}.png')
    
    def imprimir(self):
        aux = self.primero
        while aux != None:
            print('nombre_cliente', aux.nombre_cliente)
            aux = aux.siguiente