from sistema import SistemaGestorTiempo
from administrador import Administrador
from colaborador import Colaborador

if __name__ == '__main__':
    sistema = SistemaGestorTiempo.cargar_datos()

    sistema.usuarios.append(Administrador(1, 'Maribel', 'Pilquinao', 'admin@gmail.com', 'admin123'))
    sistema.usuarios.append(Colaborador(2, 'Pedro', 'López', 'colab@gmail.com', 'colab123'))

    def agregar_usuario_unico(sistema, nuevo_usuario):
        for usuario in sistema.usuarios:
            if usuario.get_correo() == nuevo_usuario.get_correo():
                return
        sistema.usuarios.append(nuevo_usuario)

    #menu + login
    usuario = sistema.iniciar_sesion()
    if usuario:
        sistema.mostrar_menu(usuario)

sistema.guardar_datos()