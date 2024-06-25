print("Bienvenido a la Calculadora de Python")

menu = """
Digite el numero de la opcion que desea ejecutar

1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Salir
"""

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        print("No es posible dividir por 0")
    else:
        print(f"El resultado es : {num1 / num2}")
    
while True:
    print(menu)
    
    opcion = int(input("Digite la opcion que desesa ejecutar: "))
    
    if opcion in [1, 2, 3, 4, 5]:
        if opcion == 5:
            print("El programa se cerrara")
            break
        else:
            num1 = float(input("Digite el primer numero: "))
            num2 = float(input("Digite el segundo numero: "))
            
            if opcion == 1:
                print(f"El resultado es : {suma(num1, num2)}")
            elif opcion == 2:
                print(f"El resultado es : {resta(num1, num2)}")
            elif opcion == 3:
                print(f"El resultado es : {multiplicacion(num1, num2)}")
            elif opcion == 4:
                division(num1, num2)
    else:
        print("La opcion no es valida, el programa se cerrara")
        break