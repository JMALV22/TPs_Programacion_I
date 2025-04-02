"""
Trabajo practico 3 - Estructuras condicionales
Alumno: JOSE MATIAS ALVAREZ MESEGUES
"""
from statistics import mode, median, mean
import random

print("\nActividades\n\n1)")

# Actividades:

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")

print("\n2)")
# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
# deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar 
# el mensaje “Desaprobado”.

nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

print("\n3)")
# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el 
# uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

num_par = int(input("Ingrese un número par: "))

if num_par % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

print("\n4)")
# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

print("\n5)")
# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por la
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

contra = input("Ingrese su contraseña de entre 8 y 14 caracteres: ")

long_contra = len(contra)

if 8 <= long_contra <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

print("\n6)")
# Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media 
# y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el 
# resultado por pantalla.
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media   = mean(numeros_aleatorios)
print(f"La media es: {media}")

mediana = median(numeros_aleatorios)
print(f"La mediana es: {mediana}")

moda    = mode(numeros_aleatorios)
print(f"La moda es: {moda}\n")

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")

print("\n7)")
# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

frase = input("Ingrese una frase o palabra: ")

vocal = frase[-1].lower()

es_vocal = vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u"

if es_vocal:
    print(frase + "!")
else:
    print(frase)

print("\n8)")
# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
#   1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#   2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#   3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")

print("Elija una de las siguentes opciones")
print("1) Su nombre en mayuscula.\n2) Su nombre en minuscula.\n3) Su nombre con la primer letra en mayuscula.")

opcion = input("Ingrese su opción: ")

if opcion == "1":
    en_mayuscula = nombre.upper()
    print(en_mayuscula)
elif opcion == "2":
    en_minuscula = nombre.lower()
    print(en_minuscula)
elif opcion == "3":
    p_letra_mayus = nombre.title()
    print(p_letra_mayus)
else:
    print("Ingrese un número del 1 al 3")

print("\n9)")
# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
#    ● Menor que 3: "Muy leve" (imperceptible).
#    ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#    ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#      generalmente no causa daños).
#    ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#      débiles).
#    ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#    ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

categoria = float(input("Ingrese la magnitud del terremoto "))

if categoria < 3:
    print("Muy leve (imperceptible)")
elif 3 <= categoria < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= categoria < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= categoria < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= categoria < 7:
    print("Muy fuerte (puede causar daños significativos)")
elif 7 <= categoria:
    print("Extremo (puede causar graves daños a gran escala)")
else:
    print("Ingrese una escala correcta, mayor a 0")

print("\n10)")
# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año (TABLA EN PDF DEL TP3)
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese el hemisferio en el que se encuentra: ").title()

mes = input("Ingrese el mes del año: ").title()

dia = int(input("Ingrese el día: "))

if hemisferio == "Norte": 
    if   mes == "Enero" or mes == "Febrero":
        print("Es Invierno")   
    elif mes == "Marzo":
        if 1 <= dia <= 20:
            print("Es Invierno")
        elif 21 <= dia <=31:
            print("Es Primavera")
    elif mes == "Abril" or mes == "Mayo":
        print("Es Primavera")
    elif mes == "Junio":
        if 1 <= dia <= 20:
            print("Es Primavera")
        elif 21 <= dia <=30:
            print("Es Verano")
    elif mes == "Julio" or mes == "Agosto":
        print("Es Verano")
    elif mes == "Septiembre":
        if 1 <= dia <= 20:
            print("Es Verano")
        elif 21 <= dia <=30:
            print("Es Otoño")
    elif mes == "Octubre" or mes == "Noviembre":
        print("Es Otoño")
    elif mes == "Diciembre":
        if 1 <= dia <= 20:
            print("Es Otoño")
        elif 21 <= dia <=31:
            print("Es Invierno")
elif hemisferio == "Sur": 
    if   mes == "Enero" or mes == "Febrero":
        print("Es Verano")   
    elif mes == "Marzo":
        if 1 <= dia <= 20:
            print("Es Verano")
        elif 21 <= dia <=31:
            print("Es Otoño")
    elif mes == "Abril" or mes == "Mayo":
        print("Es Otoño")
    elif mes == "Junio":
        if 1 <= dia <= 20:
            print("Es Otoño")
        elif 21 <= dia <=30:
            print("Es Invierno")
    elif mes == "Julio" or mes == "Agosto":
        print("Es Invierno")
    elif mes == "Septiembre":
        if 1 <= dia <= 20:
            print("Es Invierno")
        elif 21 <= dia <=30:
            print("Es Primavera")
    elif mes == "Octubre" or mes == "Noviembre":
        print("Es Primavera")
    elif mes == "Diciembre":
        if 1 <= dia <= 20:
            print("Es Primavera")
        elif 21 <= dia <=31:
            print("Es Verano")

print("\nFin del Trabajo Practico N°3")

