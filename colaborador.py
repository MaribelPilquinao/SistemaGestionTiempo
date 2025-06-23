from usuario import Usuario

class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, correo):
        super().__init__(id, nombre, apellido, correo, rol = 'colaborador')
        self.proyecto_asignado = []
        self.actividades = []