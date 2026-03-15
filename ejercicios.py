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

'''
Ejercicios comentados hasta aquí (para no tener que usar el input cada vez): 8, 11, 12
'''






