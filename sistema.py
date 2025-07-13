from colaborador import Colaborador
from administrador import Administrador
from actividad import Actividad
from proyecto import Proyecto
from datetime import date, time
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
        print('usuario no encontrado o clave incorrecta.\n')
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
                fecha = input("Ingrese la fecha a asignar (YYYY-MM-DD): ")
                admin.asignar_fechas_registro(
                    [u for u in self.usuarios if u.get_rol() == 'colaborador'],
                    fecha
                )
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
                        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
                        admin.asignar_fecha_por_colaborador(colaboradores[idx], fecha)
                    else:
                        print("Número inválido.")
                except Exception as e:
                    print(f"Error: {e}")
            elif opcion == '4':
                # admin.generar_reporte([u for u in self.usuarios if u.get_rol() == 'colaborador'])
                self.exportar_resumen_proyecto_excel()
            elif opcion == '5':
                for p in self.proyectos:
                    p.mostrar_resumen()
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
        while True:
            id = input('Ingrese el id del nuevo proyecto: ')
            
            if any(p.get_id() == id for p in self.proyectos):
                print(f'Ya existe el id asignado al proyecto. Intenta de nuevamente')
            else:
                break
            
        nombre = input("Nombre del proyecto: ")
        descripcion = input("Descripción: ")
        proyecto = Proyecto(id, nombre, descripcion)
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
                print("selección inválida.")
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
                print(f"{i+1}. {p.get_nombre()}")
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
            print(f"error al registrar actividad: {e}")
            
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