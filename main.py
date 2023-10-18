#Corte 2

#WHILE

'''
while True:
    print("Calculadora Simple")
    print("Opciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Elija una opción (1/2/3/4/5): ")

    if opcion == "5":
        print("¡Adiós!")
        break
    elif opcion in ["1", "2", "3", "4"]:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            resultado = num1 + num2
            print("El resultado de la suma es:", resultado)
        elif opcion == "2":
            resultado = num1 - num2
            print("El resultado de la resta es:", resultado)
        elif opcion == "3":
            resultado = num1 * num2
            print("El resultado de la multiplicación es:", resultado)
        elif opcion == "4":
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
            else:
                resultado = num1 / num2
                print("El resultado de la división es:", resultado)
    else:
        print("Opción no válida. Por favor, elija una opción válida (1/2/3/4/5).")

'''
########
'''
total_compras = 0  # Inicializamos el total de compras en 0

while True:
    compra = float(input("Ingrese el valor de la compra (0 para salir): "))

    if compra == 0:
        break  # Salir del bucle si el usuario ingresa 0
    elif compra < 0:
        print("El valor de la compra no puede ser negativo. Ingrese un nuevo valor.")
    else:
        total_compras += compra  # Sumar el valor de la compra al total

# Calcular el descuento si el total de compras supera $1,000,000
if total_compras > 1000000:
    descuento = total_compras * 0.10  # Calcula el 10% de descuento
    total_compras -= descuento  # Resta el descuento al total

print(f"El total a pagar es: ${total_compras:.2f}")
'''

#FOR

'''
import random

numero_aleatorio = random.randint(1, 100)
intentos_maximos = 5  # Puedes cambiar este valor según tus preferencias

print("Adivina el número entre 1 y 100.")

for intento in range(1, intentos_maximos + 1):
    intento_usuario = int(input(f"Intento {intento}/{intentos_maximos}: Ingrese su adivinanza: "))

    if intento_usuario == numero_aleatorio:
        print(f"¡Felicidades! ¡Has adivinado el número {numero_aleatorio} en {intento} intentos!")
        break
    elif intento_usuario < numero_aleatorio:
        print("El número es mayor.")
    else:
        print("El número es menor.")

else:
    print(f"Agotaste tus {intentos_maximos} intentos. El número correcto era {numero_aleatorio}. ¡Mejor suerte la próxima vez!")
  
'''
########
'''
# Solicitar al usuario ingresar un número
numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))

# Utilizar un bucle for para imprimir la tabla de multiplicar
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
'''
#########
'''
# Solicitar al usuario ingresar un número
numero = int(input("Ingrese un número para calcular su factorial: "))

# Inicializar el factorial como 1
factorial = 1

# Calcular el factorial utilizando un bucle for
for i in range(1, numero + 1):
    factorial *= i

# Mostrar el resultado
print(f"El factorial de {numero} es {factorial}")
'''
#########
'''
# Solicitar al usuario ingresar una palabra o frase
entrada = input("Ingrese una palabra o frase: ")

# Utilizar un bucle for para imprimir cada carácter
print("Caracteres en la palabra o frase:")
for caracter in entrada:
    print(caracter)
'''

#FOR-WHILE

