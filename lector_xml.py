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
                        escritorios = punto_de_atencion.find('listaEscritorios').findall('escritorio')
                        #escritorios = empresa.find('listaPuntosAtencion').find('puntoAtencion').findall('listaEscritorios')
                        for escritorio in escritorios:
                            id_escritorio = escritorio.attrib['id']
                            
                            identificador_escritorio = escritorio.find('identificacion').text
                            encargado_escritorio = escritorio.find('encargado').text
                            nodo_punto_atencion = nodo_empresa.lst_punto_atencion.buscar_punto_atencion(id_punto_atencion)
                            nodo_punto_atencion.lst_escritorio.agregar(id_escritorio, identificador_escritorio, encargado_escritorio)
                   
                    lista_tranasacciones = empresa.find('listaTransacciones').findall('transaccion')
                    for transaccion in lista_tranasacciones:
                        transaccion_id = transaccion.attrib['id']
                        nombre_transaccion = transaccion.find('nombre').text
                        tiempo = transaccion.find('tiempoAtencion').text
                        empresa = self.lst_empresa.buscar_empresa(id_empresa)
                        empresa.lst_transacciones.agregar_transaccion(transaccion_id, nombre_transaccion, tiempo)
                print('#¡EMPRESAS CARGADAS CON ÉXITO!#')            
                            
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
                   
                    empresa = self.lst_empresa.buscar_empresa(id_empresa)
                    punto_atencion = empresa.lst_punto_atencion.buscar_punto_atencion(id_punto)
                    if empresa != None and punto_atencion != None:
                    
                        #ESCRITORIOS ACTIVOS
                        escritorios_activos = configuracion_inicial.find('escritoriosActivos')
                        for escritorio_activo in escritorios_activos:
                            id_escritorio_activo = escritorio_activo.attrib['idEscritorio']
                            #buscar escritorio por id y cambiar a true activo 
                            if punto_atencion.lst_escritorio.buscar_escritorio(id_escritorio_activo) !=None:
                                punto_atencion.lst_escritorio.buscar_escritorio(id_escritorio_activo).esta_activo = True 
                            else: print('El escritorio no exite!')
                            
                            print('id escritorio activo=>', id_escritorio_activo)
                        #CLIENTES
                        lista_clientes = configuracion_inicial.find('listadoClientes').findall('cliente')
                        for cliente in lista_clientes:
                            dpi = cliente.attrib['dpi']
                            nombre_cliente = cliente.find('nombre').text
                            punto_atencion.lst_clientes.agregar_cliente(dpi, nombre_cliente)
                            nodo_cliente =  punto_atencion.lst_clientes.buscar_cliente(dpi)
                            #TRANSACCIONES DE LOS CLIENTES
                            lista_transacciones = cliente.find('listadoTransacciones')
                            for transaccion in lista_transacciones:
                                transaccion_id = transaccion.attrib['idTransaccion']
                                transaccion_cantidad = transaccion.attrib['cantidad']
                                transaccion_tiempo = float(empresa.lst_transacciones.buscar_transaccion(transaccion_id).tiempo)*int(transaccion_cantidad)
                                nodo_cliente.tiempo_transaccion += transaccion_tiempo
                                nodo_cliente.lst_transacciones.agregar_transaccion_cliente(transaccion_id,transaccion_cantidad)
                            
                            
                            nodo_cliente.tiempo_en_cola = punto_atencion.lst_clientes.tiempo_cola(dpi)
                            nodo_cliente.tiempo_total = nodo_cliente.tiempo_transaccion+nodo_cliente.tiempo_en_cola
                        
                        
                        
                            
                        print('tiempos')
                        punto_atencion.lst_clientes.tiempo_total()
                        
                        punto_atencion.tiempo_promedio_espera = punto_atencion.lst_clientes.tiempo_promedio_espera()
                        
                        punto_atencion.tiempo_max_espera = punto_atencion.lst_clientes.tiempo_max_espera()
                        
                        punto_atencion.tiempo_min_espera = punto_atencion.lst_clientes.tiempo_min_espera()
                        
                        punto_atencion.tiempo_promedio_atencion = punto_atencion.lst_clientes.tiempo_promedio_atencion()
                        
                        
                        punto_atencion.tiempo_max_atencion = punto_atencion.lst_clientes.tiempo_max_atencion()
                        
                        
                        punto_atencion.tiempo_min_atencion = punto_atencion.lst_clientes.tiempo_min_atencion()
                        
                        
                            
                                
                                
                    else: print('La empresa o el punto de atención no existen!')      
        except Exception as e:
            print('error en cargar archivo configuracion =>', e)
        
        finally:
            archivo_xml.close()
    
    
    def atender_cliente(self, id_empresa, id_punto_atencion):
        empresa = self.lst_empresa.buscar_empresa(id_empresa)
        punto_atencion = empresa.lst_punto_atencion.buscar_punto_atencion(id_punto_atencion)
        lst_escritorios_activos = punto_atencion.lst_escritorio.lista_escritorios_activos()
        punto_atencion.lst_clientes.listar()
        if punto_atencion.lst_escritorio.escritorios_activos() != 0:
            
            if len(lst_escritorios_activos) >= 1:

                for escritorio in lst_escritorios_activos:
                    cliente = punto_atencion.lst_clientes.atender()
                    if cliente != None:
                        print('-------------------------------------------')
                        print(f'Cliente atendido: {cliente.nombre_cliente}')
                        print(f'Por escritorio: {escritorio.id_escritorio}')
                        print('-------------------------------------------')
                        escritorio.lst_clientes_atendidos.agregar(cliente)
                        #escritorio.lst_clientes_atendidos.imprimir()
                    else: print('No hay más clientes por atender!')
        else:
            print('Por el momento no hay escritorios activos para atender a clientes!') 
        
                
            
        
        
        
        
        
        
    def crear_empresa(self):
        print('---------------------------')
        id_empresa = input('Ingresa el id de la empresa: ')
        nombre_empresa = input('Ingresa el nombre de la emprsa:')
        abreviatura_empresa = input('Ingresa la abreviatura de la empresa: ')
        self.lst_empresa.agregar(id_empresa, nombre_empresa, abreviatura_empresa)
        nodo_empresa = self.lst_empresa.buscar_empresa(id_empresa)
        #PUNTOS_ATENCION
        while True:
            print('----------------Puntos de atención-----------------------')
            id_punto_atencion = input('Ingresa el id del punto atencion: ')
            nombre_punto_atencion = input('Ingresa el nombre del punto de atencion: ')
            direccion_punto_atencion = input('Ingresa la direccion del punto de atencion: ')
            nodo_empresa.lst_punto_atencion.agregar(id_punto_atencion, nombre_punto_atencion, direccion_punto_atencion)
            
            print('¿desea agregar mas puntos?')
            print('1. sí')
            print('2. no')
            opcion_agregar_mas = input('Ingresa una opción: ')
            
            if opcion_agregar_mas == '2':
                break
        while True:        
            print('-------------- Escritorios ------------------------')
            nodo_empresa.lst_punto_atencion.recorrer()
            id_punto_atencion = input('Ingresa el id del punto de atencion al que quieres agregar escritorios: ')
            nodo_punto_atencion = nodo_empresa.lst_punto_atencion.buscar_punto_atencion(id_punto_atencion)
            if nodo_punto_atencion != None:
                id_escritorio = input('Ingresa el Id del escritorio que deseas agregar: ')
                identificador = input('Ingresa el identificador: ')
                encargado_escritorio = input('Ingresa el nombre del encargado: ')
                print('Deseas que el escritorio este activo: ')
                print('1. Sí')
                print('2. No')
                activado = input('Ingresa una respuesta: ')
                if activado == '1':
                    nodo_punto_atencion.lst_escritorio.agregar(id_escritorio,identificador, encargado_escritorio)
                    nodo_escritorio = nodo_punto_atencion.lst_escritorio.buscar_escritorio(id_escritorio)
                    nodo_escritorio.esta_activo = True
                else:
                    nodo_punto_atencion.lst_escritorio.agregar(id_escritorio,identificador, encargado_escritorio)
                    nodo_escritorio = nodo_punto_atencion.lst_escritorio.buscar_escritorio(id_escritorio)
            opcion = input('Desea agregar mas escritorios: \n 1. Sí \n 2. No \n')
            if opcion == '2':
                break
            
    def elegir_empresa_punto_atencion(self):
        print('-------------Empresas------------------')
        self.lst_empresa.recorrer()
        id_empresa = input('Ingresa el id de la empresa: ')
        empresa_seleccionada = self.lst_empresa.buscar_empresa(id_empresa)
        print('')
        print('-------------Puntos de Atención------------------')
        empresa_seleccionada.lst_punto_atencion.recorrer()
        id_punto_atencion = input('Ingresa el id del punto de atencion: ')
        punto_atencion_seleccionado = empresa_seleccionada.lst_punto_atencion.buscar_punto_atencion(id_punto_atencion)
        print('')
        print('-------------Estado Punto Atención------------------')
        print('')
        print('Cantidad Escritorios Activos: ', punto_atencion_seleccionado.lst_escritorio.escritorios_activos())
        print('')
        print('Cantidad Escritorios Inactivos: ', punto_atencion_seleccionado.lst_escritorio.escritorios_desactivados())
        print('')
        print('Clientes en espera: ', punto_atencion_seleccionado.lst_clientes.clientes_en_espera())
        print('')
        print('-------------Opciones Punto de Atención--------------')
        
        while True:
            print('1. Activar Escritorio')
            print('2. Desactivar Escritorio')
            print('3. Atender Cliente.')
            print('4. Solicitud de Atención.')
            print('5. Simular Actividad.')
            print('6. Regresar')
            opcion = int(input('Escoge una opcion: '))
            if opcion == 1:
                id_escritorio = input('Ingresa el Id del escritorio que deseas activar: ')
                if punto_atencion_seleccionado.lst_escritorio.activar_escritorio(id_escritorio):
                    print('#ESCRITORIO ACTIVADO CON EXITO#')
                else: print('#EL ID NO CONCUERDA CON NINGUN ESCRITORIO O YA SE ENCUENTRA ACTIVO#')
            if opcion == 2:
                id_escritorio = input('Ingresa el Id del escritorio que deseas activar: ')
                if punto_atencion_seleccionado.lst_escritorio.desactivar_escritorio(id_escritorio):
                    print('#ESCRITORIO DESACTIVADO CON EXITO#')
                else: print('#EL ID NO CONCUERDA CON NINGUN ESCRITORIO O YA SE ENCUENTRA DESACTIVADO#')
            if opcion == 3:
                self.atender_cliente(id_empresa, id_punto_atencion)
            if opcion == 6:
                break
    
    def crear_cliente(self, id_empresa, id_punto_atencion):
        print('--------------AGREGAR CLIENTES-----------------')
        nodo_empresa = self.lst_empresa.buscar_empresa(id_empresa)
        nodo_punto_atencion = nodo_empresa.lst_punto_atencion.buscar_punto_atencion(id_punto_atencion)
        while True:
           dpi_cliente =  input('Ingresa el DPI del cliente: ')
           nombre_cliente =   input('Ingresa el Nombre del cliente: ')
           nodo_punto_atencion.lst_clientes.agregar_cliente(dpi_cliente, nombre_cliente)
           opcion = input('¿Desea agregar mas clientes al punto? \n 1. Sí \n 2. No \n')
           if opcion == '2':
               break
            
        
    
        

cargar_archivo = CargarArchivo()
""" cargar_archivo.cargar_archivo('codigo-fuente/entrada.xml')
cargar_archivo.cargar_archivo_configuracion('codigo-fuente/entrada_configuracion.xml')
cargar_archivo.atender_cliente("1", "001") """
#cargar_archivo.crear_empresa()