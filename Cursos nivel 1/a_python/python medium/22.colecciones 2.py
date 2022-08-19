#C I C L O S    F O R (.ZIP)(UNIR +2 COLECCIONES PERO DE MANERA agrupada(en tuplas) o alternada)
#LISTAS
lista1 = [1, 3, 5, 7, 9]
lista2 = [2, 4, 6, 8, 10]
#se pueden zipear mas de 2 listas
#CREAR LA LISTA DIRECTAMENTE CON ZIP
lista_zipeada = [] #la lista en donde meteremos las tuplas de cada i esimo elemento de ambas listas
for elemento_zipeado in zip(lista1, lista2): #esto crea: [(lista1[0],lista2[0]), (lista1[1],lista2[1])... (lista1[n], lista2[n])]
    lista_zipeada.append(elemento_zipeado) #cada elemento es: (lista1[i], lista2[i]) una tupla
print('Lista a partir de listas: {}'.format(lista_zipeada))
# Lista a partir de listas: [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
lista_zipeada = list(zip(lista1, lista2))
print('Lista a partir de listas(rapido): {}'.format(lista_zipeada))

#esto aparece como una lista con cada elemento como una tupla con la union de los 2 elementos del mismo indice de las listas
#esto quiere decir que los elementos zipeados con hata el indice maximo(de la lista con menos elementos)

#ZIP PARA ALTERNAR ELEMENTOS
lista_unida_alternadamente = [] #aca uniremos los elementos, sacandolos de las listas (porque quiero y puedo)
for elemento_1, elemento_2 in zip(lista1, lista2): #esto crea la misma lista de arriba donde cada tupla se desempaqueta con (x, y)
    lista_unida_alternadamente.append(elemento_1) # este es lista1[i]   (el primer elemento x me lo traigo aca)
    lista_unida_alternadamente.append(elemento_2) # este es lista2[i] (y el segundo elemento y me lo traigo aca)
print('Lista a partir de listas: {}'.format(lista_unida_alternadamente))
# Lista a partir de listas: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#esto nos sirve para tener mas control en los elementos con: desempaquetando tuplas

#__________________
#TUPLAS
tupla1 = (1, 3, 5, 7, 9)
tupla2 = (2, 4, 6, 8, 10)
#se pueden zipear más de 2 tuplas
#CREAR LA LISTA DIRECTAMENTE CON ZIP
lista_zipeada = [] #donde meteremos las tuplas que se crean a partir de los pares de los elementos i esimos de cada una
for elemento_zipeado in zip(tupla1, tupla2): #esto crea: [(tupla1[0],tupla2[0]), (tupla1[1],tupla2[1])... (tupla1[n], tupla2[n])]
    lista_zipeada.append(elemento_zipeado) #cada elemento es: (tupla1[i], tupla2[i]) otra tupla
print('Lista a partir de tuplas: {}'.format(lista_zipeada))
# Lista a partir de tuplas: [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

#COMVERTIRLA A TUPLA
tupla_zipeada = tuple(lista_zipeada)
print('Tupla a partir de tuplas: {}'.format(tupla_zipeada))
# Tupla a partir de tuplas: ((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))


#ZIP PARA ALTERNAR ELEMENTOS
lista_unida_alternadamente = []
for elemento_1, elemento_2 in zip(tupla1, tupla2): #esto crea la misma tupla de arriba pero cada tupla se desempaqueta con (x, y)
    lista_unida_alternadamente.append(elemento_1) # este es tupla1[i]
    lista_unida_alternadamente.append(elemento_2) # este es tupla2[i]
print('Lista a partir de tuplas: {}'.format(lista_unida_alternadamente)) # ya que en tuplas no funciona append y es inmutable
# Lista a partir de tuplas: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#COMVERTIRLA A TUPLA
tupla_unida_alternadamente = tuple(lista_unida_alternadamente)
print('Tupla a partir de tuplas: {}'.format(tupla_unida_alternadamente))
# Tupla a partir de tuplas: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


