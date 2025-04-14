#Práctico 4: Estructuras repetitivas

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
"""
for i in range(101): #101 no incluído
    print (i)
"""
#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
"""
# Solicito numero al usuario sin convertir a entero para que me lo tome como string
numero = input ("Por favor ingrese un número entero: ")
# Utilizo funcion len y convierto a valor absoluto por si se ingresa un número negativo
print ("La cantidad de dígitos es", (len(str(abs(numero))))) 
"""
#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.
"""
num1 = int(input("Por favor, ingrese el primer número: "))
num2 = int(input("Por favor, ingrese el segundo número: "))

if num1 > num2:
    num1, num2 = num2, num1
#invierto los valores de las variables por si el num1 ingresado es mayor a num2
#inicializo la suma en 0
suma = 0
# como el primer número del for lo incluye y debe excluirlo le sumo 1
for x in range (num1+1,num2):
    suma += x
#    print (x) usado para verificar qué números suma

print(f"La suma de los números entre {num1} y {num2}, excluyéndolos, es: {suma}")
"""
#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
#El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
"""
sumatoria = 0 #inicializo valor de la variable
num = int(input("Por favor, ingrese un número entero ó 0 para terminar: "))

while num != 0: 
    sumatoria += num
    num = int(input("Por favor, ingrese otro número entero ó 0 para terminar: "))
print (f"La sumatoria de los números ingresados es: {sumatoria}")
"""
#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""
intentos = 1
import random
print ("Adivine el número que estoy pensando entre el 0 y el 9: ")
num = int(input("Los números por fuera del rango se tomarán como intentos: "))
num_aleatorio = random.randint(0, 9)  # Generamos el número solo una vez

while num != num_aleatorio and (num < 9 or num > 0):
    num = int(input("Incorrecto, pruebe nuevamente : "))
    intentos += 1
print (f"¡Correcto!, el número era {num_aleatorio}, y fueron necesarios {intentos} intentos")
"""
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
"""
for i in range(100,0-1,-2): # 0 menos 1 porque sino no lo incluye, de dos en dos orden decreciente
    print (i)
"""
#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
"""
num = int(input("Por favor, ingrese un número entero positivo para calcular la suma entre los números que comprenden el 0 y ese número: "))
sumatoria = 0 #inicializo valor de la variable

if num <= 0: #si se ingresa un número que no es positivo se termina el programa
    print ("Por favor, ingrese un numero positivo")
else: #inicio bloque repetitivo
    num = (num + 1) #sumo uno para que el numero ingresado sea incluído en el rango
    for i in range(0,num):
        sumatoria += i
    print (f"La sumatoria de los números es {sumatoria}")
"""
#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""
cant_num = 10 # inicializo la variable en 10 para probar programa 
# contadores
positivos = 0
negativos = 0
pares = 0
impares = 0

print (f"Ingresa {cant_num} números enteros:")

for i in range(cant_num):
# pido num por num hasta cant_num
    numero = int(input(f"Ingresa el número {i + 1}: ")) 

    # Aplicamos a contadores par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Aplicamos a contadores positivo o negativo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1



print("Resultados:")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")
"""
# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
"""
cant_num = 10 # inicializo la variable en 10 para probar programa 
sumatoria = 0 # variable que acumula la suma

print (f"Ingresa {cant_num} números enteros:")

for i in range(cant_num):
# pido num por num hasta cant_num
    num = int(input(f"Ingresa el número {i + 1}: "))
    sumatoria += num

#promedio
media = sumatoria / cant_num
print(f"La media de los números ingresados es: {media}")
"""
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int (input ("Por favor ingrese un número para realizar la inversión del mismo: "))
num_ab = abs(num) # le anulo el signo negativo por si lo tenía

invertido = 0 #inicializo variable

while num_ab > 0:
    ult_digito = num_ab % 10  # Ultimo dígito
    invertido = invertido * 10 + ult_digito  # Lo agrego al invertido
    num_ab //= 10  # Elimino el último dígito del número absoluto

# Lo presento como negativo si es que era negativo
if num < 0:
    invertido = -invertido

print(f"El número invertido es: {invertido}")