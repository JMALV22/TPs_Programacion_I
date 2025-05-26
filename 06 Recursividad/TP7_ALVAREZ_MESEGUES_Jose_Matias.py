"""
Trabajo practico 7 - Aplicación de la Recursividad
Alumno: JOSE MATIAS ALVAREZ MESEGUES
"""

import math

print("\nActividades\n\n1)")

# Actividades:

# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

# Definicion de funciones

def factorial(num):
    # Condicional ternario
    return 1 if num == 0 else num * factorial(num - 1)
    # Como CASO BASE, cuando num = 0, retorna 1.

# Programa principal

facto = int(input("Ingrese un número para calculo de factorial: "))
print(factorial(facto))

print("\n2)")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique

# Definicion de funciones

def sec_fibonacci(posi):
    #  En este caso tenemos 2 CASOS BASE, posi = 0 y pasi = 1
    if posi == 0:
        return 0
    elif posi == 1:
        return 1
    # En la sucesion de Fibo, para N posicion = (posiN -1) + (posiN - 2)
    else:
        return sec_fibonacci(posi - 2) + sec_fibonacci(posi - 1)

# Programa principal

posi = int(input("Ingrese una posicion de fibonacci: "))
for i in range(0, posi + 1): # Utilizamos un for para imprimir pada posicion
    print(f"Para la posición {i} es: {sec_fibonacci(i)}")

print("\n3)")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛 ** 𝑚 = 𝑛 ∗ 𝑛 ** (𝑚−1) . Prueba esta función en un
# algoritmo general.

# Definicion de funciones

def potencia_n(base, expo):
    return 1 if expo == 0 else potencia_n(base, expo - 1) * base

# Programa principal

base = int(input("Ingrese la base: "))
expo = int(input("Ingrese el exponente: "))

print(f"El número {base} elevado a la {expo} es: {potencia_n(base, expo)}")

print("\n4)")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
# unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
# procedimiento:

# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

# 🧠Ejemplo:
# Convertir el número 10 a binario:

# 10 ÷ 2 = 5 resto: 0
# 5  ÷ 2 = 2 resto: 1
# 2  ÷ 2 = 1 resto: 0
# 1  ÷ 2 = 0 resto: 1 

# Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010"

# Definicion de funciones

def potencia_n(num_base_decimal):

    num_bin = ""

    if num_base_decimal == 0:
        return num_bin

    if num_base_decimal % 2 == 0:
        num_bin += "0"
    else:
        num_bin += "1"

    return potencia_n(num_base_decimal // 2) + num_bin

# Programa principal

num_decimal = int(input("Ingrese el número decimal a convertir en binario: "))

print(f"El número decimal {num_decimal} es ingual a {potencia_n(num_decimal)} en binario")

print("\n5)")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

# Definicion de funciones

def revers_str_recursiva(palabra):
    long = len(palabra)
    palindromo = palabra[0]
    return palindromo if long == 1 else revers_str_recursiva(palabra[1:]) + palindromo

def es_palindromo(palabra):
    if revers_str_recursiva(palabra) == palabra:
        print("Es PALINDROMO")
    else:
        print("NO es PALINDROMO")

# Programa principal

palabra = input("Ingrese una cadena de texto sin espacios ni tildes: ")
es_palindromo(palabra)

print("\n6)")

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número
# entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9)    → 9
# suma_digitos(305)  → 8  (3 + 0 + 5)

# Definicion de funciones
"""
Utilizamos esta funcion para verificar que el usuario ingrese un numero entero y natural
La misma la podemos utilizar mas adelante, ya que nos da la opcion de ingresar:
Mensaje, minimo a chequear y maximo...
"""
def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = int(input(mensaje))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}"))
    return n

def suma_digitos(n):
    digito = n % 10
    return n if n < 10 else suma_digitos(n//10) + digito

# Programa principal

nume = leer_entero_validado("Ingrese un número entero positivo: ", 1)
print(f"La suma de los digitos del número {nume} es: {suma_digitos(nume)}")

print("\n7)")

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.

# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.

# Ejemplos:
# contar_bloques(1) → 1  (1)
# contar_bloques(2) → 3  (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

# Definicion de funciones
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return contar_bloques(n - 1) + n

# Programa principal
""" Para pedirle el numero al usuario, llamamos la funcion del ejercicio anterior y la adaptamos a nustro requerimiento"""
num_bloques = leer_entero_validado("Ingresa el número de bloque del último nivel (entero, positivo): ", 1)
print(f"Se necesita para construir la pidamide: {contar_bloques(num_bloques)}")

print("\n8)")

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.

# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5)     → 4
# contar_digito(123456, 7)   → 0

# Definicion de funciones

def contar_digito(numero, digito):
    dig = numero % 10
    cont = 0
    if dig == digito:
        cont += 1
    if numero < 10:
        return cont
    else: 
        return contar_digito(numero//10, digito) + cont

# Programa principal

numero = int(input("Ingrese el número a evaluar: "))
digito = int(input("Ingrese el digito a buscar: "))

print(f"El digito {digito} esta {contar_digito(numero, digito)} veces en el número {numero}")

print("\nFin del Trabajo Practico N°7")


