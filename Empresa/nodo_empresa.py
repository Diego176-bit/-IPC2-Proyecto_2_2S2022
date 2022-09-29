import sys
sys.path.insert(0, './')
from PuntosAtencion.lst_punto_atencion import LstPuntoAtencion
from Transacciones.lst_transacciones import LstTransacciones
class NodoEmpresa:
    def __init__(self, id_empresa, nombre_empresa, abreviatura_empresa) -> None:
        self.id_empresa = id_empresa
        self.nombre_empresa = nombre_empresa
        self.abreviatura_empresa = abreviatura_empresa
        self.lst_punto_atencion = LstPuntoAtencion()
        self.lst_transacciones = LstTransacciones()
        self.siguiente = None
        
 
    
        