'''
# Solicitar al usuario el nombre del archivo a leer
nombre_archivo = input("Ingrese el nombre del archivo: ")

try:
    # Intentar abrir el archivo en modo lectura
    with open(nombre_archivo, 'r') as archivo:
        # Inicializar un contador de líneas
        numero_linea = 0

        # Leer el archivo línea por línea utilizando un bucle for
        for linea in archivo:
            numero_linea += 1
            # Buscar el carácter 'x' en la línea
            if 'x' in linea:
                print(f"'x' encontrado en la línea {numero_linea}:")
                print(linea.strip())  # Mostrar la línea sin saltos de línea

except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
'''
'''
# Solicitar al usuario el nombre del archivo a leer
nombre_archivo = input("Ingrese el nombre del archivo: ")

try:
    # Intentar abrir el archivo en modo lectura
    with open(nombre_archivo, 'r') as archivo:
        # Inicializar un contador de líneas y una variable para el bucle while
        numero_linea = 0
        encontrado = False

        # Leer el archivo línea por línea utilizando un bucle while
        while True:
            linea = archivo.readline()
            if not linea:
                break  # Salir del bucle si llegamos al final del archivo
            numero_linea += 1
            # Buscar el carácter 'x' en la línea
            if 'x' in linea:
                encontrado = True
                print(f"'x' encontrado en la línea {numero_linea}:")
                print(linea.strip())  # Mostrar la línea sin saltos de línea

        if not encontrado:
            print("El carácter 'x' no fue encontrado en el archivo.")

except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
'''
########
'''
# Solicitar al usuario el nombre del archivo a leer
nombre_archivo = input("Ingrese el nombre del archivo: ")

try:
    # Intentar abrir el archivo en modo lectura
    with open(nombre_archivo, 'r') as archivo:
        # Inicializar un contador de palabras
        contador_palabras = 0

        # Leer el archivo línea por línea utilizando un bucle for
        for linea in archivo:
            # Utilizar split() para dividir la línea en palabras
            palabras = linea.split()
            # Incrementar el contador de palabras con la longitud de la lista de palabras
            contador_palabras += len(palabras)

except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {e}")

# Mostrar el número total de palabras en el archivo
print(f"El número total de palabras en el archivo es: {contador_palabras}")
'''
'''
# Solicitar al usuario el nombre del archivo a leer
nombre_archivo = input("Ingrese el nombre del archivo: ")

try:
    # Intentar abrir el archivo en modo lectura
    with open(nombre_archivo, 'r') as archivo:
        # Inicializar un contador de palabras
        contador_palabras = 0

        # Leer el archivo línea por línea utilizando un bucle while
        while True:
            linea = archivo.readline()
            if not linea:
                break  # Salir del bucle si llegamos al final del archivo

            # Utilizar split() para dividir la línea en palabras
            palabras = linea.split()
            # Incrementar el contador de palabras con la longitud de la lista de palabras
            contador_palabras += len(palabras)

except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {e}")

# Mostrar el número total de palabras en el archivo
print(f"El número total de palabras en el archivo es: {contador_palabras}")
'''
##########
'''
# Solicitar al usuario el nombre del archivo de origen y destino
nombre_archivo_origen = input("Ingrese el nombre del archivo de origen: ")
nombre_archivo_destino = input("Ingrese el nombre del archivo de destino: ")

try:
    # Abrir el archivo de origen en modo lectura
    with open(nombre_archivo_origen, 'r') as archivo_origen:
        # Leer el contenido del archivo de origen
        contenido = archivo_origen.read()

    # Abrir el archivo de destino en modo escritura
    with open(nombre_archivo_destino, 'w') as archivo_destino:
        # Escribir el contenido en el archivo de destino
        archivo_destino.write(contenido)

    print(f"Se copió el contenido de '{nombre_archivo_origen}' a '{nombre_archivo_destino}'.")

except FileNotFoundError:
    print(f"El archivo '{nombre_archivo_origen}' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
'''
'''
# Solicitar al usuario el nombre del archivo de origen y destino
nombre_archivo_origen = input("Ingrese el nombre del archivo de origen: ")
nombre_archivo_destino = input("Ingrese el nombre del archivo de destino: ")

try:
    # Abrir el archivo de origen en modo lectura
    with open(nombre_archivo_origen, 'r') as archivo_origen:
        # Abrir el archivo de destino en modo escritura
        with open(nombre_archivo_destino, 'w') as archivo_destino:
            # Leer y copiar línea por línea utilizando un bucle while
            while True:
                linea = archivo_origen.readline()
                if not linea:
                    break  # Salir del bucle si llegamos al final del archivo
                archivo_destino.write(linea)

    print(f"Se copió el contenido de '{nombre_archivo_origen}' a '{nombre_archivo_destino}'.")

except FileNotFoundError:
    print(f"El archivo '{nombre_archivo_origen}' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
'''

#LISTAS EN PYTHON

