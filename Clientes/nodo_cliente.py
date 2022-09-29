from TransaccionesClientes.lst_transacciones_clientes import LstTransaccionesClientes
class NodoCliente:
    def __init__(self, dpi, nombre_cliente) -> None:
        self.dpi = dpi
        self.nombre_cliente = nombre_cliente
        self.tiempo = 0
        self.lst_transacciones = LstTransaccionesClientes()
        self.siguiente = None
    
    