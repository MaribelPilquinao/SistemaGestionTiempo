from sistema import SistemaGestorTiempo
from administrador import Administrador
from colaborador import Colaborador

if __name__ == '__main__':
    sistema = SistemaGestorTiempo.cargar_datos()

    sistema.usuarios.append(Administrador(1, 'Maribel', 'Pilquinao', 'mp@gmail.com', 'admin123'))
    sistema.usuarios.append(Colaborador(2, 'Fulano', 'Fulanix', 'ful@gmail.com', 'ful123'))
    
    #menu + login
    usuario = sistema.iniciar_sesion()
    if usuario:
        sistema.mostrar_menu(usuario)

sistema.guardar_datos()