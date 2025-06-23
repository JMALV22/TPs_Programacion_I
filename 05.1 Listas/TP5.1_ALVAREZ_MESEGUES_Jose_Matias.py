"""
Trabajo practico 5 - LISTAS
Alumno: JOSE MATIAS ALVAREZ MESEGUES
"""
import random

print("\nActividades\n\n1)")

# Actividades:

# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

mult_4 = []

for i in range(1,101):
    if i % 4 == 0:
        mult_4.append(i)

print("La siguiente es una lista de los numeros multiplos de 4, del 1 al 100")
print(mult_4)

print("\n2)")

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

lista = ["Rojo", True, "Verde", 10, 4.7]
penult = lista[-2]

print(lista)
print(f"El penultimo elemento de la lista es: {penult}")

print("\n3)")

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista: para
# crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: 
# lista_vacia = []

print("Crea tu lista, ingresa tres palabras...")

lista_vacia = []
lista_vacia.append(input("Ingresa tu primer palabra: "))
lista_vacia.append(input("Ingresa tu segunda palabra: "))
lista_vacia.append(input("Ingresa tu tercer palabra: "))

lista_3plabras = lista_vacia

print("Tu lista es")
print(lista_3plabras)

print("\n4)")

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. 
# Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo 
# funciona el indexing con números negativos! 

animales = ["perro", "gato", "conejo", "pez"]
print(f"Lista original: {animales}")

animales[1] = "loro"
animales[-1] = "oso"

print(f"Lista modificada: {animales}")

print("\n5)")

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# ANALISIS:
# Ejecutando el codigo dado, se puede observar que elimina el maximo numero de la lista, 
# mediante la funcion "remove()" se elimina el maximo numero obtenido con la funcion "max()".

print("\n6)")

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar 
# por pantalla los dos primeros.

lista_10_al_30 = list(range(10,31,5))

print(lista_10_al_30)

print("\n7)")

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera. 

autos = ["sedan", "polo", "suran", "gol"]

print(f"Lista original: {autos}")

autos[1] = "clio"
autos[2] = "yaris"

print(f"Lista modificada: {autos}")

print("\n8)")

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. 
# Imprimir la lista resultante por pantalla.

dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

print("\n9)")

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

print(f"Lista original {compras}")

# a)
compras[2].append("jugo")
# b)
compras[1][1] = "tallarines"
# c)
del compras[0][0]
# d)
print(f"Lista final {compras}")

print("\n10)")

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)

print("\nFin del Trabajo Practico N°5")