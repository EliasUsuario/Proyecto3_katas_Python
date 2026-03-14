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
    return " ".join(map(str, tupla))# Convierto cada elemento a string y los uno con un espacio

datos = [("Perico", "Palotes"), ("Holaquetal", 9.99), ("Estudiante", "The_Power")]
resultado_iterador = map(tupla_a_string, datos)# Se usa map para transformar cada tupla de la lista con la función 'tupla_a_string'.
lista_strings = list(resultado_iterador)# Se convierte el resultado a una lista para poder mostrarlo.

print(f"Lista de tuplas original: {datos}")
print(f"Lista de strings resultante: {lista_strings}")






