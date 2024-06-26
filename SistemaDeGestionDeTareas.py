#Definicion de la clase, sus atributos y sus metodos constructores
class Tarea:
    def __init__(self, titulo, descripcion, estado):
      self.titulo = titulo
      self.descripcion = descripcion
      self.estado = estado

#Creacion de las variables globales del proyecto      
tareas = []
menu = """\nDigite el numero de la opcion que desea ejecutar

1. Crear Tarea
2. Mostrar Tareas
3. Buscar Tareas
4. Actualizar Tareas
5. Eliminar Tarea
6. Salir"""
opcionesEstado = """Opciones de estado para la tarea
1. Pendiente
2. Completada
Digite solo el numero de la opcion: """
opcionesMostrar = """\nOpciones de filtrado de tareas a mostrar
1. Tareas Pendientes
2. Tareas Completada
3. Todas las Tareas
Digite solo el numero de la opcion: """
opcionesActualizar = """\nOpciones de actualizacion para la tarea
1. Actualizar Descripcion
2. Actualizar Estado
Digite solo el numero de la opcion: """
opcionesBorrado = """\n¿Seguro que desea eliminar la tarea?
1. Si
2. No
Digite solo el numero de la opcion: """

#Tareas pre-cargadas para pruebas
tareas.append(Tarea("Leer Articulo", "Lectura del articulo de la flexion en vigas", 2))
tareas.append(Tarea("Armar Escritorio", "Armar el escritorio de triplex para el computador", 1))
tareas.append(Tarea("Comprar Comida", "Realizar el pedido de los tacos en Tom Gleen con la aplicacion de Rappi", 2))
tareas.append(Tarea("Crear Presentacion del Proyecto", "Realizar las diapositivas para la sustentacion del proyecto", 1))

#Creacion de las Funciones del proyecto
def estadoLetras(estado):
  if estado == 1:
    return "Pendiente"
  elif estado == 2:
    return "Completado"

def crearTareas():
  titulo = input("\nDigite el Titulo de la Tarea: ")
  descripcion = input("Digite la Descripcion de la tarea: ")
  while True:
    try:
      estado = int(input(opcionesEstado))
      if estado in [1, 2]:
        break
      else:
        print("\n---Digite solo un numero valido para la opcion que necesita---\n")
    except:
      print("\n---Digite solo un numero valido para la opcion que necesita---\n")
  
  tareas.append(Tarea(titulo, descripcion, estado))
  print(f"\n¡¡¡Tarea creada con Exito!!!\n------------\nTitulo: {titulo}\nDescripcion: {descripcion}\nEstado: {estadoLetras(estado)}\n------------")

def mostrarTareas():
  tareasMostrar = []
  while True:
    try:
      indexMostrar = int(input(opcionesMostrar))
      if indexMostrar in [1, 2, 3]:
        break
      else:
        print("\n---Digite solo un numero valido para la opcion que necesita---\n")
    except:
      print("\n---Digite solo un numero valido para la opcion que necesita---\n")
  
  if indexMostrar == 3:
    tareasMostrar = tareas
  
  else:
    for tarea in tareas:
      if tarea.estado == indexMostrar:
        tareasMostrar.append(tarea)
  
  tareaIndex = 1
  print("------------")
  for tarea in tareasMostrar:
    print(f"Tarea {tareaIndex}\nTitulo: {tarea.titulo}\nDescripcion: {tarea.descripcion}\nEstado: {estadoLetras(tarea.estado)}\n------------")
    tareaIndex += 1

def buscarTareas():
  nombreBusqueda = input("\nDigite el nombre de la tarea que desea buscar: ")
  print("\nBuscando Tarea...")
  busqueda = True
  
  for tarea in tareas:
    if tarea.titulo.lower() == nombreBusqueda.lower():
      print(f"\nTarea Encontrada\n------------\nTitulo: {tarea.titulo}\nDescripcion: {tarea.descripcion}\nEstado: {estadoLetras(tarea.estado)}\n------------")
      busqueda = False
      break
  
  if busqueda:
    print("\nTarea no Encontrada")