'''
Append(): adiciona un elemento a la lista
Index(): retorna el índice del elemento de la lista
Remove(): elimina un elemento de la lista
Sort(): ordena los elementos de la lista
clear(): elimina todos los elementos de la lista
copy(): arroja una copia de la lista.
count(): arroja el número de elementos con el valor
indicado.
extend(): añade los elementos de una lista (o cualquier
iterador) al final de la lista actual.
insert(): añade un elemento en la posición que se indica.
pop(): elimina el elemento de la posición que se indica.
reverse(): invierte el orden de la lista
'''
#########
'''
# Crear una lista vacía para almacenar las cadenas de caracteres
lista_original = []

# Leer 5 cadenas de caracteres por teclado y agregarlas a la lista
for i in range(5):
    cadena = input("Introduce una cadena de caracteres: ")
    lista_original.append(cadena)

# Crear una lista nueva con los elementos en orden inverso
lista_inversa = lista_original[::-1]

# Mostrar los elementos de la lista inversa por pantalla
print("Elementos en orden inverso:")
for elemento in lista_inversa:
    print(elemento)
'''
###########
'''
import random

# Inicializar una lista con 10 valores aleatorios del 1 al 10
lista = [random.randint(1, 10) for _ in range(10)]

# Mostrar cada elemento de la lista junto con su cuadrado y cubo
for elemento in lista:
    cuadrado = elemento ** 2
    cubo = elemento ** 3
    print(f"Elemento: {elemento}, Cuadrado: {cuadrado}, Cubo: {cubo}")
'''
###########
'''
# Inicializar una lista vacía para almacenar las notas
notas = []

# Leer 5 notas por teclado y agregarlas a la lista
for i in range(5):
    while True:
        try:
            nota = float(input(f"Introduce la nota {i + 1} (entre 0 y 10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("La nota debe estar entre 0 y 10. Inténtalo de nuevo.")
        except ValueError:
            print("Debes ingresar un número válido.")

# Mostrar todas las notas
print("Notas obtenidas por el alumno:")
for nota in notas:
    print(nota)

# Calcular la nota promedio
promedio = sum(notas) / len(notas)

# Encontrar la nota más alta y la menor
nota_maxima = max(notas)
nota_minima = min(notas)

# Mostrar los resultados
print(f"Nota promedio: {promedio:.2f}")
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")
'''
############
'''
# Crear una lista con los números del 1 al 10
numeros = list(range(1, 11))

# Mostrar los números en orden inverso separados por comas
numeros_inversos = reversed(numeros)  # Invierte la lista
numeros_coma = ', '.join(map(str, numeros_inversos))  # Convierte los números a cadenas y los une con comas

print(numeros_coma)
'''
############
'''
# Lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Crear una lista vacía para almacenar las asignaturas a repetir
asignaturas_a_repetir = []

# Preguntar al usuario la nota que ha sacado en cada asignatura
for asignatura in asignaturas:
    nota = float(input(f"Introduce la nota en {asignatura}: "))
    if nota < 5.0:  # Si la nota es menor que 5, se agrega a la lista de asignaturas a repetir
        asignaturas_a_repetir.append(asignatura)

# Mostrar las asignaturas a repetir
if asignaturas_a_repetir:
    print("Asignaturas que tienes que repetir:")
    for asignatura in asignaturas_a_repetir:
        print(asignatura)
else:
    print("¡Felicidades! Has aprobado todas las asignaturas.")
'''
############
'''
# Crear una lista con el abecedario
abecedario = list("abcdefghijklmnopqrstuvwxyz")

# Eliminar las letras que ocupen posiciones múltiplos de 3
abecedario_filtrado = [letra for indice, letra in enumerate(abecedario, start=1) if indice % 3 != 0]

# Mostrar la lista resultante
print(abecedario_filtrado)
'''
###########
'''
def es_palindromo(texto):
    # Eliminar espacios y convertir a minúsculas
    texto = texto.replace(" ", "").lower()
    # Reversar el texto
    texto_invertido = texto[::-1]
    # Verificar si es un palíndromo
    return texto == texto_invertido

# Pedir al usuario una palabra o frase
entrada = input("Ingresa una palabra o frase: ")

# Verificar si es un palíndromo
if es_palindromo(entrada):
    print(f"'{entrada}' es un palíndromo.")
else:
    print(f"'{entrada}' no es un palíndromo.")
'''
#############
'''
# Crear una lista con los precios
precios = [50, 75, 46, 22, 80, 65, 8]

# Encontrar el precio menor y mayor
precio_menor = min(precios)
precio_mayor = max(precios)

# Mostrar los resultados
print(f"El precio menor es: {precio_menor}")
print(f"El precio mayor es: {precio_mayor}")
'''
############
'''
# Definir los vectores como listas
vector1 = [1, 2, 3]
vector2 = [-1, 0, 2]

# Calcular el producto escalar
producto_escalar = sum(x * y for x, y in zip(vector1, vector2))

# Mostrar el resultado
print(f"El producto escalar de los vectores {vector1} y {vector2} es: {producto_escalar}")
'''
##############
'''
# Solicitar al usuario una palabra
palabra = input("Ingresa una palabra: ")

# Convertir la palabra a minúsculas para que no distinga entre mayúsculas y minúsculas
palabra = palabra.lower()

# Inicializar contadores para cada vocal
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

# Recorrer cada letra de la palabra
for letra in palabra:
    if letra == 'a':
        contador_a += 1
    elif letra == 'e':
        contador_e += 1
    elif letra == 'i':
        contador_i += 1
    elif letra == 'o':
        contador_o += 1
    elif letra == 'u':
        contador_u += 1

# Mostrar el número de veces que aparece cada vocal
print(f'Cantidad de "a" en la palabra: {contador_a}')
print(f'Cantidad de "e" en la palabra: {contador_e}')
print(f'Cantidad de "i" en la palabra: {contador_i}')
print(f'Cantidad de "o" en la palabra: {contador_o}')
print(f'Cantidad de "u" en la palabra: {contador_u}')
'''

