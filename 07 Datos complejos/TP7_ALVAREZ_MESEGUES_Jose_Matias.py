"""
Trabajo practico 7 - Estructuras de datos complejas
Alumno: JOSE MATIAS ALVAREZ MESEGUES
"""

print("\nActividades\n\n1)")

# Actividades:

# 1) Dado el diccionario precios_frutas 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
print(f"Diccionario original:\n{precios_frutas}")
# Añadir las siguientes frutas con sus respectivos precios:

# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(f"Diccionario con nuevas frutas:\n{precios_frutas}")

print("\n2)")
# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:

# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(f"Diccionario con nuevos precios:\n{precios_frutas}")

print("\n3)")
# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin 
# los precios.

frutas_keys = precios_frutas.keys()
print(f"Las frutas sin precios son:\n{list(frutas_keys)}")

print("\n4)")
# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {'Juan': 115644822, 'Pedro': 251116542} 

def consul_contacto():
    corte = "A"
    while corte != "S":
        nombre = input("Ingrese el nombre del contacto a consultar: ").capitalize()
        consult = contactos.get(nombre, "El contacto no existe")
        if consult == "El contacto no existe":
            print(consult)
        else:
            print(f"El numero de {nombre} es: {consult}")
        corte = input("Ingrese 'S' para salir al menu principal o enter para continuar consultando:\n").upper()

def agreg_contacto():
    corte = "A"
    while corte != "S":
        nombre = input("Ingrese el nombre del contacto a agregar: ").capitalize()
        cant_cont = len(contactos)
        if nombre in contactos:
            print("El contacto existe")
        elif cant_cont == 5:
            print("Agenda completa (max. 5 contactos)")
        else:
            telefono = int(input("Ingrese el número telefonico: "))
            contactos[nombre] = telefono
        corte = input("Ingrese 'S' para salir al menu principal o enter para continuar agregando:\n").upper()

def elimin_contacto():
    corte = "A"
    while corte != "S":
        nombre = input("Ingrese el nombre del contacto a eliminar: ").capitalize()
        if not(nombre in contactos):
            print("El contacto no existe")
        else:
            del contactos[nombre]
            print("Contacto eliminado")
        corte = input("Ingrese 'S' para salir al menu principal o enter para continuar eliminando:\n").upper()

def mostrar_contactos():
    print("Contactos actuales:")
    for i in contactos:
        print(f"{i} = {contactos[i]}")

def main():
    fin = False
    while fin == False:
        print("\n### --- Menu --- ###\n" \
            "Maximo 5 contactos      \n" \
            "1) Consultar contacto   \n" \
            "2) Agregar contacto     \n" \
            "3) Eliminar contacto    \n" \
            "4) Mostrar lista de contacto actual\n" \
            "5) Finalizar\n")

        opcion = input("Ingrese una opcción: ")

        if opcion == "1":
            consul_contacto()
        elif opcion == "2":
            agreg_contacto()
        elif opcion == "3":
            elimin_contacto()
        elif opcion == "4":
            mostrar_contactos()
        elif opcion == "5":
            fin = True
        else:
            print(" ¡¡¡ ingrese una opción del 1 al 5: !!! ")

main()

print("\n5)")
# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase a evaluar: ").lower()
list_palabras = frase.split()
lista_palb_unicas = set(list_palabras)
dict = {}
for i in lista_palb_unicas:
    dict[i] = 0

for i in list_palabras:
    if i in dict:
        dict[i] += 1

print(f"Lista de palabras unicas:\n{lista_palb_unicas}")
print(f"Diccionario con número de veces que se repiten las palabras:\n{dict}")

print("\n6)")
# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

alumnos = {}
cont = 1
while cont < 4:
    cont += 1
    alum = input("Ingrese el nombre de un alumno: ").capitalize()
    alumnos[alum] = [0, 0, 0]
    for i in range(0,len(alumnos[alum])):
        nota = float(input("Ingrese la nota: "))
        alumnos[alum][i] = nota
    alumnos[alum] = tuple(alumnos[alum])

print(alumnos)

print("\n7)")
# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1_aprobados = ["Juan", "Matias", "Pedro", "Federico", "Nicolas"]
parcial_2_aprobados = ["Juan", "Matias", "Javier", "Ricardo", "Pedro"]

aprob_ambos_parc = []
aprob_solo_uno = []

for i in parcial_1_aprobados:
    for j in parcial_2_aprobados:
        if i == j:
            aprob_ambos_parc.append(i)

check = False
for i in parcial_1_aprobados:
    for j in parcial_2_aprobados:
        if i == j:
            check = True
    if check == False:
        aprob_solo_uno.append(i)
    check = False

check = False
for i in parcial_2_aprobados:
    for j in parcial_1_aprobados:
        if i == j:
            check = True
    if check == False:
        aprob_solo_uno.append(i)
    check = False

print(f"Los que aprobaron ambos parciales fueron: {aprob_ambos_parc}")
print(f"Los que aprobaron solo un parcial fueron: {aprob_solo_uno}")

print("\n8)")
# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

