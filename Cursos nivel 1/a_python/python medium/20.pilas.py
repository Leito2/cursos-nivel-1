#P I L A S
#el ultimo en entrar pero primero en salir es como una pila de libros (apilar, desapilar)
#en general usa solo append y pop y en general se trabaja con lo que retorna pop
print('pilas\n')

pila = [1, 2, 3] #vamos a simularlas con listas
print(pila) # lo mismo

#como una pila se añaden cosas por el final como con append()

pila.append(4)
pila.append(5)
print(pila)
# [1, 2, 3, 4, 5]

#como una pila se quitan por el final de la lista con pop(sin parametro)

ultimo_elemento= pila.pop() #además de quitar pop coge el libro y lo guarda
print(f'de {pila} quite el elemento {ultimo_elemento}') # el pop retorna lo que quito
#       de [1, 2, 3, 4] quite el elemento 5