#__________________
#CONJUNTOS
conjunto1 = {1, 3, 5, 7, 9}
conjunto2 = {2, 4, 6, 8, 10}
#se pueden zipear más de 2 conjuntos
#CREAR EL SET DIRECTAMENTE CON ZIP (esto en los sets es malo hacerlo)
conjunto_zipeado = set() #donde meteremos las tuplas que se crean a partir de los pares de los elementos i esimos de cada una
for elemento_zipeado in zip(conjunto1, conjunto2): #esto crea: [(conjunto1[0],conjunto2[0]), (conjunto1[1],conjunto2[1])... (conjunto1[n], conjunto2[n])]
    conjunto_zipeado.add(elemento_zipeado) #cada elemento es: (conjunto1[i], conjunto2[i])
print('Set a partir de sets: {}'.format(conjunto_zipeado))
# Set a partir de sets: {(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)} es malo que almacenen otras colecciones


#ZIP PARA ALTERNAR ELEMENTOS
conjunto_unida_alternadamente = set()
for elemento_1, elemento_2 in zip(conjunto1, conjunto2): #desempaquetamiento
    conjunto_unida_alternadamente.add(elemento_1) # este es conjunto1[i]
    conjunto_unida_alternadamente.add(elemento_2) # este es conjunto2[i]
print('Set a partir de sets: {}'.format(conjunto_unida_alternadamente))
# Set a partir de tuplas: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


#__________________
#DICCIONARIOS
dic1 = {'uno':1, 'tres':3, 'cinco':5, 'siete':7, 'nueve':9}
dic2 = {'dos':2, 'cuatro':4, 'seis':6, 'ocho':8, 'diez':10}
#se pueden zipear más de 2 diccionarios
#PERO SOLO ALMACENAR EN LISTAS
#CREAR LA LISTA DIRECTAMENTE CON ZIP (solo claves)
lista_zipeada = [] #donde meteremos las tuplas que se crean a partir de los pares de los elementos i esimos de cada una
for elemento_zipeado in zip(dic1, dic2): #esto crea: [(clave1[0],clave2[0]), (clave1[1],clave2[1])... (clave1[n], clave2[n])]
    lista_zipeada.append(elemento_zipeado) #cada elemento es: (clave1[i], clave2[i])
print('Lista a partir de diccionarios(claves): {} < claves'.format(lista_zipeada))
# Lista a partir de diccionarios: [('uno', 'dos'), ('tres', 'cuatro'), ('cinco', 'seis'), ('siete', 'ocho'), ('nueve', 'diez')]
# se puede hacer con valores pero haciendo algo similar a lo de abajo

#pero si se podria perder el tiempo creando tuplas con las clave:valor de los 2 diccionarios o mas
lista_con_tuplas_con_dics = []
for elemento_1, elemento_2 in zip(dic1, dic2): #desempaquetamiento
    diccionario_temporal_1 = {} #esto es para poder agregar a la tupla
    diccionario_temporal_2 = {} #y este porque tienen que ser agregados diccionarios individiales para añadir a la tupla temporal
    diccionario_temporal_1[elemento_1] = dic1[elemento_1] # asignandole la clave y el valor al diccionario 1
    diccionario_temporal_2[elemento_2] = dic2[elemento_2] # asignandole la clave y el valor al diccionario 2
    tupla_temporal = (diccionario_temporal_1, diccionario_temporal_2) # para poder ir colocando tuplas en la lista
    lista_con_tuplas_con_dics.append(tupla_temporal) #añadiendo la tupla a la lista
print('Lista a partir de diccionarios(claves:valores): {}'.format(lista_con_tuplas_con_dics))

#pero si se podria perder el tiempo creando tuplas con las valores de los 2 diccionarios o mas
lista_zipeada = []
for elemento_1, elemento_2 in zip(dic1, dic2): #desempaquetamiento
    tupla_temporal = (dic1[elemento_1], dic2[elemento_2])
    lista_zipeada.append(tupla_temporal)
print('Lista a partir de diccionarios(valores): {}'.format(lista_zipeada))

#ZIP PARA ALTERNAR ELEMENTOS ({calve:valor})
dic_unido_alternadamente = {}
for elemento_1, elemento_2 in zip(dic1, dic2): #desempaquetamiento
    dic_unido_alternadamente[elemento_1] = dic1[elemento_1] #almacena un clave:valor con: clave: clave1    y   valor: valor del diccionario 1(dic1[clave1])
    dic_unido_alternadamente[elemento_2] = dic2[elemento_2] #lo mismo pero con el dic2
