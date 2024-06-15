# """
# Condicionales
# """

# num1 = float(input("Digite el numero 5:"))

# if (num1 == 5):
#     print("Ese es el numero")
# else:
#     print("Ese no es el numero")
    
# a = 2
# b = 5

# if (b != 0):
#     print(a/b)

"""
Ejercicio Condicionales

Sistema para calcular el promedio de 4 notas de un estudiante
"""

nombre = input("Digite el nombre del estudiante: ")

nota1 = float(input("Digite la primera nota del estudiante: "))
nota2 = float(input("Digite la segunda nota del estudiante: "))
nota3 = float(input("Digite la tercera nota del estudiante: "))
nota4 = float(input("Digite la cuarta nota del estudiante: "))

promedio = (nota1 + nota2 + nota3 + nota4) / 4

if (promedio >= 3.0):
    print(f"Felicitaciones, {nombre}, 'APROBASTE' el curso, tu promedio fue de: {promedio}")
else:
    print(f"{nombre}, lastimosamente 'NO' aprobaste el curso, tu promedio fue de: {promedio}")

