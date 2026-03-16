from functools import reduce


# 1- Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. 
    # Los espacios no deben ser considerados.
def contar_frecuencias(cadena):
    frecuencias = {}
    
    for caracter in cadena: # Verifica que no sea un espacio
        if caracter != " ": # Si la letra ya está en el diccionario se suma 1, si no se inicializa en 1
            if caracter in frecuencias:
                frecuencias[caracter] += 1
            else:
                frecuencias[caracter] = 1
    return frecuencias

# Ejemplo de uso:
texto = "hola mundo"
resultado = contar_frecuencias(texto)
print(resultado)

#2- Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().
def duplicar(n):
    return n * 2
numeros = [1, 2, 3, 4, 5] # Lista de entrada para la prueba

    # Aplico la función 'duplicar' a cada elemento de la lista 'numeros'
    # map() devuelve un objeto iterable, así que lo convierto a lista con list()
resultado = list(map(duplicar, numeros))

print(f"Lista original: {numeros}")
print(f"Lista duplicada: {resultado}")

#3- Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
    # La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def filtrar_por_objetivo(lista_palabras, objetivo):
    coincidencias = []
    for palabra in lista_palabras:
        if objetivo in palabra: # Si hay coincidencia, la añado a mi lista de resultados
            coincidencias.append(palabra)
    return coincidencias

# Ejemplo de uso:
mis_palabras = ["estas", "son", "varias", "palabras", "de", "ejemplo"]
busqueda = "var"
resultado = filtrar_por_objetivo(mis_palabras, busqueda)# Llamada a la función
print(f"Lista original: {mis_palabras}")
print(f"Palabra objetivo: '{busqueda}'")
print(f"Resultado del filtro: {resultado}") # varias

#4- Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().
def restar(a, b):
    return a - b # Devuelve la diferencia entre el primer y el segundo número

lista_a = [10, 20, 30, 40]
lista_b = [3, 5, 10, 25]

resultado_objeto = map(restar, lista_a, lista_b)# Paso la función 'restar' y ambas listas al map

diferencias = list(resultado_objeto)# Convierto el iterador resultante en una lista para poder imprimirlo

print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")
print(f"Diferencias: {diferencias}")

#5- Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). 
    # La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. 
    # Si es así, el estado será "aprobado"; de lo contrario, "suspenso". 
    # La función debe devolver una tupla que contenga la media y el estado.
def evaluar_rendimiento(notas, nota_aprobado=5):
    if not notas:
        return (0, "suspenso") # Si la lista está vacía, evito el error de división por cero
    media = sum(notas) / len(notas) # Calculo la suma total y la divido por la cantidad de elementos
    if media >= nota_aprobado:  # Determino el estado según la comparación con nota_aprobado
        estado = "aprobado"
    else:
        estado = "suspenso"
    return (media, estado)# Devuelvo ambos valores en una tupla

# Pruebas para validar el funcionamiento
mis_notas = [7, 8, 4, 9, 6]

# Prueba con el valor por defecto (5)
resultado_1 = evaluar_rendimiento(mis_notas)
# Prueba cambiando el aprobado a un 7
resultado_2 = evaluar_rendimiento(mis_notas, 7)

print(f"Notas: {mis_notas}")
print(f"Resultado con aprobado en 5: {resultado_1}")
print(f"Resultado con aprobado en 7: {resultado_2}")

#6- Escribe una función que calcule el factorial de un número de manera recursiva.
def calcular_factorial(n):
    # *Lo que más me costó entender es que si no pongo esto, la función se llama infinitamente. 
    # Si n es 0 o 1, el factorial es 1.
    if n <= 1:
        return 1
    else:
        return n * calcular_factorial(n - 1) # Multiplico el número actual por el factorial del anterior.

# Pruebas de funcionamiento
numero = 5
resultado = calcular_factorial(numero)

print(f"El factorial de {numero} es: {resultado}")
# Probando con un caso simple para verificar
print(f"El factorial de 3 es: {calcular_factorial(3)}") # Debería ser 6 (3 * 2 * 1)

