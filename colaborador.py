from usuario import Usuario

class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, correo, clave):
        super().__init__(id, nombre, apellido, correo, clave, rol = 'colaborador')
        self.__proyectos_asignados = []
        self.__actividades = []
        self.__fechas_asignadas = []
        
    def registrar_actividad(self, actividad):
        if actividad is None:
            print('debe registrar actividad')
            return
        self.__actividades.append(actividad)
        print(f'actividad registrada para {self.get_nombre()} {self.get_apellido()}')
        
    def ver_historial_actividades(self):
        if not self.__actividades:
            print('No hay actividades registradas')
            return
        print(f'historial de {self.get_nombre()} {self.get_apellido()}')
        for act in self.__actividades:
            print(f'- {act.get_fecha()} | {act.get_descripcion()} | {act.get_proyecto().get_nombre()} | {act.calcular_duracion():2.f}h')
        
    def ver_fechas_asignadas(self):
        if not self.__fechas_asignadas:
            print('No hay fechas asignadas')
            return
        print('Fechas asignadas para registrar actividades: ')
        for fecha in self.__fechas_asignadas:
            print(f' - {fecha}')
            
    def asignar_fecha(self, fecha):
        if fecha not in self.__fechas_asignadas:
            self.__fechas_asignadas.append(fecha)
        
    def get_actividades(self):
        return self.__actividades
        
    def get_proyectos_asignados(self):
        return self.__proyectos_asignados