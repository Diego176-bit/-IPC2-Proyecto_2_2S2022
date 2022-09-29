from Escritorio.lst_escritorio import LstEscritorio

class NodoPuntoAtencion:
    def __init__(self, id_punto_atencion, nombre_punto_atencion, direccion_punto_atencion) -> None:
        self.id_punto_atencion = id_punto_atencion
        self.nombre_punto_atencion = nombre_punto_atencion
        self.direccion_punto_atencion = direccion_punto_atencion
        self.lst_escritorio = LstEscritorio()
        self.siguiente = None
    
    