#7- Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().
def tupla_a_string(tupla):
    return " ".join(map(str, tupla))# Convierto cada elemento a string y los uno con un espacio.

datos = [("Perico", "Palotes"), ("Holaquetal", 9.99), ("Estudiante", "The_Power")]
resultado_iterador = map(tupla_a_string, datos)# Se usa map para transformar cada tupla de la lista con la función 'tupla_a_string'.
lista_strings = list(resultado_iterador)# Se convierte el resultado a una lista para poder mostrarlo.

print(f"Lista de tuplas original: {datos}")
print(f"Lista de strings resultante: {lista_strings}")

'''
#8- Escribe un programa que pida al usuario dos números e intente dividirlos. 
    # Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada 
    # y muestra un mensaje indicando si la división fue exitosa o no.
def division_dos_numeros():
    try:
        numerador = float(input("Introduce el primer número (dividendo): "))# Pido los datos y los convierto a float.
        denominador = float(input("Introduce el segundo número (divisor): "))# Pido los datos y los convierto a float.

        resultado = numerador / denominador # Se intenta realizar la operación

    except ValueError:# Este error salta si el usuario escribe letras en lugar de números
        print("Error: ¡Debes introducir un valor numérico válido!")
        print("La división no fue exitosa.")
        
    except ZeroDivisionError: # Este error salta si el denominador es 0
        print("Error: No se puede dividir entre cero.")
        print("La división no fue exitosa.")
        
    else: # El bloque 'else' solo se ejecuta si NO hubo ninguna excepción
        print(f"¡División exitosa! El resultado es: {resultado}")
        
    finally: # Esto se ejecuta siempre, haya error o no
        print("Fin del proceso de división.")

# Ejecuto la función
division_dos_numeros()
'''
#9- Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva 
    # una nueva lista excluyendo ciertas mascotas prohibidas en España. 
    # La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. 
    # Usa la función filter().

def es_mascota_permitida(mascota):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return mascota not in prohibidas # Compruebo si la mascota no está en la lista negra con 'not in'.

mis_mascotas = ["Perro", "Mapache", "Gato", "Oso", "Canario", "Tigre"]# Lista de mascotas que queremos revisar
resultado_filtrado = filter(es_mascota_permitida, mis_mascotas)# Uso filter() para aplicar la regla de validación a toda la lista

mascotas_legales = list(resultado_filtrado)# Convierto el iterador de filter a una lista real para poder usarla

print(f"Lista completa: {mis_mascotas}")
print(f"Lista de mascotas permitidas: {mascotas_legales}")


#10- Escribe una función que reciba una lista de números y calcule su promedio. 
    # Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

class ListaVaciaError(Exception): #Excepción lanzada cuando la lista de números no tiene elementos.
    pass
def calcular_promedio(numeros):# Verifico si la lista tiene elementos usando len()
    if len(numeros) == 0:
        raise ListaVaciaError("No se puede calcular el promedio de una lista vacía.") # Si está vacía, "lanzo" el error manualmente con raise
    return sum(numeros) / len(numeros) # Si hay datos, calculo el promedio normal

# Bloque de prueba para validar el manejo del error
listas_a_probar = [[10, 20, 30], [], [5, 15, 25]]

for lista in listas_a_probar:
    try:
        print(f"Procesando lista: {lista}")
        resultado = calcular_promedio(lista)
        print(f"El promedio es: {resultado}")
    except ListaVaciaError as e: # Capturo mi error personalizado y muestro el mensaje que definí arriba
        print(f"Error detectado: {e}")
