from datetime import datetime

class Actividad:
    def __init__(self, id, fecha, hora_ini, hora_fin, descripcion, tipo, proyecto, usuario, esta_activo=True):
        self.id = id
        self.fecha = fecha
        self.hora_ini = hora_ini
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.tipo = tipo
        self.proyecto = proyecto
        self.usuario = usuario
        self.esta_activo = esta_activo
        
    def calcular_duracion(self):
        return (datetime.combine(self.fecha, self.hora_fin) - datetime.combine(self.fecha, self.hora_ini)).total_seconds() / 3600