def actualizarTareas():
  nombreBusqueda = input("\nDigite el nombre de la tarea que desea actualizar: ")
  print("\nBuscando Tarea...")
  busqueda = True
  
  for tarea in tareas:
    if tarea.titulo.lower() == nombreBusqueda.lower():
      print(f"\nTarea Encontrada\n------------\nTitulo: {tarea.titulo}\nDescripcion: {tarea.descripcion}\nEstado: {estadoLetras(tarea.estado)}\n------------")
      busqueda = False
      
      while True:
        try:
          indexActualizar = int(input(opcionesActualizar))
          if indexActualizar in [1, 2]:
            if indexActualizar == 1:
              tarea.descripcion = input("\nDigite la nueva descripcion: ")
              print("\nActualizando descripcion...")
              print(f"\nTarea Actualizada\n------------\nTitulo: {tarea.titulo}\nDescripcion: {tarea.descripcion}\nEstado: {estadoLetras(tarea.estado)}\n------------")
            elif indexActualizar == 2:
                while True:
                  try:
                    print("")
                    estado = int(input(opcionesEstado))
                    if estado in [1, 2]:
                      tarea.estado = estado
                      print("\nActualizando esatado...")
                      print(f"\nTarea Actualizada\n------------\nTitulo: {tarea.titulo}\nDescripcion: {tarea.descripcion}\nEstado: {estadoLetras(tarea.estado)}\n------------")
                      break
                    else:
                      print("\n---Digite solo un numero valido para la opcion que necesita---")
                  except:
                    print("\n---Digite solo un numero valido para la opcion que necesita---")
            
            break
          
          else:
            print("\n---Digite solo un numero valido para la opcion que necesita---")
        except:
          print("\n---Digite solo un numero valido para la opcion que necesita---")
      
      break
  
  if busqueda:
    print("\nTarea no Encontrada")

def eliminarTareas():
  nombreBusqueda = input("\nDigite el nombre de la tarea que desea buscar: ")
  print("\nBuscando Tarea...")
  busqueda = True
  
  for tarea in tareas:
    if tarea.titulo.lower() == nombreBusqueda.lower():
      print(f"\nTarea Encontrada\n------------\nTitulo: {tarea.titulo}\nDescripcion: {tarea.descripcion}\nEstado: {estadoLetras(tarea.estado)}\n------------")
      busqueda = False
      while True:
        try:
          borrado = int(input(opcionesBorrado))
          if borrado in [1, 2]:
            if borrado == 1:
              print("\nEliminando Tarea...")
              tareas.remove(tarea)
              print("\nTarea Eliminada")
            elif borrado == 2:
              print("\nTarea no eliminada")
            break
          else:
            print("\n---Digite solo un numero valido para la opcion que necesita---")
        except:
          print("\n---Digite solo un numero valido para la opcion que necesita---")
      break
  
  if busqueda:
    print("\nTarea no Encontrada")

#Creacion del ciclo While para la ejecucion del proyecto
print("\nBienvenido al Gestor de Tareas")

while True:
  
  print(menu)
  opcion = input("\nDigite unicamente el numero de la opcion que desea ejecutar: ")
  try:
    opcion = int(opcion)
  except:
    print("\n---Digite solo valores numericos---")
  
  if opcion in range (1, 7):
    if opcion == 1:
      crearTareas()
      
    elif opcion == 2:
      mostrarTareas()
      
    elif opcion == 3:
      buscarTareas()
      
    elif opcion == 4:
      actualizarTareas()
      
    elif opcion == 5:
      eliminarTareas()
      
    elif opcion == 6:
      print("\nCerrando el programa, vuelva pronto!\n")
      break    
    
  else:
    print("\nOpcion no valida, utilice solo los numero de las opciones validas")