'''
#11- Escribe un programa que pida al usuario que introduzca su edad. 
    # Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), 
    # maneja las excepciones adecuadamente.

class EdadFueraDeRangoError(Exception): #Excepción para edades menores de 0 y mayores de 120.
    pass

def pedir_edad(): #Solicita la edad al usuario y valida que sea un número entre 0 y 120.
    while True:
        try:
            entrada = input("Por favor, introduce tu edad: ")
            edad = int(entrada)
            if edad < 0 or edad > 120: # Comprobamos el rango solicitado, si está fuera de rango, lanzamos nuestra propia excepción
                raise EdadFueraDeRangoError(f"La edad {edad} no es válida. Debe estar entre 0 y 120.")
            print(f"Edad registrada correctamente: {edad}")# Si todo ha ido bien, saldrá del bucle
            break
            
        except ValueError:# Se activa si el usuario introduce texto o decimales
            print("Error: ¡Debes introducir un número entero!")
        except EdadFueraDeRangoError as e:# Se activa si el número es válido pero está fuera de rango
            print(f"Error: {e}")
        print("Inténtalo de nuevo.\n")

# Ejecución del programa
pedir_edad()

#12- Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().
def medir_palabras(frase):
    palabras = frase.split()# Divido la frase por los espacios para obtener una lista de palabras con.split()
    resultado_map = map(len, palabras)# Uso map para aplicar la función len a cada elemento de la lista 'palabras'
    return list(resultado_map)# Convierto el iterador a una lista para poder devolverlo

# Prueba del programa
texto = input("Introduce una frase: ")
resultado = medir_palabras(texto)

print(f"Frase original: '{texto}'")
print(f"Longitudes: {resultado}")
'''

#13- Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. 
    # Las letras no pueden estar repetidas. Usa la función map().

def transformar_a_tuplas(caracteres): # Elimino duplicados convirtiendo la entrada a un set.

    caracteres_unicos = set(caracteres)
    def crear_tupla(letra):
        return (letra.upper(), letra.lower()) # Devuelvo la tupla con las dos versiones de la letra.
    resultado_iterador = map(crear_tupla, caracteres_unicos) # Uso map para aplicar la transformación a cada carácter único.
    return list(resultado_iterador) # Convierto el resultado a una lista como pide el enunciado.

# Ejemplo de prueba con letras repetidas y desordenadas.
entrada_datos = ['a', 'a', 'a', 'z', 'B', 'K', 'c', 'm', 'd']
resultado = transformar_a_tuplas(entrada_datos)

print(f"Entrada original: {entrada_datos}")
print(f"Resultado (Tuplas sin repetir): {resultado}")

#14- Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().

def filtrar_por_inicial(lista_palabras, letra_especifica):
    letra_especifica = letra_especifica.lower() # Paso la letra objetivo a minúscula para facilitar la comparación

    def empieza_con(palabra):# Verifico que la palabra no esté vacía para evitar errores de índice
        if len(palabra) == 0:
            return False
        
        # Accedo al primer carácter mediante el índice [0] y lo comparo en minúsculas
        return palabra[0].lower() == letra_especifica
    resultado_iterador = filter(empieza_con, lista_palabras)# Uso filter() para la comprobación
    return list(resultado_iterador)

# Datos de prueba
animales = ["Perro", "gato", "Pájaro", "Elefante", "Pez"]
letra = "p"

# Ejecución
resultado = filtrar_por_inicial(animales, letra)

print(f"Lista original: {animales}")
print(f"Palabras que empiezan por '{letra}': {resultado}")


#15- Crea una función lambda que sume 3 a cada número de una lista dada.
numeros = [10, 20, 30, 40, 50]
resultado_objeto = map(lambda x: x + 3, numeros)# Uso map() junto con una función lambda
resultado_lista = list(resultado_objeto)# Convierto el resultado a lista para poder visualizarlo

print(f"Lista original: {numeros}")
print(f"Lista tras sumar 3: {resultado_lista}")

#16- Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().
def filtrar_palabras_largas(texto, n):

    palabras = texto.split()# Conversion del texto en una lista de palabras.
    def es_larga(palabra): # Solo se devuelve True si la longitud de la palabra supera n
        return len(palabra) > n

    resultado_iterador = filter(es_larga, palabras)
    return list(resultado_iterador)

# Ejemplo de prueba
frase_ejemplo = "Esta es una frase que he puesto de ejemplo"
longitud_minima = 4

resultado = filtrar_palabras_largas(frase_ejemplo, longitud_minima)

print(f"Texto original: '{frase_ejemplo}'")
print(f"Palabras con más de {longitud_minima} caracteres: {resultado}")