productos = {
    'Lapiceras': 20,
    'Lapiz': 10,
    'Goma de borrar': 5,
    'Tinta para sellos': 6,
    'Hoja A4': 20,
    } 

def consul_stock():
    corte = "A"
    while corte != "S":
        producto = input("Ingrese el nombre del producto para ver su stock: ").capitalize()
        consult = productos.get(producto, "El producto no existe")
        if consult == "El producto no existe":
            print(consult)
        else:
            print(f"Stock del producto: {producto} es: {consult}")
        corte = input("Ingrese 'S' para salir al menu principal o enter para continuar consultando:\n").upper()

def agreg_stock_a_producto():
    corte = "A"
    while corte != "S":
        producto = input("Ingrese el nombre del producto a agregar stock: ").capitalize()
        if producto in productos:
            stock = int(input("Ingrese el stock a agregar: "))
            productos[producto] += stock
        else:
            print("El producto no existe")
        corte = input("Ingrese 'S' para salir al menu principal o enter para continuar agregando:\n").upper()

def agreg_producto():
    corte = "A"
    while corte != "S":
        producto = input("Ingrese el nombre del producto a agregar stock: ").capitalize()
        if producto in productos:
            print("El producto existe")
        else:
            stock = int(input("Ingrese el stock del nuevo producto: "))
            productos[producto] = stock
        corte = input("Ingrese 'S' para salir al menu principal o enter para continuar agregando:\n").upper()

def elimin_producto():
    corte = "A"
    while corte != "S":
        producto = input("Ingrese el nombre del producto a eliminar: ").capitalize()
        if not(producto in productos):
            print("El producto no existe")
        else:
            del productos[producto]
            print("producto eliminado")
        corte = input("Ingrese 'S' para salir al menu principal o enter para continuar eliminando:\n").upper()

def mostrar_productos():
    print("Stock de productos actualizados:")
    for i in productos:
        print(f"{i} = {productos[i]}")

def main():
    fin = False
    while fin == False:
        print("\n### --- Menu --- ###     \n" \
            "1) Consultar stock           \n" \
            "2) Agregar stock a producto  \n" \
            "3) Agregar producto          \n" \
            "4) Eliminar producto         \n" \
            "5) Mostrar productos y stock \n" \
            "6) Finalizar\n")

        opcion = input("Ingrese una opcción: ")

        if opcion == "1":
            consul_stock()
        elif opcion == "2":
            agreg_stock_a_producto()
        elif opcion == "3":
            agreg_producto()
        elif opcion == "4":
            elimin_producto()
        elif opcion == "5":
            mostrar_productos()
        elif opcion == "6":
            fin = True
        else:
            print(" ¡¡¡ ingrese una opción del 1 al 6: !!! ")

main()

print("\n9)")
# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

eventos = {}

def cosultar_agenda():
    print("Eventos al dia de la fecha:")
    if eventos:
        for i in eventos:
            print(f"{i} = {eventos[i]}")
    else:    
        print("No hay eventos al momento")

def agregar_evento():
    corte = "A"
    while corte != "S":
        dia_hora = []
        dia = input("Ingrese dia del nuevo evento: ")
        hora = input("Hora del evento (formato xx:xx): ")
        dia_hora.append(dia)
        dia_hora.append(hora)
        dia_hora = tuple(dia_hora)
        if dia_hora in eventos:
            print("La fecha y hora estan ocupadas")
        else:
            evento = input("Ingrese el evento: ")
            eventos[dia_hora] = evento
        corte = input("Ingrese 'S' para salir al menu principal o enter para continuar eliminando:\n").upper()

def elimin_evento():
    corte = "A"
    while corte != "S":
        evento = input("Ingrese el evento a eliminar: ").capitalize()
        i = 0
        elemen_a_eliminar = []
        for clave, value in eventos.items():
            if evento == value:
                i += 1
                elemen_a_eliminar.append(clave)
        for i in elemen_a_eliminar:
            del eventos[i]
            print("Evento eliminado")
        if i == 0:       
            print("El evento no existe")
        corte = input("Ingrese 'S' para salir al menu principal o enter para continuar eliminando:\n").upper()

def main():
    fin = False
    while fin == False:
        print("\n### --- Menu --- ###      \n" \
            "1) Consultar agenda           \n" \
            "2) Agregar evento             \n" \
            "3) Eliminar evento            \n" \
            "4) Finalizar                  \n"
            )

        opcion = input("Ingrese una opcción: ")

        if opcion == "1":
            cosultar_agenda()
        elif opcion == "2":
            agregar_evento()
        elif opcion == "3":
            elimin_evento()
        elif opcion == "4":
            fin = True
        else:
            print(" ¡¡¡ ingrese una opción del 1 al 4: !!! ")

main()

print("\n10)")
# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

original = {"Argentina":"Buenos Aires", "Uruguay":"Montevideo", "Chile":"Santiago"}

invertido = {}

for clave, value in original.items():
    invertido[value] = clave

print(f"Diccionario original:\n{original}")
print(f"Diccionario invertido:\n{invertido}")

print("\nTP finalizado")