"""
Trabajo practico 1 - Estructuras secuenciales
Alumno: JOSE MATIAS ALVAREZ MESEGUES
"""

# Actividades

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = input("Ingresa tu nombre: ")

print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre    = input("Ingresa tu nombre: ")
apellido  = input("Ingresa tu apellido: ")
edad      = input("Ingresa tu edad: ")
residecia = input("Ingresa tu lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residecia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = float(input("Ingrese el radio del circulo: "))

perimetro = 3.14 * (radio * 2)
area      = 3.14 * (radio ** 2)

print(f"El perimetro del Circulo es {perimetro} mts. y su area {area} mts.")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

seg = float(input("Ingrese los segundos a convertir en horas: "))

seg_en_horas = seg / 3600

print(f"{seg} segundos son {seg_en_horas} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

tabla = int(input("Ingrese la tabla que desea construir: "))

print(f"{tabla} x 1  = {tabla * 1} ")
print(f"{tabla} x 2  = {tabla * 2} ")
print(f"{tabla} x 3  = {tabla * 3} ")
print(f"{tabla} x 4  = {tabla * 4} ")
print(f"{tabla} x 5  = {tabla * 5} ")
print(f"{tabla} x 6  = {tabla * 6} ")
print(f"{tabla} x 7  = {tabla * 7} ")
print(f"{tabla} x 8  = {tabla * 8} ")
print(f"{tabla} x 9  = {tabla * 9} ")
print(f"{tabla} x 10 = {tabla * 10} ")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y 
# muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

n1 = int(input("Ingrese el primer numero distinto de cero: "))
n2 = int(input("Ingrese el segundo numero distinto de cero: "))

print(f"{n1} + {n2}  = {n1 + n2} ")
print(f"{n1} - {n2}  = {n1 - n2} ")
print(f"{n1} * {n2}  = {n1 * n2} ")
print(f"{n1} / {n2}  = {n1 / n2} ")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
# Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
# 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2

peso   = float(input("Ingrese su peso en Kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

print(f"Su Indice de Masa Corporal 'IMC' es {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 
# Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32.

temp_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

temp_fahrenheit = ((9/5) * temp_celsius) + 32

print(f"La temperatura {temp_celsius} °C es igual a {temp_fahrenheit} °F")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

print("Promedia de 3 numeros")
n_1 = int(input("Ingrese el primer número: "))
n_2 = int(input("Ingrese el segundo número: "))
n_3 = int(input("Ingrese el tercer número: "))

promedio = (n_1 + n_2 + n_3) / 3

print(f"El promedio de los 3 numeros ingresado es {promedio}.")

print("FIN DEL TRABAJO PRACTICO I")
