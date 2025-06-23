"""
Trabajo practico 6 - FUNCIONES
Alumno: JOSE MATIAS ALVAREZ MESEGUES
"""
import utils_TP6
import math

print("\nActividades\n\n1)")

# Actividades:

# 1) Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: 
# “Hola Mundo!”. Llamar a esta función desde el programa principal.

# Definicion de funciones

def imprimir_hola_mundo(saludo):
    print(saludo)

# Programa principal

imprimir_hola_mundo("Hola mundo") # Se puede ingresar cualquier saludo que desee el usuario

print("\n2)")

# 2) Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre 
# y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), 
# deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando 
# el nombre al usuario.

# Definicion de funciones

def nombre_ingresado_por_usuario():
    nombre = input("Ingrese su nombre: ")
    while not nombre.isalpha(): 
        nombre = input("Ingrese su nombre (solo letras): ")
    return nombre

def saludar_usuario(nombre):
    saludo = f"Hola {nombre}!"
    print(saludo)

# Programa principal

nombre = nombre_ingresado_por_usuario()
saludar_usuario(nombre)

print("\n3)")

# 3) Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que 
# reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en 
# [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Definicion de funciones

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"\nSoy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa principal

nombre, apellido = utils_TP6.nombre_apellido_verificado()
edad = utils_TP6.edad_verificada()
residencia = utils_TP6.lugar_residencia()
informacion_personal(nombre, apellido, edad, residencia)

print("\n4)")

# 4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y 
# devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro 
# y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para 
# mostrar los resultados.

# Definicion de funciones

def radio_por_usuario():
    radio = float(input("Ingrese el radio del circulo: "))
    return radio

def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    print(f"El area del circulo con {radio} de radio es: {round(area, 2)}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    print(f"El perimetro del circulo con {radio} de radio es: {round(perimetro, 2)}")

# Programa principal

radio = radio_por_usuario()
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

print("\n5)")

# 5) Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos 
# como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los 
# segundos y mostrar el resultado usando esta función.

# Definicion de funciones

def segundos_del_usuario():
    segundos = input("Ingrese los segundos a calcular, enteros: ")
    if segundos.isdigit():
        return int(segundos)
    else:
        print("ERROR, dato incorrecto, ingrese los segundos a calcular, enteros")

def segundos_a_horas(segundos):
    horas = segundos / 3600
    if horas == 1:
        print(f"Conversión: {segundos} segundos son {round(horas, 2)} hora")
    else:
        print(f"Conversión: {segundos} segundos son {round(horas, 2)} horas")

# Programa principal
segundos = segundos_del_usuario()
segundos_a_horas(segundos)

print("\n6)")

# 6) Crear una función llamada tabla_multiplicar(numero) que reciba un número como 
# parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario 
# el número y llamar a la función.

# Definicion de funciones

def numero_1_al_10():
    while True:
        num = int(input("Ingrese un número del 1 al 10: "))
        if 1 <= num <=10:
            return num
        else:
            print("Debe ingresar un número del 1 al 10.")

def tabla_multiplicar(numero): # En esta funcion se realiza una COMPOSICION DE FUNCIONES, utilizando un import desde utils.py
    for i in range(1, 11):
        if i == 10:  # Con este If lo unico que se logra es imprimir los resultados en la misma columna, algo estetico
            print(f"{numero} x {i} = {utils_TP6.formula_multiplicar_dos_numeros(numero, i)}") #COMPOSICION DE FUNCIONES
        else:
            print(f"{numero} x {i}  = {utils_TP6.formula_multiplicar_dos_numeros(numero, i)}") #COMPOSICION DE FUNCIONES

# Programa principal
numero = numero_1_al_10()
tabla_multiplicar(numero)

print("\n7)")

# 7) Crear una función llamada operaciones_basicas(a, b) que reciba dos números como 
# parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos 
# y dividirlos. Mostrar los resultados de forma clara.

# Definicion de funciones

def numeros_del_usuario():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    return num1, num2

def operaciones_basicas(a, b):
    resultados_lista = []
    
    suma = a + b
    resultados_lista.append(suma)
    
    resta = a - b
    resultados_lista.append(resta)
    
    multipli = a * b
    resultados_lista.append(multipli)
    
    if b != 0:
        división = a / b
        resultados_lista.append(round(división, 2))
    
    resultados_tupla = tuple(resultados_lista)
    
    print(f"Los ressultados de las operaciones basicas son:{resultados_tupla}")
    print(f"Suma: {resultados_tupla[0]}")
    print(f"Resta: {resultados_tupla[1]}")
    print(f"Multiplicación: {resultados_tupla[2]}")
    if b == 0:
        print("La division no se puede realizar, NO se puede dividir por cero")
    else:
        print(f"División: {resultados_tupla[3]}")

# Programa principal

a, b = numeros_del_usuario()
operaciones_basicas(a, b)

print("\n8)")

# 8) Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos
# y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario 
# los datos y llamar a la función para mostrar el resultado con dos decimales.

# Definicion de funciones

def peso_y_altura():
    peso   = float(input("Ingrese su peso (puede ser con deciamales): "))
    altura = float(input("Ingrese su altura (puede ser con deciamales): "))
    return peso, altura

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)  
    print("Segun la siguiente información:\n"
        f"Peso: {peso} Kg\n"
        f"Altura: {altura} mts\n"
        f"El IMC es: {round(imc, 2)}")

# Programa principal

peso, altura = peso_y_altura()
calcular_imc(peso, altura)

print("\n9)")

# 9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en 
# grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura 
# en Celsius y mostrar el resultado usando la función.

# Definicion de funciones

def temperatura_celsius():
    temp   = float(input("Ingrese la temperatura en grados celsius (solo números): "))
    return temp

def celsius_a_fahrenheit(celsius):
    en_fahrenheit = (celsius * (9/5)) + 32
    print(f"La temperatura de {celsius}°C es igual a {en_fahrenheit}°F")

# Programa principal

en_celsius = temperatura_celsius()
celsius_a_fahrenheit(en_celsius)

print("\n10)")

# 10) Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como 
# parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar 
# el resultado usando esta función.

# Definicion de funciones

def numeros_usuario():
    print("Ingrese 3 números")
    a = int(input("Ingrese un número: "))
    b = int(input("Ingrese otro número: "))
    c = int(input("Ingrese otro número: "))
    return a, b, c

def  calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio de {a}, {b} y {c}, es: {round(promedio, 2)}.")


# Programa principal

a, b, c = numeros_usuario()
calcular_promedio(a, b, c)

print("\nFin del Trabajo Practico N°6")


