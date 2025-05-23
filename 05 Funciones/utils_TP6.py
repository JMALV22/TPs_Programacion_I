"""
Funciones del punto numero 3
"""
def nombre_apellido_verificado(): # Se verifica que el usuario ingrese solo letras
    while True:
        nombre   = input("Ingrese su nombre: ").strip()
        apellido = input("Ingrese su apellido: ").strip()
        es_valido = True

        for i in nombre: 
            if not (i.isalpha() or i == " "): # Mediante la funcion .isalpha(), chequeamos que solo tengamos letras en la variable nombre y espacios. 
                es_valido = False
                break
            for i in apellido: # Con un for anidado verificamos la siguiente variable que es apellido.
                if not (i.isalpha() or i == " "):
                    es_valido = False
                    break

        if es_valido: # Si los condicionales if de los for no se cumplen, la variable es_valido sigue siendo True y la funcion devuelve las variable nombre y apellido. 
            return nombre, apellido
        else:
            print("Nombre o Apellido inválido. Solo se permiten letras y espacios.")

# La siguiente funcion es identica a la anterior, solo que verificamos que sean solo numeros
def edad_verificada(): # Se verifica que el usuario ingrese solo numeros
    while True:
        edad = input("Ingrese su edad: ").strip()
        es_valido = True

        for i in edad:
            if not (i.isdigit()):
                es_valido = False
                break
        
        if es_valido:
            return edad
        else:
            print("Edad inválida. Solo se permiten números.")

def lugar_residencia():
    residencia = input("Ingrese su lugar de residencia: ").strip()
    return residencia

"""
Funciones del punto numero 6
"""
def formula_multiplicar_dos_numeros(a, b):
    c = a * b
    return c