from lector_xml import cargar_archivo
class Main:
    def __init__(self) -> None:
        pass
    
    def menu_principal(self):
        opcion = int()
        salir = True
        while salir:
            print('---------------------------------------------------')
            print('Bienvenido a “Soluciones Guatemaltecas, S.A.”')
            print('1. Configuracion de empresa')
            print('2. Seleccionar Empresa')
            print('3. Cargar archivo con configuración inicial para la prueba.')
            print('4  Salir.')
            opcion = int(input('Escoge un opcion: '))
            try:
                if opcion == 1:
                    self.menu_configuracion_empresa()
                if opcion == 2:
                    cargar_archivo.elegir_empresa_punto_atencion()
                if opcion == 3:
                    cargar_archivo.cargar_archivo_configuracion()
                if opcion == 4:
                    salir = False
            
            except Exception as e:
                print('error en menu principal => ',e)
                
                    
            print('---------------------------------------------------')
    def menu_configuracion_empresa(self):
        while True:
            print('-------------CONFIGURACION DE EMPRESA---------------------')
            print('1. Cargar archivo.')
            print('2. Crear Empresa.')
            print('3. Cargar archivo con configuración inicial.')
            print('4. Menú Principal.')
            print('')
            opcion = int(input('Escoge una opcion: '))
            
            if opcion == 1:
                path = input('Ingresa la ruta del archivo xml:  ')
                cargar_archivo.cargar_archivo(path)
            if opcion == 2:  
                cargar_archivo.crear_empresa()
            if opcion == 3:
                path = input('Ingresa la ruta del archivo configuracion xml:  ')
                cargar_archivo.cargar_archivo_configuracion(path)
            if opcion == 4:
                break 

if __name__ == '__main__':
    main = Main()
    main.menu_principal()