from usuario import Usuario

class Administrador(Usuario):
    def __init__(self, id, nombre, apellido, correo):
        super().__init__(id, nombre, apellido, correo, rol='administrador')
        
    def asignar_fechas_registro(self):
        pass
    
    def generar_reporte(self):
        pass
    
    