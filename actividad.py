from datetime import datetime

class Actividad:
    def __init__(self, id, fecha, hora_ini, hora_fin, descripcion, tipo, proyecto, usuario, esta_activo=True):
        self.__id = id
        self.__fecha = fecha
        self.__hora_ini = hora_ini
        self.__hora_fin = hora_fin
        self.__descripcion = descripcion
        self.__tipo = tipo
        self.__proyecto = proyecto
        self.__usuario = usuario
        self.__esta_activo = esta_activo
        
    def calcular_duracion(self):
        try:
            if self.__hora_fin < self.__hora_ini:
                raise ValueError('La hora final no puede ser menor que la hora de unicio')
            duracion = datetime.combine(self.__fecha, self.__hora_fin) - datetime.combine(self.__fecha, self.__hora_ini)
            return duracion.total_seconds() / 3600
        except Exception as e:
            print(f'Error al calcular duracion: {e}')
            
    #getters
    def get_id(self):
        return self.__id
        
    def get_fecha(self):
        return self.__fecha
        
    def get_hora_ini(self):
        return self.__hora_ini
        
    def get_hora_fin(self):
        return self.__hora_fin
        
    def get_descripcion(self):
        return self.__descripcion
        
    def get_tipo(self):
        return self.__tipo
        
    def get_proyecto(self):
        return self.__proyecto
        
    def get_usuario(self):
        return self.__usuario
        
    def get_is_active(self):
        return self.__esta_activo
        
    #elminar la logica
    def eliminar(self):
        self.__esta_activo = False
            
        