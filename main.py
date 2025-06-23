from sistema import SistemaGestorTiempo
from administrador import Administrador
from colaborador import Colaborador

if __name__ == '__main__':
    sistema = SistemaGestorTiempo()
    sistema.usuarios.append(Administrador(1,'Maribel', 'Pilquinao', 'mp@gmail.com'))
    sistema.usuarios.append(Colaborador(2, 'Fulano', 'Fulanix', 'ful@gmail.com'))
    
    usuario = sistema.iniciar_sesion()
    if usuario:
        sistema.mostrar_menu(usuario)
    