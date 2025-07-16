from colaborador import Colaborador
from administrador import Administrador
from actividad import Actividad
from proyecto import Proyecto
from datetime import date, time, datetime
import pickle
import os


class SistemaGestorTiempo:
    def __init__(self):
        self.usuarios = []
        self.proyectos = []
        self.actividades = []

    def iniciar_sesion(self):
        correo = input('Ingrese su correo: ')
        clave = input('Ingrese su clave: ')
        for usuario in self.usuarios:
            if usuario.login(correo, clave):
                print(f'\n Bienvenido, {usuario.get_nombre()} {usuario.get_apellido()} ({usuario.get_rol()})\n')
                return usuario
        print('Usuario no encontrado o clave incorrecta.\n')
        return None

    def mostrar_menu(self, usuario):
        if usuario.get_rol() == 'administrador':
            self.menu_administrador(usuario)
        elif usuario.get_rol() == 'colaborador':
            self.menu_colaborador(usuario)

    def menu_administrador(self, admin):
        while True:
            print("\n--- MENÚ ADMINISTRADOR ---")
            print("1. Crear proyecto")
            print("2. Asignar fechas de registro a todos los colaboradores")
            print("3. Asignar fechas de registro por colaborador")
            print("4. Generar reporte de actividades Excel")
            print("5. Ver resumen de proyectos")
            print("6. Asignar colaborador a proyecto")
            print("0. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.crear_proyecto()
            elif opcion == '2':
                fecha_actual = datetime.now().strftime('%d-%m-%Y')
                fecha_inicio = input(f"Fecha de inicio [{fecha_actual}]: ") or fecha_actual
                fecha_fin = input("Fecha de fin (opcional): ")
                rango_fechas = [fecha_inicio, fecha_fin] if fecha_fin.strip() else [fecha_inicio]
                colaboradores = [u for u in self.usuarios if u.get_rol() == 'colaborador']
                for colaborador in colaboradores:
                    for f in rango_fechas:
                        colaborador.asignar_fecha(f)
                print(f"Fechas {', '.join(rango_fechas)} asignadas a todos los colaboradores.")
            elif opcion == '3':
                colaboradores = [u for u in self.usuarios if u.get_rol() == 'colaborador']
                if not colaboradores:
                    print("No hay colaboradores disponibles.")
                    return

                print("Seleccione un colaborador:")
                for i, colab in enumerate(colaboradores):
                    print(f"{i + 1}. {colab.get_nombre()} {colab.get_apellido()}")

                try:
                    idx = int(input("Número de colaborador: ")) - 1
                    if 0 <= idx < len(colaboradores):
                        fecha = input("Ingrese la fecha (DD-MM-YYYY): ")
                        admin.asignar_fecha_por_colaborador(colaboradores[idx], fecha)
                    else:
                        print("Número inválido.")
                except Exception as e:
                    print(f"Error: {e}")
            elif opcion == '4':
                self.exportar_resumen_proyecto_excel()
            elif opcion == '5':
                if not self.proyectos:
                    print("No hay proyectos activos.")
                    return
                print("\n=== PROYECTOS ACTIVOS ===")
                for idx, p in enumerate(self.proyectos, start=1):
                    print(f"\n--- Proyecto # {idx} ---")
                    p.mostrar_resumen()
                    print('-' * 30)
            elif opcion == '6':
                self.asignar_colaborador_a_proyecto()
            elif opcion == '0':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida.")

    def menu_colaborador(self, colaborador):
        while True:
            print("\n--- MENÚ COLABORADOR ---")
            print("1. Registrar actividad")
            print("2. Ver historial de actividades")
            print("3. Ver fechas asignadas")
            print("0. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.registrar_actividad(colaborador)
            elif opcion == '2':
                colaborador.ver_historial_actividades()
            elif opcion == '3':
                colaborador.ver_fechas_asignadas()
            elif opcion == '0':
                print("Saliendo...")
                break
            else:
                print("Opción inválida.")

    def crear_proyecto(self):
        nuevo_id = str(len(self.proyectos) + 1)
        print(f"ID del proyecto: {nuevo_id}")
        nombre = input("Nombre del proyecto: ")
        descripcion = input("Descripción: ")
        proyecto = Proyecto(nuevo_id, nombre, descripcion)
        self.proyectos.append(proyecto)
        print(f"Proyecto '{nombre}' creado correctamente.")

    def exportar_resumen_proyecto_excel(self):
        if not self.proyectos:
            print("No hay proyectos disponibles.")
            return

        print("\nProyectos:")
        for i, proyecto in enumerate(self.proyectos):
            print(f"{i + 1}. {proyecto.get_nombre()}")

        try:
            idx = int(input("Seleccione el número del proyecto: ")) - 1
            if 0 <= idx < len(self.proyectos):
                self.proyectos[idx].exportar_resumen_excel()
            else:
                print("Selección inválida.")
        except Exception as e:
            print(f"Error: {e}")

    def registrar_actividad(self, colaborador):
        try:
            id = input("ID de actividad: ")
            fecha = input("Fecha (YYYY-MM-DD): ")
            hora_ini = input("Hora inicio (HH:MM): ")
            hora_fin = input("Hora fin (HH:MM): ")
            descripcion = input("Descripción: ")
            tipo = input("Tipo de actividad (desarrollo, prueba, etc.): ")

            print("Proyectos disponibles:")
            for i, p in enumerate(self.proyectos):
                print(f"{i + 1}. {p.get_nombre()}")
            idx = int(input("Seleccione el número de proyecto: ")) - 1
            proyecto = self.proyectos[idx]

            actividad = Actividad(
                id,
                date.fromisoformat(fecha),
                time.fromisoformat(hora_ini),
                time.fromisoformat(hora_fin),
                descripcion,
                tipo,
                proyecto,
                colaborador
            )

            colaborador.registrar_actividad(actividad)
            proyecto.agregar_actividad(actividad)
            self.actividades.append(actividad)

        except Exception as e:
            print(f"Error al registrar actividad: {e}")

    def asignar_colaborador_a_proyecto(self):
        if not self.proyectos:
            print("No hay proyectos disponibles.")
            return

        print("\nProyectos:")
        for i, proyecto in enumerate(self.proyectos):
            print(f"{i + 1}. {proyecto.get_nombre()}")
        idx_proyecto = int(input("Seleccione el número del proyecto: ")) - 1
        proyecto = self.proyectos[idx_proyecto]

        colaboradores = [u for u in self.usuarios if u.get_rol() == 'colaborador']
        if not colaboradores:
            print("No hay colaboradores registrados.")
            return

        print("\nColaboradores:")
        for i, colab in enumerate(colaboradores):
            print(f"{i + 1}. {colab.get_nombre()} {colab.get_apellido()}")
        idx_colab = int(input("Seleccione el número del colaborador: ")) - 1
        colaborador = colaboradores[idx_colab]

        proyecto.asignar_colaborador(colaborador)

    def guardar_datos(self, archivo='datos.pkl'):
        with open(archivo, 'wb') as f:
            pickle.dump(self, f)
        print("Datos guardados correctamente.")

    @staticmethod
    def cargar_datos(archivo='datos.pkl'):
        if os.path.exists(archivo):
            with open(archivo, 'rb') as f:
                print("Cargando datos guardados...")
                sistema = pickle.load(f)

                usuarios_unicos = {}
                for u in sistema.usuarios:
                    usuarios_unicos[u.get_correo()] = u
                sistema.usuarios = list(usuarios_unicos.values())

            return sistema
        else:
            print("No se encontraron datos previos, iniciando sistema nuevo.")
            return SistemaGestorTiempo()

