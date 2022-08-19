# D I C C I O N A R I O
# estos son totalmente desordenados, por lo que no importa su indice, estos elementos se buscan por su nombre y se insertan segun su elemento y no por una posición

diccionario = {'hola':'hello', 'azul':'blue'} # un diccionario se crea con {clavo:valor, clave:valor}
diccionario = {
    'hola':'hello',
    'azul':'blue',
} # lo mismo

print(diccionario) # {clave1:valor1, clave2:valor2}


# A S I G N A R     Y     R E A S I G N A R
#ASIGNAR
diccionario['amarrillo'] = 'yellow' #añade ('amarrillo':yellow)
# {'hola':'hello', 'azul':'blue', 'amarrillo':'yellow'}
diccionario['leo'] = [18, 'senior', '188', 75] # se pueden añadir otras colecciones
print(diccionario)
# {'hola': 'hello', 'azul': 'blue', 'amarrillo': 'yellow', 'leo': [18, 'senior', '188', 75]}

#REASIGNAR
diccionario['verde'] = 'tree' #añade ('verde':'tree')
diccionario['verde'] = 'green' # y reasignar ('verde':'tree') por ('verde':'green')
print(diccionario)
# {'hola': 'hello', 'azul': 'blue', 'amarrillo': 'yellow', 'leo': [18, 'senior', '188', 75], 'verde': 'green'}


# E L I M I N A R
del(diccionario['hola']) # se borra según el elemento, osea se puede hacer directamente con su clave ya que su valor es un tanto secreta, más adelante se mirara como manipular mas libremente sus elementos y borrarlo según su valor,  pero conociendo tambien su clave.
del(diccionario['leo'])
print(diccionario)
# {'azul':'blue', 'amarrillo':'yellow', 'verde':'green'}


# B U S C A R   C O N   C L A V E
#BUSCAR CLAVE  A PRIORI
print(diccionario['amarrillo']) # el valor de 'amarrillo' es 'yellow'

#BUSCAR CLAVE PARA VER SI ESTA
#se puede buscar una clave y si esa no existe ejecutar otra cosa o retornar otra cosa
#diccionario.get(clave, ejecutar si no esta el elemento)
print(diccionario.get('naranja', 'ese color no esta en el diccionario')) # como 'naranja' no esta en las claves, entonces se ejecuta lo otro


# I T E M S     K E Y S     V A L U E S
print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())
#.keys y .valeus retornan listas con lAS CLAVES o VALORES, pero .items retorna tuplas con (clave, valor) dentro de una lista


# C L E A R
diccionario.clear() #borrar todo
print(diccionario)
# {}

#dato curioso  ---    len(coleccion) sirve para todas las colecciones y en el lenguaje C++/C las listas no pueden tener muchos tipos
