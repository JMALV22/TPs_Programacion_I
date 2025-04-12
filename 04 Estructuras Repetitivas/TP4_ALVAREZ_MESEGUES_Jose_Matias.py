"""
Trabajo practico 4 - Estructuras repetitivas
Alumno: JOSE MATIAS ALVAREZ MESEGUES
"""
import random

print("\nActividades\n\n1)")

# Actividades:

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for num in range(101):
    print(num)

print("\n2)")

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num = input("Ingrese un numero entero ")

cant_digitos = len(num)

print(f"El número tiene {cant_digitos} digitos")

print("\n3)")
# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
suma = 0

for num in range(num1 + 1, num2):
    suma += num 

print(f"La suma de los numeros es {suma}")

print("\n4)")
# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

num = int(input("Ingrese el primer numero: "))
suma = 0
suma += num

while num != 0:
    num = int(input("Ingrese otro numero: "))
    suma += num

print(f"El total acumulado es {suma}")

print("\n5)")
# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

num_adivina = random.randint(0, 9)
selec = 10
intentos = 0
print("Adivina el número random...")
while selec != num_adivina:
    selec = int(input("Ingresa un numero entre el 0 y el 9 "))
    intentos += 1
    if 0 > selec or selec > 9:
        print("El numero debe ser entre 0 y 9")
    elif selec != num_adivina:
        print("No es el número...\nIntenta nuevamente!!!")
    
print(f"Felicitaciones!!! ADIVINASTE, el numero es {num_adivina}")
print(f"Cantidad de intendos: {intentos}")

print("\n6)")
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

print("\n7)")
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = int(input("Ingrese un número entero positivo: "))
suma = 0

for x in range(0, num + 1):
    suma += x

print(f"La suma de los numero comprendidos entre 0 y {num} es: {suma}")

print("\n8)")
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cant_numeros = 5 # Reemplazando este número, cambiamos la cantidad de veces que el usuario puede ingresar los números.
num_pares = 0

for i in range(cant_numeros):
    num_usuario = int(input("Ingrese un numero entero: "))
    if num_usuario % 2 == 0:
        num_pares += 1

print(f"Ingreso {num_pares} números pares")

print("\n9)")
# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cant_numeros = 5 # Reemplazando este número, cambiamos la cantidad de veces que el usuario puede ingresar los números.
suma = 0

for i in range(cant_numeros):
    num_usuario = int(input("Ingrese un numero entero: "))
    suma += num_usuario

media = suma / cant_numeros

print(f"La media es {media}")

print("\n10)")
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = input("Ingrese un numero entero: ")
long = len(num)
num_invert = ""

for i in range(long - 1, -1, -1):
    num_invert += num[i]

print(num_invert)

print("\nFin del Trabajo Practico N°4")