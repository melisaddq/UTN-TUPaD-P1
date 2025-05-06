# Trabajo práctico Nº 5 de Funciones. PROGRAMACION 1
# Alumna: Díaz de Quintana, Melisa. Comisión: 12

#1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. 
# Llamar a esta función desde el programa principal.
"""
# definición de funciones:
def imprimir_hola_mundo():
    print("Hola Mundo!") #instrucción

# Programa principal:
imprimir_hola_mundo()
"""
#  2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. 
# Por ejemplo, si se llama con saludar_usuario("Marcos"), # deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa 
# principal solicitando el nombre al usuario. 
"""
# definición de funciones: 
def saludar_usuario(nombre):
    print (f"Hola {nombre}!") #Instrucción

# Programa principal: 
nombre = input ("Por favor, ingrese su nombre: ") 
saludar_usuario(nombre)
"""
# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: 
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.
"""
# definición de funciones:
def informacion_personal (n, a, e, r):
    print (f"Soy {n} {a}, tengo {e} años y vivo en {r}.")

# Programa principal
print("Por favor, ingrese los siguientes datos personales: ")
nombre = input("Nombre: ") 
apellido = input("Apellido: ") 
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)
"""
# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados. 
"""
import math # importo librería para utilizar PI por fuera de las funciones

# Definición de funciones:

def calcular_area_circulo (radio):
    return math.pi*(radio**2) #Area = pi x radio al cuadrado

def calcular_perimetro_circulo(radio):
    return (2*math.pi*radio) #Perímetro = 2 x pi x radio

def es_entero(mensaje):
    while True:
        entrada = input(mensaje) 
        if entrada.isdigit(): # Verificación de que el input sea un numero entero
            return int(entrada)
        else:
            print("ERROR. Por favor, ingrese un número entero.")

# Programa principal:
radio = es_entero ("Por favor, ingrese el radio del círculo para calcular su área y perímetro: ")
print (f"El área del círculo es {calcular_area_circulo(radio)} y el perímetro es {calcular_perimetro_circulo(radio)}")
"""
# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva 
# la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función. 
"""
# Definición de funciones:

def segundos_a_horas(segundos):
    return (segundos // 3600)

def es_entero(mensaje): #Reutilizo función del ejercicio anterior
    while True:
        entrada = input(mensaje) 
        if entrada.isdigit(): # Verificación de que el input sea un numero entero
            return int(entrada)
        else:
            print("ERROR. Por favor, ingrese un número entero.")

# Programa principal:
segundos = es_entero("Por favor, ingrese los segundos que desea convertir a horas: ") 
print (segundos_a_horas(segundos))
"""
# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar 
# de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.
"""
# Definición de funciones:

def tabla_multiplicar(mensaje):
    entrada = int(input(mensaje))
    resultado = "" #Inicializo la variable como str porque luego la utilizo como tal
    for i in range(1, 11):  # del 1 a 10
        resultado += f"{entrada} X {i} = {entrada * i}\n"
    return resultado

# Programa principal: 
print (tabla_multiplicar("Por favor, ingrese el número del cual precisa saber la tabla del 1 al 10: "))
"""
# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el 
# resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara. 
"""
# Definición de funciones:

def operaciones_basicas(a,b):
    s = a + b
    r = a - b
    m = a * b
    d = a / b if b != 0 else "No se puede dividir por cero"
    return (s, r, m, d)

# Programa principal:
print ("Vamos a calcular las operaciones básicas de dos números")
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

resultado = operaciones_basicas(a, b)

print("Resultados de las operaciones básicas:") #ordenados
print(f"Suma: {resultado[0]}")
print(f"Resta: {resultado[1]}")
print(f"Multiplicación: {resultado[2]}")
print(f"División: {resultado[3]}")
"""
# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, 
# y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado 
#  dos decimales. 
"""
# Definición de funciones:
def calcular_imc(peso,altura):
    return peso/(altura**2)

# Programa principal:
peso = int(input("Por favor, ingrese su peso en kilogramos: "))
altura = float(input("Por favor, ingrese su altura en metros: "))
print (f"Tu IMC (índice de masa corporal) es {calcular_imc(peso,altura)}")
"""
# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y 
# devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función. 
"""
# Definición de funciones:
def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius*(9/5)+32
    return (f"Los grados celsius ingresados son {fahrenheit}º Fahrenheit")
# Programa principal:
print (celsius_a_fahrenheit (int(input("Por favor, ingrese la temperatura en grados Celsius para convertir a Fahrenhet: "))))
"""
# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. 
# Solicitar los números al usuario y mostrar el resultado usando esta función.
"""
# Definición de funciones:
def calcular_promedio (a, b, c):
    return (a+b+c)/3

# Programa principal:
print ("Vamos a calcular el promedio de tres números")
a = (int(input("Por favor, ingrese el primer número: ")))
b = (int(input("Por favor, ingrese el segundo número: ")))
c = (int(input("Por favor, ingrese el tercer número: ")))
print (calcular_promedio(a,b,c))
"""

def saludo(nombre):
    return f"Hola, {nombre}!"

print(saludo("Ana"))