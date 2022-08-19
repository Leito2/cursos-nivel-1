#en las tuplas solo se puede seleccionar, slicing, buscar, contar, buscar index, o saber su nuero de elementos y comvertir la tupla en lista y biseversa pero eso se guardaria en otra variable (no es tipado dinamico)
#las tuplas son más rapidas en ejecución
# T U P L A S
#aca solo se puede hacer busqueda y 'convertirla en listas' (las tuplas son inmutables)
#pero las tuplas son más rapidas pero estáticas

# B U S C A R
#len(tupla) <-- mirar cuantos elementos tienen la tupla
tupla = (1, 3, 4, 4)
tupla_nueva = (1,)
#ya que crear una tupla nueva con 1 elemento es diferente a (1) esto es un tipo entero
print(len(tupla))

#elemento in tupla  <--  identificar si hay un elemento
print(2 in tupla) #falso, 7 no esta en la tupla
print(1 in tupla and 3 in tupla) #verdad, 1 y 3 estan agregados
#     (1, 3, 4, 4)

#tupla.count(elemento)  <-- cuantas veces se repite o se encuentra el elemento en la tupla
print(tupla, 'con count busco cuantos 4 hay')
print(tupla.count(4)) # hay 2
#     (1, 3, 4, 4)

#tupla.index(elemento)  <--  donde o en que indice se encuentra el elemento
print(tupla.index(4)) # el 6 en la tupla se encuentra primero en el indice 2
# [1, 3, 4, 4] <-- elementos
#  0  1  2  3  <-- indices
#no funciona rindex ya que es inecesario repetir elementos