#LISTAS DE LISTAS Y MATICES

'''
def menu():
  print ("""************
Lista de Contactos
************
Menu
1) Crear Contacto
2) Buscar Contacto
3) Eliminar Contacto
4) Mostrar Contactos
5) Salir
""")

def agregar_contacto(nombre, telefono, correo, contactos):
    contacto = [nombre, telefono, correo]
    contactos.append(contacto)

def buscar_contacto(nombre,contactos):
  for contacto in contactos:
    if contacto[0] == nombre:
        print(f"Nombre: {contacto[0]}, Teléfono: {contacto[1]}, Correo: {contacto[2]}")

def elimina_contacto(nombre,contactos):
  for contacto in contactos:
    if contacto[0] == nombre:
      contactos.pop(contactos.index(contacto))

  #print(contactos)

def Lista_contactos():
  contactos = []
  menu()
  opcion=0
  while opcion!=5:
    opcion= int(input("Selecione Opción\n"))

    if opcion == 1:
      nombrec=input("Escribe el nombre del contacto: ")
      telefonoc=input("Escribe el teléfono del contacto: ")
      correoc=input("Escribe el email del contacto: ")
      agregar_contacto(nombrec, telefonoc, correoc, contactos)

    elif opcion == 2:
      nombreb=input("Escriba el nombre del contacto que desea buscar: ")
      buscar_contacto(nombreb,contactos)

    elif opcion==3:
      nombreE=input("Escriba el nombre del contacto a eliminar: ")
      elimina_contacto(nombreE,contactos)
      
    elif opcion==4:
      print("Los contactos son: ", contactos)

    elif opcion==5:
      print("Gracias por usar la app!. bye")
      break
    
    else:
      print("Opción Invalida")
      
Lista_contactos()
'''
##########
'''
import random

def juego_cartas():  
  palos = ["Corazones", "Diamantes", "Picas", "Tréboles"]
  valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
  
  mazo = []
  
  for palo in palos:
      for valor in valores:
          carta = [valor, palo]
          mazo.append(carta)  
  
  random.shuffle(mazo)

  return mazo
  
def repartir_cartas(numero_jugadores, cartas_por_jugador):
    mazo= juego_cartas()
    jugadores = [[] for _ in range(numero_jugadores)]
    for _ in range(cartas_por_jugador):
        for jugador in jugadores:
            carta = mazo.pop()
            jugador.append(carta)

    for i, jugador in enumerate(jugadores):
        print(f"Jugador {i + 1}: {jugador}")

repartir_cartas(4,2)
'''

#MULTIPLICAR MATICES 

'''
def multiplicar_matices(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
      fila = []
      for j in range(len(matriz2[0])):
        suma = 0
        for k in range(len(matriz2)):
          suma += matriz1[i][k] * matriz2[k][j]
        fila.append(suma)
      resultado.append(fila)
    return resultado 

matriz1 = [[1,2], [3,4]]
matriz2 = [[5,6], [7,8]]
resultado = multiplicar_matices(matriz1, matriz2)
print(resultado)
'''
#CORTE 3 

'''
divisas={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
usuario = input("Hola, que divisa desea encontrar? ")

def divisaquequiereusuario():
  if usuario in divisas:
     simbolo = divisas[usuario]
     print("El símbolo de " + usuario + " es " + simbolo)
    
  else:
     print("La divisa que desea buscar no se encuentra en el diccionario.")
    
divisaquequiereusuario()
'''

#####

'''
numero = int(input("Introduce un número: "))

diccionario_cuadrados = {i: i**2 for i in range(1, numero + 1)}

print(diccionario_cuadrados)
'''

'''
range(start, stop, step)

start: El valor inicial del rango (inclusive).
stop: El valor final del rango (exclusivo).
step (opcional): El incremento entre los valores sucesivos en el rango. Si no se especifica, se asume un valor de 1.
'''