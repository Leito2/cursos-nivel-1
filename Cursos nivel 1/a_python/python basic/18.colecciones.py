# C I C L O S   F O R (PARA MANEJAR LOS ELEMENTOS)
#LISTAS
lista = [1, 2, 'tres', 4, 5, 6]
for elemento in lista:
    print(elemento, end=' ')
print()

# esto imprime: 1 2 'tres' 4 5 6
#en el ciclo for con elementos se puede recorrer todos los elementos de la lista


#TUPLAS
tupla = (1, 2, 'tres', 4, 5, 6)
for elemento in tupla:
    print(elemento, end=' ')
print()

# esto imprime: 1 2 'tres' 4 5 6
#en el ciclo for con elementos se puede recorrer todos los elementos de la tupla


#CONJUNTOS
conjunto = {1, 2, 'tres', 4, 5, 6}
for elemento in conjunto:
    print(elemento, end=' ')
print()

# esto imprime: 1 2 4 5 6 'tres
#en el ciclo for con elementos se puede recorrer todos los elementos del conjunto


#DICCIONARIO (desempaquetamiento de tuplas)
diccionario = {
    'clave1':'valor1',
    'clave2':'valor2',
    'clave3':'valor3'
}
for tuplas_con_clave_valor in diccionario.items(): # tupla con (clave, valor)
    print(f'esta es una tupla: {tuplas_con_clave_valor}')

#esta es una tupla: ('clave1', 'valor1')
#esta es una tupla: ('clave2', 'valor2')
#esta es una tupla: ('clave3', 'valor3')

for (clave, valor) in diccionario.items(): # tambien funciona colocando    for clave, valor in...
    print(f'Calve: {clave}\tValor: {valor}') # esto se llama desesmpaquetamiento de tuplas (en el diccionario con .items())
#Calve: clave1   Valor: valor1
#Calve: clave2   Valor: valor2
#Calve: clave3   Valor: valor3

#osea que para diccionarios aca se maneja la clave y el valor y no un solo elemento
#se puede hacer individualmente con .values o .keys



# C I C L O S   F O R (PARA MANEJAR INDICES Y ELEMENTOS)
#LISTAS
lista = [1, 2, 3, 4, 5]
for (indice, elemento) in enumerate(lista, start=0): #esto tambien se guarda en tuplas (indice, elemento)
    print('Indice: {}\tElemento: {}'.format(indice, elemento))#por defecto enumerate comienza en 0 son el start=0
#Indice: 0       Elemento: 1
#Indice: 1       Elemento: 2
#Indice: 2       Elemento: 3
#Indice: 3       Elemento: 4
#Indice: 4       Elemento: 5


#TUPLAS
tupla = (1, 2, 3, 4, 5)
for (indice, elemento) in enumerate(tupla): #esto tambien se guarda en tuplas (indice, elemento)
    print('Indice: {}\tElemento: {}'.format(indice, elemento))
#Indice: 0       Elemento: 1
#Indice: 1       Elemento: 2
#Indice: 2       Elemento: 3
#Indice: 3       Elemento: 4
#Indice: 4       Elemento: 5


#CONJUNTOS
conjunto = {1, 2, 3, 4, 5}
for (indice, elemento) in enumerate(conjunto): #esto tambien se guarda en tuplas (indice, elemento)
    print('Indice: {}\tElemento: {}'.format(indice, elemento)) #aca simplemente no sirve para nada
#Indice: 0       Elemento: 1
#Indice: 1       Elemento: 2
#Indice: 2       Elemento: 3
#Indice: 3       Elemento: 4
#Indice: 4       Elemento: 5


#DICCIONARIOS
diccionario = {'uno':1, 'dos':2, 'tres':3, 'cuatro':4, 'cinco':5}
print(diccionario)
for (indice, elemento) in enumerate(diccionario): #esto tambien se guarda en tuplas pero es (indice, clave)
    print('Indice: {}\tClave: {}'.format(indice, elemento)) #aca simplemente no sirve para nada
#Indice: 0       Clave: 'uno'
#Indice: 1       Calve: 'dos'
#Indice: 2       Calve: 'tres'
#Indice: 3       Calve: 'cuatro
#Indice: 4       Calve: 'cinco'

#el valor se chingo