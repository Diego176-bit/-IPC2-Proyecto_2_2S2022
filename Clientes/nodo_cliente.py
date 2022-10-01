from TransaccionesClientes.lst_transacciones_clientes import LstTransaccionesClientes
class NodoCliente:
    def __init__(self, dpi, nombre_cliente) -> None:
        self.dpi = dpi
        self.nombre_cliente = nombre_cliente
        self.tiempo_total = 0
        self.tiempo_en_cola = 0
        self.tiempo_transaccion = 0
        self.atendido = False
        self.lst_transacciones = LstTransaccionesClientes()
        self.siguiente = None
    
    