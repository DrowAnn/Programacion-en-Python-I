"""
Funciones def
"""

# def suma (x, y):
#     return x + y

# print(f"El resultado de la suma es: {suma(10, 11)}")

# def tablaMultiplicar (x):
#     for i in range (1, 21):
#         print(f"{x} * {i} = {x * i}")
        
# tablaMultiplicar(12)

# """
# Capture dos valores y comparelos, indique cual es el mayor
# """

# def comparacionValores (x, y):
#     if (x > y):
#         print(f"{x} es mayor que {y}")
#     elif (x < y):
#         print(f"{y} es mayor que {x}")
#     else:
#         print(f"{x} es igual a {y}")
        
# num1 = int(input("Digite el primer numero: "))
# num2 = int(input("Digite el segundo numero: "))

# comparacionValores(num1, num2)

"""
Clases y Objetos

metodo __init__ inicializa los atributos de un objeto

class nombre_de_la_clase:
    def __init__(self, atributos):
"""

# class auto:
#     marca = "Mazda"
#     modelo = 2014

# taxi = auto()

# print(taxi.marca)
# print(taxi.modelo)

class Humano:
    def __init__(self, edad, nombre, ocupacion):
        self.edad = edad
        self.nombre = nombre
        self.ocupacion = ocupacion

persona1 = Humano(25, "Robert", "Analista de Datos")

print(f"{persona1.nombre} tiene {persona1.edad} años de edad y trabaja como {persona1.ocupacion}")