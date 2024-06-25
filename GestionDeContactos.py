contacts = []
menu = """
Digite el numero de la opcion que desea ejecutar

1. Crear Contacto
2. Mostrar Contactos
3. Buscar Contacto
4. Eliminar Contacto
5. Salir
"""

class Contacto:
    def __init__(self, name, phoneNumber):
      self.name = name
      self.phoneNumber = phoneNumber
      
def capturarContacto(name, phoneNumber):
    contacts.append(Contacto(name, phoneNumber))

def mostrarContactos():
    if contacts == []:
        print("No se han agregado Productos")
        
    for contact in contacts:
        print(f"Contacto: {contact.name} - Numero de Telefono: {contact.phoneNumber}")

def buscarContacto(name):
    for contact in contacts:
        if contact.name == name:
            print("Contacto Encontrado")
            print(f"Contacto: {contact.name} - Numero de Telefono: {contact.phoneNumber}")
            break
    print("Contacto No Encontrado")

def eliminarContacto(name):
    for contact in contacts:
        if contact.name == name:
            print("Contacto Encontrado")
            contacts.remove(contact)
            print("Contacto Eliminado")
            break
    print("Contacto No Encontrado")

while True:
    print(menu)
    opcion = int(input("Digite el numero de la opcion: "))
    
    if opcion in [1, 2, 3, 4, 5]:
        if opcion == 5:
            print("Saliendo del Programa")
            break
        elif opcion == 4:
            name = input("Digite el nombre del contacto a eliminar: ")
            eliminarContacto(name)
        elif opcion == 3:
            name = input("Digite el nombre del contacto que desea buscar: ")
            buscarContacto(name)
        elif opcion == 2: 
            mostrarContactos()
        elif opcion == 1:
            name = input("Digite el nombre: ")
            phoneNumber = input("Digite el numero de telefono: ")
            capturarContacto(name, phoneNumber)
    else:
        print("Opcion no Valida, el programa se cerrara")
        break