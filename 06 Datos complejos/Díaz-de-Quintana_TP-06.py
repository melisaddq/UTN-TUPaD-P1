# Trabajo práctico Nº 6 de Datos complejos. PROGRAMACION 1
# Alumna: Díaz de Quintana, Melisa. Comisión: 12
"""
# 1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# Añadir las siguientes frutas con sus respectivos precios:
# Naranja = 1200
# Manzana = 1500
# Pera = 2300 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} #diccionario original
precios_frutas['Naranja'] = 1200 #agrego frutas y precios
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)


# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado 
# en el punto anterior, actualizar los precios de las siguientes frutas:
# Banana = 1330
# Manzana = 1700
# Melón = 2800 

precios_frutas['Banana'] = 1330 #modifico y agrego de la misma forma
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar 
# el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios. 

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)
"""
# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# Luego, pedí un nombre y mostrale el número asociado, si existe.
"""
contactos = {}
print("Por favor, ingrese nombre y número de teléfono para agendar")
# Carga de los 5 contactos:
for i in range(5):
    nombre = input(f"Nombre del contacto {i + 1}: ")
    telefono = input(f"Teléfono de {nombre}: ")
    contactos[nombre] = telefono #guardado
print(contactos)

consultar_contacto=(input("¿Quieres averiguar algún teléfono? Introduce su nombre: "))
if consultar_contacto in contactos:
    print(f"El teléfono de {consultar_contacto} es {contactos[consultar_contacto]}")
else:
    print(f"El contacto '{consultar_contacto}' no está agendado.")
"""
# 5) Solicita al usuario una frase e imprime:
# Las palabras únicas (usando un set).
# Un diccionario con la cantidad de veces que aparece cada palabra.
"""
frase = input ("Por favor, introduzca una frase: ")
palabras = frase.split() #divido las palabras

#Palabras únicas:
palabras_unicas = set(palabras) #creo el set y elimino duplicidades
print("Palabras únicas:", palabras_unicas)

# diccionario
veces_palabra = {} #creo diccionario
for palabra in palabras:
    veces_palabra[palabra] = veces_palabra.get(palabra, 0) + 1  # Contador

print("Frecuencia de palabras:", veces_palabra)
"""
# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno.

"""
alumnos = {} #creo un diccionario para poder modificarlo con los inputs

# datos alumnos
for i in range(3):
    nombre = input(f"Nombre del alumno {i + 1}: ")
    notas = []  # creo una lista para despues convertirla en tupla
    
    # notas:
    for j in range(3):
        nota = float(input(f"  Nota {j + 1} de {nombre}: "))
        notas.append(nota)  #lo agrego al final de la lista
    # Convierto lista de notas a tupla y guardo en el dicc
    alumnos[nombre] = tuple(notas)


print ("Registro de alumnos, notas y promedios: ")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)  # Calculo el promedio
    print(f"{nombre}: Notas = {notas} Promedio = {promedio}") 
"""
# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# Mostrá los que aprobaron ambos parciales.
# Mostrá los que aprobaron solo uno de los dos.
# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
"""
# Sets de estudiantes
aprobados_parcial1 = {101, 103, 105, 107, 109, 110, 112, 115}
aprobados_parcial2 = {101, 102, 105, 108, 110, 111, 113, 115}

print("Estudiantes que aprobaron Parcial 1:", aprobados_parcial1)

print("Estudiantes que aprobaron Parcial 2:", aprobados_parcial2)

aprobados_ambos = aprobados_parcial1.intersection(aprobados_parcial2) # interseccion = elementos comunes
print(f"Estudiantes que aprobaron AMBOS parciales: {aprobados_ambos}")

aprobados_solo_uno = aprobados_parcial1.symmetric_difference(aprobados_parcial2) #diferencia simétrica = en uno u otro

print(f"Estudiantes que aprobaron SOLO UNO de los parciales: {aprobados_solo_uno}")

aprobados_al_menos_uno = aprobados_parcial1.union(aprobados_parcial2) # union sin repetir

print(f"Lista de estudiantes que aprobaron AL MENOS UN parcial: {aprobados_al_menos_uno}")
"""
# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario:
#Consultar el stock de un producto ingresado.
#Agregar unidades al stock si el producto ya existe.
#Agregar un nuevo producto si no existe. 

