# cadenas es lo mismo que string osea las cosas que son 'asi'
#en si las cadenas son más o menos inmutables (se les pueden cambiar los valores con los que empezo)
# M E T O D O S
nombre = 'leandro' #leandro tiene 7 carracteres los cuales se les asigna así:
#l  e   a   n   d   r   o
#0  1   2   3   4   5   6

#para saber cuantos carracteres tiene se puede con
cantidad_carracteres = len(nombre) #el cual dara 7 por lo que los indices son: 0 1 2 3 4 5 6

# IDENTIFICAR Y SLICING O SLICES (rebanadas o cortes)

print(nombre[0]) #esta es la ( l )
print(nombre[-1]) #esta es la ( o ) (el ultimo)
print(nombre[-2]) #esta es la ( r ) (el penultimo)
print(nombre[0:2]) #slicing osea que puedo ver desde 0 hasta menor que 2 de sus indices:
#puedo ver  l    e  (este no)
#           0    1     2
print(nombre[0:5:2]) #slicing es: texto[start:stop:step]
#   ✔      ✔      ✔
#   l  e   a   n   d   r   o
#   0  1   2   3   4   5   6

nombre = 'A' + nombre[0:2] + 'j' + nombre[2:] #slicing con concatenaciones con más texto

print(nombre) # NORMAL

print(nombre.upper()) # EN MAYUSCULAS
print(nombre.lower()) # EN MINUSCULAS

print(nombre.capitalize(), ' queda igual xd') # INICIO EN MAYUSCULAS COMO CUANDO VA TEXTO DESPUES DE UN PUNTO
titulo = 'como colocar correctamente los titulos'
print(titulo.title()) # INICIO DE CADA PARABRA EN MAYUSCULAS COMO EN LOS TITULOS

print(titulo.count('co'), 'carracteres "co" tiene el titulo') #ES PARA CONTAR CUANTAS VECES APARECE 'co' EN EL TEXTO

print(titulo.find('los')) # EN CUAL INDICE ESTA LA PRIMERA CADENA 'los'
print(titulo.rfind('los')) # EN CUAL INDICE ESTA LA ULTIMA CADENA 'los' (R DE REVERSE)

print(titulo.rindex('los')) # NO ES BUENO PERO index Y rindex FUNCIONAN IGUAL QUE FIND EN CADENAS, PERO INDEX SE USA PARA LISTA


cadena_nueva = 'ttttholattttt'.strip('t') # QUITA LAS CADENAS 't' DE AMBOS LADOS DEL TEXTO EN SI
print(cadena_nueva)

cadena_nueva = 'ttttholattttt'.lstrip('t') # QUITA LAS CADENAS 't' DE LA IZQUIERDA O COMIENZO DEL TEXTO
print(cadena_nueva)

cadena_nueva = 'ttttholattttt'.rstrip('t') # QUITA LAS CADENAS 't' DE LA DERECHA O FINAL DEL TEXTO
print(cadena_nueva)

cadena_nueva = cadena_nueva.replace('t', '-') # REMPLAZA LAS CADENAS 't' POR '-'
print(cadena_nueva)

#varios metodos medio importantes son:

#1.cadena.isnumeric() --> True solo si todo son numeros: '567543564'

#2.cadena.isalpha() --> True solo si son las 26 letras de alfabeto: 'abcdefghijklmnopqrstuvwxyz'

#3.cadena.isalnum() --> True si tiene las 26 letras y los numeros del sistema decimales: '576383ry3gh9ry87fh9' (seria False: '-1')

#4.cadena.isdigit() --> True si son puros digitos (no sirve mucho)

#4.cadena.isupper() --> True si todas son mayusculas: 'HOLA GRUPO'

#5.cadena.islower() --> True si todas son minusculas: 'hola comostan'

#6.cadena.istitle() --> True Si Es Así Con Mayusculas Al Início: 'Esto Es Un Titulo'

#7.cadena.isspace() --> True si todos son espacios: '       '

#8.cadena.startswith('hola') --> True si comienza por 'hola': 'hola mundo'

#8.cadena.endswith('mundo') --> True si termina en 'mundo': 'hola mundo'

# NO MUY IMPORTANTE POR AHORA

#JUST
nombre = 'Leandro'#7 carracteres
#.rjust rellena desde la derecha, hacia la izquierda (x, 'y'), desde nombre[-1] x veces a la izq, rellenando con 'y'
#el just no remplaza los carracteres puestos y solo rellena str o un codico como unicode
print(nombre.ljust(9, 'x').ljust(10, 'l'))#la marca de ropa :
print(nombre.rjust(9, u'8').rjust(10, '.').rjust(11, '1'))#altura, etc, etc.
#Leandroxxl
#1.88Leandro


titulo = 'como colocar correctamente los titulos'
print('un metodo muy util es split: ', titulo.split(' ')) # todos los elementos espacio separa elemento por elemento y lo coloca en una lista
print(' '.join('IMPORTANTE')) #cada elemento o cada indice lo separa por un espacio
#.join() tambien se puede aplicar en lista etc.
