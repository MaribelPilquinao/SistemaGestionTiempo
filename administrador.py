from usuario import Usuario

class Administrador(Usuario):
    def __init__(self, id, nombre, apellido, correo, clave):
        super().__init__(id, nombre, apellido, correo, clave, rol='administrador')
        
    def asignar_fechas_registro(self, colaboradores, fecha):
        for colaborador in colaboradores:
            colaborador.asignar_fecha(fecha)
        print(f'Fecha: {fecha} asignada a todos los colaboradores.')
        
    def asignar_fecha_por_colaborador(self, colaborador, fecha):
        colaborador.asignar_fecha(fecha)
        print(f"Fecha {fecha} asignada a {colaborador.get_nombre()} {colaborador.get_apellido()}.")
    
    def generar_reporte(self, colaboradores):
        print('Reporte de actividades por colaborador: ')
        for colaborador in colaboradores:
            actividades = colaborador.get_actividades()
            total_horas = sum(act.calcular_duracion() for act in actividades)
            print(f'{colaborador.get_nombre()} {colaborador.get_apellido()}: {total_horas:.2f} horas')
    
    