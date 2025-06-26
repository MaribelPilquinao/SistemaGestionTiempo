from usuario import Usuario

class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, correo):
        super().__init__(id, nombre, apellido, correo, rol = 'colaborador')
        self.proyecto_asignado = []
        self.actividades = []
        self.fechas_asignadas = []
        
    def registrar_actividad(self, actividad):
        self.actividades.append(actividad)
        print(f'Actividad registrada para {self.nombre} {self.apellido}')
        
    def ver_historial_actividades(self):
        if not self.actividades:
            print('No hay actividades registradas')
            return
        print(f'historial de {self.nombre} {self.apellido}')
        for act in self.actividades:
            print(f'- {act.fecha} | {act.descripcion} | {act.proyecto.nombre} | {act.calcular_duracion():2.f}h')
        
    def ver_fechas_asignadas(self):
        if not self.fechas_asignadas:
            print('No hay fechas asignadas')
            return
        print('Fechas asignadas para registrar actividades: ')
        for fecha in self.fechas_asignadas:
            print(f' - {fecha}')