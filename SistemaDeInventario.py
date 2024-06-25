products = []
menu = """
Digite el numero de la opcion que desea ejecutar

1. Crear Producto
2. Mostrar Productos
3. Buscar Producto
4. Actualizar Producto
5. Eliminar Producto
6. Salir
"""

class Producto:
    def __init__(self, name, cantidad, precio):
      self.name = name
      self.cantidad = cantidad
      self.precio = precio
      
def capturarProducto(name, cantidad, precio):
    products.append(Producto(name, cantidad, precio))

def mostrarProductos():
    if products == []:
        print("No se han agregado Productos")
        
    for product in products:
        print(f"Producto: {product.name} - Cantidad: {product.cantidad} - Precio: ${product.precio}")

def buscarProducto(name):
    check = True
    for product in products:
        if product.name == name:
            print("Producto Encontrado")
            print(f"Producto: {product.name} - Cantidad: {product.cantidad} - Precio: ${product.precio}")
            check = False
            break
    if check:
        print("Producto No Encontrado")
    
def actualizarProducto(name):
    check = True
    for product in products:
        if product.name == name:
            print("Producto Encontrado")
            print(f"Producto: {product.name} - Cantidad: {product.cantidad} - Precio: ${product.precio}")
            check = False
            while True:
                try:
                    cantidad = input("Digite la cantidad del Producto que desea actualizar: ")
                    product.cantidad = cantidad
                    print("Actualizando Producto")
                    print(f"Producto: {product.name} - Cantidad: {product.cantidad} - Precio: ${product.precio}")
                    break
                except:
                    print("Error en la entrada, la cantidad debe ser un numero entero")
            break
    if check:
        print("Producto No Encontrado")

def eliminarProducto(name):
    check = True
    for contact in products:
        if contact.name == name:
            print("Producto Encontrado")
            products.remove(contact)
            print("Producto Eliminado")
            check = False
            break
    if check:
        print("Producto No Encontrado")

while True:
    print(menu)
    opcion = int(input("Digite el numero de la opcion: "))
    
    if opcion in [1, 2, 3, 4, 5, 6]:
        if opcion == 6:
            print("Saliendo del Programa")
            break
        elif opcion == 5:
            name = input("Digite el nombre del Producto a eliminar: ")
            eliminarProducto(name)
        elif opcion == 4:
            name = input("Digite el nombre del Producto que desea buscar: ")
            actualizarProducto(name)
        elif opcion == 3:
            name = input("Digite el nombre del Producto que desea buscar: ")
            buscarProducto(name)
        elif opcion == 2: 
            mostrarProductos()
        elif opcion == 1:
            while True:
                try:
                    name = input("Digite el nombre del producto: ")
                    cantidad = int(input("Digite la cantidad del producto: "))
                    precio = float(input("Digite el precio del producto: "))
                    capturarProducto(name, cantidad, precio)
                except:
                    print("Error de entrada, vuelva a intentar")
                break
    else:
        print("Opcion no Valida, el programa se cerrara")
        break