# Trabajo práctico Nº 11 de Recursividad. PROGRAMACION 1
# Alumna: Díaz de Quintana, Melisa. Comisión: 12

# 1) Crea una función recursiva que calcule el factorial de un número. 
# Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los 
# números enteros entre 1 y el número que indique el usuario 
"""
def fact_recursiva (n):
        if n == 0:
            return 1
        else:
            return n * fact_recursiva (n-1)

num = (int(input("Por favor ingrese un número: ")))
print (f"El factorial del número ingresado es: {fact_recursiva(num)}")
"""
# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique. 
"""
def fibonacci_recur(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recur(posicion-1) + fibonacci_recur(posicion-2)

num1 = (int(input("Por favor ingrese la posición a consultar: ")))
for i in range(num1):
    print (f"En la posición {i} obtenemos el valor de fibonacci {fibonacci_recur(i)}")
"""
# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente,
# utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general. 
"""
def pot_recur(n, m):
    if m == 0:  #Caso base // tood num elevado a la 0 da 1
        return 1
    else:
        return n * pot_recur(n, m - 1)  


b = int(input("Ingrese la base: "))
exp = int(input("Ingrese el exponente: "))
resultado = pot_recur(b, exp)
print(f"{b} elevado a {exp} es: {resultado}")
"""
# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
# y devuelva su representación en binario como una cadena de texto. 
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y unos (1), en base 2. 
# Para convertir un número decimal a binario, se puede seguir este procedimiento: 
# 1. Dividir el número por 2. 
# 2. Guardar el resto (0 o 1). 
# 3. Repetir el proceso con el cociente hasta que llegue a 0. 
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario. 
"""
def recur_binario(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return str(recur_binario(n // 2)) + str(n % 2)
    
num = int(input("Ingrese un número decimal positivo para convertir a binario: "))
print (f"El número decimal {num} equivale a {recur_binario(num)} en binario")
"""
# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes,
# devuelva True si es un palíndromo o False si no lo es.      
# Requisitos: La solución debe ser recursiva. No se debe usar [::-1] ni la función reversed().
"""
def es_palindromo(palabra):
    if len(palabra) <= 1: #Caso base // si tiene una letra es palíndromo
        return True
    if palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

palabra = (input("Ingrese una palabra para saber si es palíndromo: "))
print (f"La palabra ingresada ¿es palíndromo?: {es_palindromo(palabra)}")
""" 
# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y 
# devuelva la suma de todos sus dígitos.      
# Restricciones: No se puede convertir el número a string. # Usá operaciones matemáticas (%, //) y recursión. 
# Ejemplos: 
# suma_digitos(1234)   → 10  
# (1 + 2 + 3 + 4) suma_digitos(9)      → 9 
# suma_digitos(305)    → 8   (3 + 0 + 5) 
"""
def suma_digitos(n):
    if n < 10: # Caso base. Si tiene un dígito no hay suma, es = al dígito.
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)
    

n=int(input("Por favor, ingrese un número entero positivo para sumar sus dígitos: "))
print (f"La suma de los dígitos de {n} es {suma_digitos(n)}")
"""
# 7) Un niño está construyendo una pirámide con bloques. 
# En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), 
# y así sucesivamente hasta llegar al último nivel con un solo bloque.  
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo 
# y devuelva el total de bloques que necesita para construir toda la pirámide.        
# Ejemplos: 
# contar_bloques(1)   → 1         (1) 
# contar_bloques(2)   → 3         (2 + 1) 
# contar_bloques(4)   → 10        (4 + 3 + 2 + 1)  
"""
def contar_bloques(n):
    if n == 1:  # Caso base. Si el último nivel tiene 1 bloque, es sólo 1
        return 1
    else:
        return n + contar_bloques(n - 1)

num=int(input("Ingrese la cantidad de bloques del nivel inferior para calcular el total necesario: "))
print(f"Se necesitan {contar_bloques(num)} bloques para construir toda la pirámide.")
"""
#8) Escribí una función recursiva llamada contar_digito(numero, digito) 
# que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), 
# y devuelva cuántas veces aparece ese dígito dentro del número.       
# Ejemplos: 
# contar_digito(12233421, 2)   → 3   
# contar_digito(5555, 5)       → 4   
# contar_digito(123456, 7)     → 0   
"""
def contar_digito(numero, digito):
    if numero == 0:  # Caso base. Si se reduce a 0, es 0.
        return 0
    else:
        ultimo_digito = numero % 10 #Comparo ultimo digito con el buscado
        if ultimo_digito == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

n=int(input("Ingrese un número entero positivo: "))
d=int(input("Ingrese el dígito que desea buscar en ese número: "))
print (f"El dígito {d} aparece {contar_digito(n, d)} vez/veces en el número dado")
"""

def mystery(n):
    if n<=1:
        return n
    return mystery(n-1)+mystery(n-2)

print (mystery(4))