#17- Crea una función que tome una lista de dígitos y devuelva el número correspondiente. 
    # (Por ejemplo, [5,7,2] corresponde al número 572). Usa la función reduce().

def lista_a_numero(digitos):
    def combinar(acumulado, siguiente): # Se define la función con "acumulado" (lo calculado hasta ahora) y "siguiente" (el nuevo dígito que vamos a procesar)
        return (acumulado * 10) + siguiente # Desplazamos el acumulado una posición a la izquierda (x10) y sumamos el nuevo dígito.
    resultado = reduce(combinar, digitos) # Aplicamos reduce para "reducir" la lista a un solo valor
    return resultado

# Pruebas de funcionamiento
mi_lista = [5, 7, 2]
numero_final = lista_a_numero(mi_lista)

print(f"Lista original: {mi_lista}")
print(f"Número resultante: {numero_final}")

#18- Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación).
    # y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.

def filtrar_estudiantes(lista_estudiantes):
    def calificacion_alta(estudiante):
        return estudiante['calificación'] >= 90 # Acceso al valor de la clave 'calificación' del diccionario y comprobación de si cumple la condición.
    estudiantes_filtrados = filter(calificacion_alta, lista_estudiantes)# Uso de filter() para aplicar la regla a cada diccionario de la lista.

    
    return list(estudiantes_filtrados)# Convierto el resultado a una lista para poder trabajar con ella.

# Datos de prueba con una lista de diccionarios:
estudiantes = [
    {"nombre": "Elías", "edad": 42, "calificación": 95},
    {"nombre": "Pepe", "edad": 32, "calificación": 88},
    {"nombre": "Yomismo", "edad": 44, "calificación": 92},
    {"nombre": "Juanito", "edad": 21, "calificación": 75},
    {"nombre": "Susan", "edad": 20, "calificación": 90}
]

# Ejecución de la función
mejores_estudiantes = filtrar_estudiantes(estudiantes)

print("Lista de Estudiantes con calificación mayor o igual a 90")
for e in mejores_estudiantes:
    print(f"Nombre: {e['nombre']}, Calificación: {e['calificación']}")


#19- Crea una función lambda que filtre los números impares de una lista dada.
numeros_variados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Lista de números inicial para la prueba

impares = filter(lambda x: x % 2 != 0, numeros_variados) # La lambda recibe 'x' y devuelve True si el resto de x/2 no es 0 (1 = True).
resultado_lista = list(impares) # Convierto el resultado a lista para poder imprimirlo

print(f"Lista completa: {numeros_variados}")
print(f"Números impares: {resultado_lista}")

#20- Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().
def filtrar_enteros(lista_mixta):
    def es_entero(elemento):# Función de comprobación
        return type(elemento) == int # Comparo el tipo del elemento 'int' con type(así obtengo el tipo del elemento).
    solo_enteros = filter(es_entero, lista_mixta)
    return list(solo_enteros)

# Datos de prueba con mezclas
datos = [10, "Prueba", 5, "Hola", 22, "30", True]

# Ejecución
resultado = filtrar_enteros(datos)

print(f"Lista original: {datos}")
print(f"Solo valores enteros: {resultado}")

#21- Crea una función que calcule el cubo de un número dado mediante una función lambda.
calcular_cubo = lambda x: x ** 3 # x**3 es equivalente a x * x * x

# Datos de prueba
numero = 4
resultado = calcular_cubo(numero)
print(f"El cubo de {numero} es: {resultado}")

#22- Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().
def calcular_producto_total(numeros):
    producto = reduce(lambda x, y: x * y, numeros)# 'x' es el acumulado (se multiplica por el siguiente), 'y' es el valor actual de la lista
    return producto

# Datos de prueba
mi_lista = [2, 3, 4, 5] # El resultado debería ser 120 (2*3*4*5)

resultado = calcular_producto_total(mi_lista)

print(f"Lista de números: {mi_lista}")
print(f"El producto total es: {resultado}")

#23- Concatena una lista de palabras. Usa la función reduce(). 











'''
Ejercicios comentados hasta aquí (para no tener que usar el input cada vez que lo ejecuto): 8, 11, 12
'''


