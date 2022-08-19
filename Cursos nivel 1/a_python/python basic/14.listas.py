# L I S T A S
#es una coleccion de variables las cuales incluso pueden ser otras listas, y un conjunto de listas en una lista es una matriz o una tabla
lista_numeros = [1, 3] # elemento_lista: [elemento1, elemento2]
print(lista_numeros)

# I N D I C E S
# [1   ,  3]
#  0      1
print(lista_numeros[0]) #esto es igual a 1 ya que este contiene el indice 0


# S L I C I N G
lista_muchos_tipos = [[1, 10], 4, '7', 3, 'hola', True, 4] #la lista puede tener diferentes tipos
print(lista_muchos_tipos[0:3:1]) # [start:stop:step] desde 0 a 3 sin contar 3
# [[1, 10], 4, '7']


# P R O P I E D A D E S     Y     M E T O D O S
#las listas son mutables por lo que se pueden modificar muy bien y por eso tienen muchas propiedades o metodos


# A Ñ A D I R
#lista.append(a) <-- Forma de añadir un elemento en la ultima posición
lista_numeros = [1, 3]
lista_numeros.append(4) # pasa de [1, 3] ---> [1, 3, 4]
print(lista_numeros)

#lista.insert(posicion, elemento)  <-- un metodo que necesita 2 parametros y que inserta un elemento nuevo en una posicion n
lista_numeros.insert(1, 2) # es como decir: colocar en la posicion 1 el elemento 2
print(lista_numeros) # [1, 2, 3, 4]

#lista1.extend([lista2]) <-- necesita un parametro tipo lista el cual es añadido al final de la lista1
#lo mismo que lista_3 = lista_1 + lista_2
#contatenacion de listas
lista_numeros.extend([5, 6]) # es como decir: expande la lista anterior insertando al final esta lista
print(lista_numeros) # [1, 2, 3, 4, 5, 6]


# B U S C A R
#len(lista) <-- mirar cuantos elementos tienen la lista
len(lista_numeros)

#elemento in lista  <--  identificar si hay un elemento
print(7 in lista_numeros) #falso, 7 no esta en la lista
print(6 in lista_numeros and 5 in lista_numeros) #verdad, 5 y 6 lo acabamos de insertar con el metodo extend

#lista.count(elemento)  <-- cuantas veces se repite o se encuentra el elemento en la lista
lista_numeros.append(6) #primero para facilitar el aprendizaje agrego un 6
print(lista_numeros, 'con count busco cuantos 6 hay')
print(lista_numeros.count(6)) # ahora hay 2
# [1, 2, 3, 4, 5, 6, 6]

#lista.index(elemento)  <--  donde o en que indice se encuentra el elemento
print(lista_numeros.index(6)) # el 6 en la lista_numeros se encuentra primero en el indice 5
#print(lista_numeros.rindex(6)) # el 6 en la lista_numeros se encuentra ultimo en el indice 6
# [1, 2, 3, 4, 5, 6, 6] <-- elementos
#  0  1  2  3  4  5  6  <-- indices


# Q U I T A R
#lista.pop() <-- elimina el ultimo elemento
lista_numeros.pop()
print(lista_numeros)
# [1, 2, 3, 4, 5, 6]

#lista.pop(índice) <-- eliminar el elemento de un índice
lista_numeros.insert(3, 4) #inserto un 4 al lado del 3 y el otro 4
print(lista_numeros) #[1, 2, 3, 4, 4, 5, 6]
#                      0  1  2  3  4  5  6
lista_numeros.pop(3) #elimino el elemento indice 3 (el primer 4)
print(lista_numeros) #[1, 2, 3, 4, 5, 6]

#lista.remove(elemento) <-- eliminar elemento específico
lista_numeros.remove(6) #eliminar el elemento ( 6 )
print(lista_numeros) #[1, 2, 3, 4, 5]


# O R D E N A R
#lista.reverse() <-- darle vuelta
lista_numeros.reverse() #sin argumentos
print(lista_numeros) #[5, 4, 3, 2, 1]

#lista.sort() <-- ordenar de menor a mayor, claro tienen que ser elementos compatibles como todos numeros o todo alfabeto
#lista.sort(reverse=True) -- desendentemente (combinar sort con reverse)
lista_numeros.sort() #este es el caso en donde no hay argumento
print(lista_numeros) # otra vez [1, 2, 3, 4, 5]
listaaa = [3, 2]
listaaa = sorted(listaaa) #otra manera de ordenar
print(listaaa) # [2, 3]
#lista = sorted(lista, reverse=True) #otra manera de dar reversa ordenada

# O T R O S
#MULTIPLICAR
#lista = lista*n <--  multiplicar n veces los elementos de la lista
lista_numeros = lista_numeros*2 #duplicar
print(lista_numeros) #[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

#REASIGNACION
#lista[n] = elemento_remplazo <-- en el elemento que se le asigna el indice n, remplazarlo por el elemento_remplazo
lista_numeros[0] = 'inicio'
print(lista_numeros) #['inicio',2, 3, 4, 5, 1, 2, 3, 4, 5]

#BORRAR
#lista.clear() <-- borrar todo
lista_numeros.clear()
print(lista_numeros) #[]

#CLONAR
#para que listas iguales no sean el mismo objeto y genere errores es util evitarlos clonando listas
lista_base = [1, 3, 5]
lista_clonada = lista_base[::] #manera numero 1
lista_clonada_dos = list(lista_base) #manera numero 2