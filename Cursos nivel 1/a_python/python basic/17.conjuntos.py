# S E T S
#en las sets o conjuntos son datos totalmente desordenados y unicos, sin poder tener colecciones
#porque estos conjuntos son primarios y se operan con otros conjuntos

# D E F I N I R
conjunto = {1, 5, 'hola' , 6.5, 'adios'} # {elemento1, elemento2..., elementon}
print(conjunto) # {1, 5, 6.5, 'hola', 'adios'}
#se ordena solo como le conviene


# A Ñ A D I R
#conjunto.add(elemento)  <--  es como un append desordenado
conjunto.add('good') #no se puede tener 2 'good' en el conjunto o set
print(conjunto) # {1, 5, 6.5, 'hola', 'good', 'adios'}
# como se ve el 'good' se medio en la penultima posicion (donde le dio la gana)


# E L I M I N A R
#conjunto.discard(elemento) <-- es como un .remove(elemento)
conjunto.discard('good')
print(conjunto) # {1, 5, 6.5, 'hola', 'adios'}


# C L E A R
#conjunto.clear()  <--  es el mismo clear
conjunto.clear()
print(conjunto) # queda como: set() <- que es diferente a {} ya que eso seria diccionario vacio, es la misma razon por la que un set vacio se crea asi:

conjuntox = set() # siempre se crea así
conjuntox = {} #este es opcional, pero no se crea solo con colocar {} desde el inicio



# T E O R I A   D E     C O N J U N T O S
#en los conjuntos se hacen operaciones como en las de teoria de conjuntos (operaciones con conjuntos)

# U N I O N
#suma o union es como decir a o b en logica proposicional (con conectores logicos)
conjunto1 = {1, 2,  3, 4}
conjunto2 = {3, 4, 5, 6}
conjunto3 = conjunto1 | conjunto2 # se unen con el signo | que en otros lenguajes es lo mismo que ( or en condicionales)
print(conjunto3) # {1, 2, 3, 4, 5, 6} se refiere a la suma de elementos sin repetir


# I N T E R S E C C I O N
#interseccion como decir a y b
conjunto3 = conjunto1 & conjunto2 # se intersectan con el signo & que en otros lenguajes es como decir && ( and )
print(conjunto3) # {3, 4} sin repetir y se refiere a los elementos comunes


# D I F E R E N C I A
#diferencia como decir a y no b
conjunto3 = conjunto1 - conjunto2 # se restan con el signo de resta
print(conjunto3) # {1, 2} es como decir que todo el conjunto 1 menos lo que tiene en comun con el conjunto 2


# D I F E R E N C I A   S I M E T R I C A
conjunto3 = conjunto1 ^ conjunto2  # se hace con el signo ^ ( alt derecho más conchete[ )
print(conjunto3) # {1, 2, 5, 6} es la union de los 2 pero se le quita su interseccion, o es como sumar las 2 diferencias



# I S S U B S E T   |   I S S U P E R S E T     |    |I S D I S J O I N T
#tambien tiene algunas funciones internas de conjuntos

#1. a.issubset(b)   <-- ES MIRAR SI A SERIA UN CONJUNTO DENTRO DE B
#2. b.issuperset(a) <-- ES MIRAR SI B SERIA UN CONJUNTO QUE DENTRO TIENE A
conjunto1 = {1, 2,  3, 4}
conjunto2 = {1, 2, 3, 4, 5} #tambien coloca true si fuera {1, 2, 3, 4} (iguales)
print(conjunto1.issubset(conjunto2) and conjunto2.issuperset(conjunto1)) #las 2 son true
#si sus intersecciones son 0 entonces son disconexos
#3.a.isdisjoint(b)
print(conjunto1.isdisjoint(conjunto2)) #obvio que tienen elementos en común por lo que no son disconexos
#     esto da False

#a veces estos sets son reveldes y quieren ser inmutables tipo tuplas entonces para convertirlos como quieren ser, se coloca:
#conjunto = frozenset(conjunto)
conjunto1 = frozenset(conjunto1) #ya no funciona conjunto.add(elemento) ni discard
print(conjunto1)