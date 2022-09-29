
class NodoTransacciones:
    def __init__(self, id_transaccion, nombre_transaccion, tiempo) -> None:
        self.id_transaccion = id_transaccion
        self.nombre_transaccion = nombre_transaccion
        self.tiempo = tiempo
        self.siguiente = None