from colaborador import Colaborador
from administrador import Administrador
from actividad import Actividad
from proyecto import Proyecto


class SistemaGestorTiempo:
    def __init__(self):
        self.usuarios = []
        self.proyectos = []
        self.actividades = []
        
    def iniciar_sesion(self):
        correo = input('ingresar correo: ')
        for usuario in self.usuarios:
            if usuario.correo == correo:
                print(f'Bienvenido, {usuario.nombre} {usuario.apellido}')
                return usuario
        print('usuario no encontrado')
        return None
        
    def mostrar_menu(self, usuario):
        if usuario.rol == 'administrador':
            pass
        elif usuario.rol == 'colaborador':
            pass
        
