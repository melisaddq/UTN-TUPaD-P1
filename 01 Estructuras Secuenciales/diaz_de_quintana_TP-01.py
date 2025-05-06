# Trabajo práctico Nº1 - Melisa Díaz de Quintana

#Ejercicio 1
print("Hola mundo!")

#Ejercicio 2
nombre = input("Por favor, ingresa tu nombre: ")
print(f"Hola, ¨{nombre} !")

#Ejercicio 3 // nombre, apellido, edad y lugar de residencia
nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Ahora ingresa tu apellido: ")
edad = input("Bien, ¿me dirías tu edad?: ")
residencia = input("Gracias, finalmente, ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ejercicio 4
print ("Vamos a calcular el área y el perímetro de un círculo")
radio = float (input("Por favor, ingresa el radio: "))
perimetro= 2 * (3.14159) * radio
area= (3.14159) * radio ** 2
print (f"El área y el perímetro del cículo para radio = {radio} son {area} y {perimetro} respectivamente.")

#Ejercicio 5 
segundos = int(input ("Por favor, ingresa la cantidad de segundos que quieres convertir a horas: "))
horas = int(segundos//3600)
print (f"{segundos} segundos equivale a {horas} horas.")

#Ejercicio 6 
num = int(input("Por favor, ingresa un número para ofrecerte su tabla de multiplicar: "))
print (f"La tabla de multiplicar en orden del 1 al 10 de {num} es: {num*1}, {num*2}, {num*3}, {num*4}, {num*5}, {num*6}, {num*7}, {num*8}, {num*9}, {num*10}.")

#Ejercicio 7 
print("Vamos a realizar las operaciones básicas entre dos números")
num1=int(input("Ingresa el primer número: "))
num2=int(input("Ingresa el segundo número: "))
print (f"El resultado de la suma es {num1+num2}")
print (f"El resultado de la resta es {num1-num2}")
print (f"El resultado de la multiplicación es {num1*num2}")
print (f"El resultado de la división es {num1/num2}")

#Ejercicio 8 Crear un programa que pida al usuario su altura y su peso 
# e imprima por pantalla su índice de masa corporal
print ("¡Vamos a calcular tu índice de masa corporal!")
altura= float(input ("Por favor, ingrese su altura en metros: "))
peso= float(input ("Ahora ingrese su peso en Kg: "))
print (f"Su índice de masa corporal o IMC es de {peso/altura**2}")

#Ejercicio 9 Crear un programa que pida al usuario una temperatura 
#en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
print ("Vamos a convertir la temperatura de grados Celsius a Fahrenheit")
celsius= float(input("Por favor, ingrese la temperatura en grados celsius: "))
print (f"{celsius}º celsius son {(9/5*celsius) + 32}º fahreinheit")

#Ejercicio 10. Crear un programa que pida al usuario 3 números 
# e imprima por pantalla el promedio de dichos números.
print ("Vamos a calcular el promedio entre tres números")
num1=float(input("Por favor, ingrese el primer número: "))
num2=float(input("Por favor, ingrese el segundo número: "))
num3=float(input("Por favor, ingrese el tercer número: "))
promedio=(num1+num2+num3)/3
print (f"El promedio de los números ingresados es {promedio}")