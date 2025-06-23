class Usuario:
    def __init__(self, id, nombre, apellido, correo, rol):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.rol = rol
        
    def login(self, correo, clave):
        return self.correo == correo
        