"""
stock_productos = { # Diccionario stock
    "Manzanas": 100,
    "Peras": 75,
    "Naranjas": 120,
    "Bananas": 50
}

def consultar_stock(producto):
    if producto in stock_productos:
        print(f"stock de {producto}: {stock_productos[producto]} unidades.")
    else:
        print(f"El producto '{producto}' no se encuentra en el stock.")

def agregar_unidades(producto, cantidad):
    if cantidad < 0:
        print("La cantidad a agregar no puede ser negativa.")
        return

    if producto in stock_productos:
        stock_productos[producto] += cantidad
        print(f"Se agregaron {cantidad} unidades a {producto}. Nuevo stock: {stock_productos[producto]}.")
    else:
        stock_productos[producto] = cantidad
        print(f"Producto '{producto}' nuevo, agregado con {cantidad} unidades.")

# Programa ppal
while True:
    print("\n ¿Qué desea hacer?")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades a un producto (o agregar nuevo producto)")
    print("3. Ver todo el stock")
    print("4. Salir")

    opcion = input("Ingrese el número de su opción: ")

    if opcion == '1':
        nombre_producto = input("Ingrese el nombre del producto a consultar: ")
        consultar_stock(nombre_producto)
    elif opcion == '2':
        nombre_producto = input("Ingrese el nombre del producto: ")
        try:
            cantidad_a_agregar = int(input(f"Ingrese la cantidad de unidades a agregar para '{nombre_producto}': "))
            agregar_unidades(nombre_producto, cantidad_a_agregar)
        except ValueError:
            print("Error: Ingrese una cantidad numérica válida.")
    elif opcion == '3':
        print("\nStock actual:")
        if stock_productos:
            for producto, stock in stock_productos.items():
                print(f"- {producto}: {stock} unidades")
        else:
            print("El stock está vacío.")
    elif opcion == '4':
        print("¡Hasta pronto!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 4.")
"""

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
#Permití consultar qué actividad hay en cierto día y hora. 
"""
agenda = {
    ("lunes", "9:00"): "Reunión de equipo",
    ("lunes", "19:00"): "Clase pilates",
    ("martes", "18:00"): "Turno psico",
    ("viernes", "20:00"): "Cena trabajo",
    ("miercoles", "20:00"): "Exámen programación",
    ("sabado", "21:00"): "Cena con Nico"
}

while True:
    dia_a_consultar = input("Ingrese el día de la semana (ej. lunes, martes): ")

    actividades_en_dia = []
    for (dia_agenda, hora_agenda), evento_agenda in agenda.items():
        if dia_agenda == dia_a_consultar:
            actividades_en_dia.append((hora_agenda, evento_agenda))

    if actividades_en_dia:
        for hora, evento in actividades_en_dia:
            print(f"- {hora}: {evento}")
    else:
        print(f"\nNo hay actividades programadas para el {dia_a_consultar}.")

    otra_consulta = input("\n¿Desea consultar otro día? (s/n): ")
    if otra_consulta != 's':
        print("¡Hasta pronto!")
        break
"""
# 10) Dado un diccionario que mapea nombres de países con 
# sus capitales, construí un nuevo diccionario donde:
# Las capitales sean las claves.
# Los países sean los valores. 
"""
original_paises_capitales = {
    ("Argentina"): "Buenos Aires",
    ("España"): "Madrid",
    ("Alemania"): "Berlín",
    ("Canadá"): "Ottawa",
    ("Japón"): "Tokio",
    ("Italia"): "Roma"
}


print("\nDiccionario Original (País: Capital)")
for pais, capital in original_paises_capitales.items():
    print(f"- {pais}: {capital}")

capitales_paises = {capital: pais for pais, capital in original_paises_capitales.items()}

print("\nNuevo Diccionario (Capital: País)")
for capital, pais in capitales_paises.items():
    print(f"- {capital}: {pais}")
"""