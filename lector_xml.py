import xml.etree.ElementTree as ET
from Empresa.lst_empresa import LstEmpresa
class CargarArchivo:
    def __init__(self) -> None:
        self.lst_empresa = LstEmpresa()
    
    
    def cargar_archivo(self, path):
        
        try:
            archivo_xml = open(path, 'r')
            if archivo_xml.readable():
                xml_datos = ET.fromstring(archivo_xml.read())
                
                #EMPRESA
                empresas = xml_datos.findall('empresa')
                for empresa in empresas:
                    id_empresa = empresa.attrib['id']
                    
                    nombre_empresa = empresa.find('nombre').text
                    abreviatura_empresa = empresa.find('abreviatura').text
                    self.lst_empresa.agregar(id_empresa, nombre_empresa, abreviatura_empresa)
                    #PUNTOS DE ATENCION 
                    puntos_de_atencion = empresa.find('listaPuntosAtencion').findall('puntoAtencion')
                    for punto_de_atencion in puntos_de_atencion:
                        id_punto_atencion = punto_de_atencion.attrib['id']
                        
                        nombre_punto_atencion = punto_de_atencion.find('nombre').text
                        direccion_punto_atencion = punto_de_atencion.find('direccion').text
                        
                        #recuperar la empresa actual
                        nodo_empresa = self.lst_empresa.buscar_empresa(id_empresa)
                        nodo_empresa.lst_punto_atencion.agregar(id_punto_atencion, nombre_punto_atencion, direccion_punto_atencion)
                        
                        #ESCRITORIOS
                        escritorios = empresa.find('listaPuntosAtencion').find('puntoAtencion').findall('listaEscritorios')
                        for escritorio in escritorios:
                            id_escritorio = escritorio.find('escritorio').attrib['id']
                            
                            identificador_escritorio = escritorio.find('escritorio').find('identificacion').text
                            encargado_escritorio = escritorio.find('escritorio').find('encargado').text
                            nodo_punto_atencion = nodo_empresa.lst_punto_atencion.buscar_punto_atencion(id_punto_atencion)
                            nodo_punto_atencion.lst_escritorio.agregar(id_escritorio, identificador_escritorio, encargado_escritorio)
            self.lst_empresa.recorrer()                
        except Exception as e:
            print('error en cargar archivo =>', e)
        
        finally:
            archivo_xml.close()
    
    def cargar_archivo_configuracion(self, path):
        
        try:
            archivo_xml = open(path, 'r')
            if archivo_xml.readable():
                xml_datos = ET.fromstring(archivo_xml.read())
                
                configuraciones_iniciales = xml_datos.findall('configInicial') 
                for configuracion_inicial in configuraciones_iniciales:
                    id_configuracion_inicial = configuracion_inicial.attrib['id']
                    id_empresa = configuracion_inicial.attrib['idEmpresa']
                    id_punto = configuracion_inicial.attrib['idPunto']
                    print('id configuracion inicial => ', id_configuracion_inicial)
                    print('id empresa => ', id_empresa)
                    print('id punto => ', id_punto)
                    empresa = self.lst_empresa.buscar_empresa(id_empresa)
                    punto_atencion = empresa.lst_punto_atencion.buscar_punto_atencion(id_punto)
                    
                    
                    #ESCRITORIOS ACTIVOS
                    escritorios_activos = configuracion_inicial.find('escritoriosActivos')
                    for escritorio_activo in escritorios_activos:
                        id_escritorio_activo = escritorio_activo.attrib['idEscritorio']
                        #buscar escritorio por id y cambiar a true activo 
                        if punto_atencion.lst_escritorio.buscar_escritorio(id_escritorio_activo) !=None:
                            punto_atencion.lst_escritorio.buscar_escritorio(id_escritorio_activo).esta_activo = True
                        print('id escritorio activo=>', id_escritorio_activo)
                    #CLIENTES
                    lista_clientes = configuracion_inicial.find('listadoClientes').findall('cliente')
                    for cliente in lista_clientes:
                        nombre_cliente = cliente.find('nombre').text
                        print('nombre cliente =>', nombre_cliente)
                        
                        #TRANSACCIONES
                        lista_transacciones = cliente.find('listadoTransacciones')
                        for transaccion in lista_transacciones:
                            transaccion_id = transaccion.attrib['idTransaccion']
                            print('id transaccion =>', transaccion_id)
                           
        except Exception as e:
            print('error en cargar archivo configuracion =>', e)
        
        finally:
            archivo_xml.close()

cargar_archivo = CargarArchivo()
cargar_archivo.cargar_archivo('codigo-fuente/entrada.xml')
cargar_archivo.cargar_archivo_configuracion('codigo-fuente/entrada_configuracion.xml')
#cargar_archivo.lst_empresa.recorrer()