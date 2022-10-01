from Escritorio.lst_escritorio import LstEscritorio
from Clientes.lst_clientes import LstClientes
class NodoPuntoAtencion:
    def __init__(self, id_punto_atencion, nombre_punto_atencion, direccion_punto_atencion) -> None:
        self.id_punto_atencion = id_punto_atencion
        self.nombre_punto_atencion = nombre_punto_atencion
        self.direccion_punto_atencion = direccion_punto_atencion
        self.tiempo_promedio_espera = 0
        self.tiempo_max_espera = 0
        self.tiempo_min_espera = 0
        self.tiempo_promedio_atencion = 0
        self.tiempo_max_atencion = 0
        self.tiempo_min_atencion = 0 
        self.lst_escritorio = LstEscritorio()
        self.lst_clientes = LstClientes()
        self.siguiente = None
    
    