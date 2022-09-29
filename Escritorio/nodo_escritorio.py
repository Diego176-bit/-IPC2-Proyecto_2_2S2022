
"""Nodo de Escritorio"""
class NodoEscritorio:
    def __init__(self, id_escritorio,identificador, encargado) -> None:
        self.id_escritorio = id_escritorio
        self.identificador = identificador
        self.encargado = encargado
        self.esta_activo = False
        self.siguiente= None