# S C O P E (ALCANCE DE VARIABLES)
nombre='Global'# VARIABLE GLOBAL
def primerafuncion(nombre):
    print(nombre)#                          imprime la variable global------1
    nombre = 'Enclosing'#reasigna VARIABLE ENCLOSING (entre 2 funciones)
    def segundafuncion(nombre):
        print(nombre)#                      imprime la variable enclosing---2
        nombre = 'Local'#reasignar VARIABLE LOCAL
        print(nombre)#                      imprime la variable local-------3
    segundafuncion(nombre)#la primera funcion ejecuta la funcion local
primerafuncion(nombre)
#Global
#Enclosing
#Local


# F U N C I O N E S     R E C U R S I V A S
#el una funcion llamarse a si mismo
def cuenta_regresiva(num):
    if num > 0:
        print(num)
        cuenta_regresiva(num - 1)   #se llama a si misma maximo 994 veces y reduciendo valores
    elif num < 0:
        print('no funciona para numeros negativos')
    else:                           #para que cuando llegue a 0 termine el bucle
        print('BOMMMMM !')
cuenta_regresiva(994) #maxima recursión

import sys
print(sys.getrecursionlimit()) #maxima recursión
#1000
#Para modificar ese límite
n = 1000 # por ejemeplo
sys.setrecursionlimit(n) # n es el nuevo límite a establecer


# A R G S    Y    K W A R R G S
#cuando se quiere colocar lista o elementos en forma de lista indefinida en  los parametros
#se colocar *nombre (en este caso args porque los argumentos se pasan a la lista pero puede ser: *nombre por ejemplo)
def tienda (*args, **kwargs):
    print(args)
    print(kwargs)#por otro lado **kwargs (con **) es para argumentos tipo diccionario solo: (clave=valor)
    print(f'Me gustaria comprar {args[-1]} de {kwargs["tomar"]}') #maneara para referirse a los args y kwargs
tienda(4, 8, 43, 5, tomar='leche', comer='jamon', jugar='x-box-360')#formatos lista y diccionario con estos tipos de parametros


# M O D U L O S     D E     F U C I O N E S
lista=[]
cuantos = int(input('Quieres sumar cuantos numeros?: ')) #utilizar en consola
for i in range(cuantos): #ciclo se repite cuantas veces se diga en cuantos
    z= 'El numero ' + str(i+1) + ' es: ' #definir texto con la variable i para colocar en input <IMPORTANTE
    agregar = int(input(z)) #pedir entero
    lista.append(agregar)#cada entero agregar a lista
#IMPORTANTE
import otro #importa el paquete otro.py el cual tiene distindos modulos (sumar_lista, sumar_estos)
print('La suma de los numeros es: ', otro.sumar_lista(lista))
print('Suma de 1, 3 y 4 es: ', otro.sumar_estos(1, 3, 4)) # aplicacion con lo anterior *args


#Y I E L D
def my_gen(i):
    while i >= 0:
        yield i#retorna elemento i que se añada, en este caso hasta que 3 sea -1, por lo que retorna:
        i -= 1#un iter([3, 2, 1, 0])
for x in my_gen(3):
    print(x)
#esto es como lo que es una funcion range()
#se puede imitar


# L A M B D A
#def nombre(parametros):
#   return valor_retornado
#nombre = lambda parametros: valor_retornado
#ejemplo
nombre_de_funcion_en_un_objeto = lambda parametro_1, parametro_2 : parametro_1 + parametro_2
resultado = nombre_de_funcion_en_un_objeto(1, 3)
print(resultado)
#        4
#esto explica por ejemplo que las funciones son objetos y se pueden colocar en variables
#lo mismo las funciones se pueden meter en listas o en parametros pero solo el nombre: (nombre_funcion)