print('Diccionario a partir de diccionarios: {}'.format(dic_unido_alternadamente))
# Diccionario a partir de diccionarios: {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5, 'seis': 6, 'siete': 7, 'ocho': 8, 'nueve': 9, 'diez': 10}

#se pueden hacer mucha cosas pero esto es algunas cosas locas con zip



# M A N E J O   E S P E C I A L     C O N    L I S T A S (Y OTRAS COLECCIONES)
#RANGE
#para crear una lista con numeros enteros es facil con range
lista_con_enteros = list(range(10, 0, -1))
print(lista_con_enteros)
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


#LIST COMPREHENSION
#ELEMENTO FOR I IN RANGE(START:STOP:STEP) IF CONDICIONAL
lista_con_cuadrados = [i**2 for i in range(1, 6) if i%2 != 0] #lo que esta al inicio es lo que se guarda en la lista, respecto a i
print(lista_con_cuadrados)#                    aqui un condicional de numeros impares
# [1, 4, 9, 16, 25]


#DICTS COMPREHENSION
#CLAVE: VALOR FOR I IN RANGE(START:STOP:STEP) IF CONDICIONAL
diccionario_1_100_cube = {x: x**3 for x in range(1, 101) if x%3 != 0} #los primeros 100 numeros al cubo

#SPLIT
string_numeros = '1 2 3 4 5'
numeros = string_numeros.split(' ') # por defecto tiene (' ')
#esto genera una lista que cada elemento es el string separado por cada ( espacio )
print(numeros)
# ['1', '2', '3', '4', '5']
#comvertir de string a lista con metodo split


#JOIN
numeros = [1, 2, 3, 4, 5]
lista=[str(numero) for numero in numeros]# una manera de convertir todos los elementos en texto
#utilizamos lo aprendido anteriormente: (elemento for i in iterable)

string_numeros = ' '.join(lista) #por cada elemento de la lista numeros separarlos con un espacio
print(string_numeros)
# 1 2 3 4 5


#ITERADOR
lista = [1, 22, 5, 7]# listas in iterables
lista_iterable = iter(lista) #esto es lo que pasa con las listas, sets, tuplas y diccionarios en bucles
#comvertirmos a lista en un objeto iterador
#el cual tiene como metodo principal o unico a next(iterador)
elemento_1 = next(lista_iterable)#por ejemplo los carracteres de un string me pasan uno a uno con el metodo next en el iterable
elemento_2 = next(lista_iterable)
elemento_3 = next(lista_iterable)
elemento_4 = next(lista_iterable)
print(elemento_1 ,elemento_2, elemento_3, elemento_4)
#se puede comvertir las colecciones a iteradores


#F U N C I O N E S    D E    A L T O    O R D E N
#son las que utilizan otras funciones
#FILTER
numeros = {1, 2, 3, 4, 5}
def par(x):
    return x%2 == 0
for numero in filter(par, numeros):
    print(numero)
#2
#4

#filter funciona con booleanos, una funcion que utiliza un elemento x como parametro y retorna un booleano que utiliza obvio el parametro x por ejemplo.
#asi de facil identificamos los numeros pares de una lista o puede ser tupla o set:

numeros_tupla = (1, 46, 9, 6, 5, 465, 4, 35)
for numero in filter(par, numeros_tupla):
    print(numero, end=' ')
#46 6 4
print()


#MAP
#map funciona con funciones que retornar algo que queremos
numeros = ['1', '2', '3', '4', '5']
lista_mapeada = list(map(int, numeros)) #map (funcion, *iterable) (cada elemento entra a la funcion)
# | Es para ver el iterable y implementarla la funcion int, esto crea una lista [int(x), int(y)]... |
print(lista_mapeada)
# [1, 2, 3, 4, 5]
#map es similar a filter y a: (elemento for i in iterable)


#REDUCE
number_list = [2, 2, 2, 2, 2]
all_multiplied = 1

for i in number_list:
    all_multiplied = all_multiplied *i
print(f'La multiplicación de todos los elementos es: {all_multiplied}')#32
#vamos a hacer esto pero con reduce
from functools import reduce #se tiene que importar, pero es una orden superior muy importante

all_multiplied = reduce(lambda a, b: a * b, number_list)

print(f'La multiplicación de todos los elementos es: {all_multiplied}')
#32