# Práctico 3: Estructuras condicionales / Alumna: Díaz de Quintana, Melisa

#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
"""
edad = input ( "Por favor, introduzca su edad: ") 
if int(edad) > 18:
    print("Es mayor de edad")
"""
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.
"""
nota = input ( "Por favor, introduzca su nota: ")
if int(nota) >= 6:
    print("Aprobado")
else: print ("Desaprobado")
"""
#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.
"""
num1 = input ( "Por favor, introduzca un número par: ")
num1=int(num1)
if num1 % 2 == 0:
    print ("Ha ingresado un número par")
else:
    print ("Por favor, ingrese un número par")
"""
#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.
"""
edad = input ( "Por favor, introduzca su edad: ")
edad=int(edad)
if edad < 12:
    print ("Es un/a niño/a")
elif edad >= 12 and edad < 18:
    print ("es un/a adolescente")
elif edad >= 18 and edad < 30:
    print ("es un/a adulto/a joven")
else:
    print ("es un adulto/a")
"""
#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string. 
"""
contraseña = input ( "Por favor, introduzca una contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print ("Ha ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
"""
#6) Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Sesgo positivo o a la derecha: cuando la media MEDIAN es mayor que la mediana mean y, a su vez, la
#mediana es mayor que la moda MODE.
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
#la mediana es menor que la moda.
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.
"""
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
from statistics import mode, median, mean
#print (numeros_aleatorios) utilizado para verificar que sean distintos porque me daba siempre el mismo resultado
mediana=mean(numeros_aleatorios)
moda=mode(numeros_aleatorios)
media=median(numeros_aleatorios)
if media > mediana and media > moda:
    print ("Sesgo positivo o a la derecha")
elif media < mediana and media < moda:
    print ("Sesgo negativo o a la izquierda")
else:
    print ("sin sesgo") 
"""
#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.
"""
def palabra_frase (): str
palabra_frase = input ( "Por favor, introduzca una palabra o frase: ")
vocales = "aeiouAEIOU"
if palabra_frase[-1].lower() in vocales:
    print (palabra_frase + "!")
else:
    print (palabra_frase)
"""
#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.
"""
nombre = input ("Por favor, ingrese su nombre: ")
print ( "Ingrese 1. Si quiere su nombre en mayúsculas, ")
print ("ingrese 2 Si quiere su nombre en minúsculas, ó")
print ("ingrese 3 si quiere su nombre con la primera letra mayúscula.")
num1 = input ("Por favor, ingrese el número el número de la opción deseada: ")
if num1 == 1:
    print (nombre.upper())
elif num1 == 2:
    print (nombre.lower())
else:
    print (nombre.title())
"""

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes 
# categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
"""
magnitud = input ("Por favor, ingrese la magnitud del terremoto: ")
magnitud = float(magnitud)
if magnitud < 3:
    print ("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print ("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
        print ("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
     print ("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
     print ("Muy Fuerte (puede causar daños significativos)")
else:
    print ("Extremo (puede causar graves daños a gran escala)")
"""
#10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
#El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño,
#invierno, primavera o verano.
#HEMISFERIONORTE
#Desde el 21 de diciembre hasta el 20 demarzo (incluidos) INVIERNO
#Desde el 21 de marzo hasta el 20 de junio (incluidos) PRIVAMERA
#Desde el 21 de junio hasta el 20 de septiembre (incluidos) VERANO
#Desde el 21 de septiembre hasta el 20 de diciembre (incluidos) OTOÑO
"""
hemisferio = input ( "Por favor, introduzca Norte o Sur según el hemisferio en el que se encuentre (N/S): ").upper()
dia = input ( "Por favor, introduzca qué día del mes es: ")
mes = input ( "Por favor, introduzca el mes: ")
mes=int(mes)
dia = int(dia)
if hemisferio == "N":
    if mes == 1 or mes == 2: 
        print ("Es invierno")
    elif mes == 4 or mes == 5: 
        print ("Es primavera")
    elif mes == 7 or mes == 8: 
        print ("Es verano")
    elif mes == 10 or mes == 11: 
        print ("Es otoño")
    if mes == 3 and dia <= 20: 
        print ("es invierno") 
    elif mes == 3 and dia > 20: 
        print("es primavera")
    elif mes == 12 and dia <= 20: 
        print ("es otoño") 
    elif mes == 12 and dia > 20: 
        print ("Es invierno")
    elif mes == 6 and dia <= 20: 
        print ("Es primavera") 
    elif mes == 6 and dia > 20: 
        print ("Es verano")
    elif mes == 9 and dia <= 20: 
        print ("Es verano") 
    elif mes == 9 and dia > 20: 
        print ("Es otoño")
if hemisferio == "S":
    if mes == 1 or mes == 2: 
        print ("Es verano")
    elif mes == 4 or mes == 5: 
        print ("Es otoño")
    elif mes == 7 or mes == 8: 
        print ("Es invierno")
    elif mes == 10 or mes == 11: 
        print ("Es primavera")
    if mes == 3 and dia <= 20: 
        print ("es verano") 
    elif mes == 3 and dia > 20: 
        print("es otoño")
    elif mes == 12 and dia <= 20: 
        print ("es primavera") 
    elif mes == 12 and dia > 20: 
        print ("Es verano")
    elif mes == 6 and dia <= 20: 
        print ("Es otoño") 
    elif mes == 6 and dia > 20: 
        print ("Es invierno")
    elif mes == 9 and dia <= 20: 
        print ("Es invierno") 
    elif mes == 9 and dia > 20: 
        print ("Es primavera")
"""