class Proyecto:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.colaboradores = []
        self.actividades = [] 

    def asignar_colaborador(self, colaborador):
        if colaborador not in self.colaboradores:
            self.colaboradores.append(colaborador)

    def agregar_actividad(self, actividad):
        self.actividades.append(actividad)

    def obtener_total_horas(self):
        total = 0
        for actividad in self.actividades:
            total += actividad.calcular_duracion()
        return total

    def mostrar_resumen(self):
        print(f"Proyecto: {self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print(f"Colaboradores asignados: {len(self.colaboradores)}")
        print(f"Total de actividades registradas: {len(self.actividades)}")
        print(f"Total de horas trabajadas: {self.obtener_total_horas():.2f}")
