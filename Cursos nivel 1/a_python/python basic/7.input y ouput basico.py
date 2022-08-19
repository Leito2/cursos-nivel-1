#en diagramas de flujo se colocan como un paralelogramo y es utilian para pedir y mandar datos
# I N P U T     input()
variable_en_texto = input('Escribir 33: ')
# input() retorna un string con lo que se escribe en carracteres en la consola por ejemplo '33'
variable_en_entero = int(input('Escribir 33: '))
#esto si seria 33 como numero operable

# IMPORTANTE    \n  y   \t
print('hola\nmundo')  #imprime: hola (paso de linea)
#                               mundo

print('hola\tmundo')  #imprime: hola    mundo (tabulacion)

# O U T P U T
#PROPIEDADES
#1.print('texto' + 'otro')  esto es igual a 'textootro' <-- el '+' funciona siempre que todo ea texto o numeros
#2.print('texto', 'otro')   esto es igual a 'texto otro'
#3.
# print('texto', end=' ')
# print('otro') <--  esto seria 'texto otro' (a diferencia de no colocar end -> saltaria de linea [por defecto: end='\n'])
#4.print('texto', 'otro', sep='_') <-- esto seria 'texto_otro' (la coma por defecto tiene sep=' ', por lo que esto indica el tipo de separacion)
print(variable_en_texto, variable_en_entero, sep=' en numero es: ', end=' ') #no hay diferencia entre '33' y 33 al imprimirlos
print('(es lo mismo)')


# F O R M A T
#1.print(f'este es tu numero {x}')
#esto sirve para formatear el texto y colocarle una variable entre texto, como por ejemplo colocar esto
x = 3.141592653589793238462643383279
print(f'x es igual a: {x}') # en {variable} tambien...
# x es igual a: 3.141592653589793238462643383279

print(f'x es igual a: {x:.3f}') # se puede colocar :.°decimales
# x es igual a: 3.14(redondea)

print(f'x es igual a: {round(x, 3)}') # hay un metodo para eso tambien
# x es igual a: 3.142(lo redondea)

#2.print('estos son tus numeros {}, {}, {}'.format(x, y, z))
#por defecto el primer {} tiene un numero implicito {0} y se le asigna .format(0, 1, 2) esos son los incides de cada argumento o cada variable que yo le paso a .format()
#es lo mismo que print('estos son tus numeros {0}, {1}, {2}'.format(x, y ,z))
y = 4
z = 8
print('estos son tus numeros {1}, {0}, {2}'.format(x, y, z)) #tambien en desorden
#   estos son tus numeros 4, 3.141592653589793, 8


# % (mapeo con %)
numero = '3'
numero_mapeado = 'hola%s %s%s' %(numero, numero, numero) #si esto fuera solo numeros sin sepacio se podria colocar int()
print(numero_mapeado) # hola3 33 (s de string)

decimal = 3.141592
print('el valor redondeado a 3 decimales es %.3f' %decimal) #para colocar de manera facil decimales limitados
#     el valor redondeado a 3 decimales es 3.142

palabra = 'holeichon'
print('%.4s' %palabra) #para colocar de maneara facil parabras limitadas
#     hole (4 carractere de string)