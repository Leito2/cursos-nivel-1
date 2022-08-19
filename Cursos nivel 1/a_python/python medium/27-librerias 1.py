#se puede importar como:
#import Nombre as alias
#import random as rd
#from random import randint, sample, choice <-- modulos de la libreria o paquete
#from libreria import *      <---  (todos) lo mismo que import libreria
#ser modulos o funciones de la libreria = dir(libreria)
import random, math, datetime

# M A T H
#cosas para matematicas

#FLOOR, CEIL
print(math.floor(3.7)) #redondea al menor = 3
print(math.ceil(3.7)) #redondea al mayor = 4
print(math.floor(3.7)) #parte entera(como floor xd) = 3

#PI
print(math.pi)#valor de pi

#SIN, COS, TAN...
print(math.sin(math.radians(45)))
print(math.cos(45))




#R A N D O M
#es una libreria para cosas al azar y totalmente util

#RANDINT
#numero aleatoria incluyendo los extremos de los parametros
#randint(int)
print(random.randint(1, 100))#numero aleatorio del 1 al 100

#RANDRANGE
#se comporta como los parametros de range()
#numero aleatorio como randint pero con 1parametro y sin incluir
#randrange(int)
print(random.randrange(101))#del 0 al 100
#numero aleatorio sin incluir extremo de arriba
print(random.randrange(1, 101))#del 1 al 100
#numero aleatorio con (start, stop, step) sin incluir stop
print(random.randrange(0, 101, 2))#0 a 100 de pares

#RANDOM
#del 0 al 1 aleatorio
#random(int)
print(random.random())

#UNIFORM
#combinacion entre randint y random
#random(float)
print(random.uniform(1, 10)) #decimal 1-10 (incluye extremos como randint)

#CHOICE
#elige al azar un elemento de la lista
#choice(coleccion)
print(random.choice(list({1, 7, 6})))# elige uno de los 3 elementos de la coleccion
#comvertí en lista un set

#SAMPLE
#elegir al azar n elementos de la lista sin repetir
#sample(coleccion, int) #error con sets
print(random.sample([1, 7, 6], 2))# elige 2 de los 3 elementos de la coleccion

#SHUFFLE
#desordenar la lista
#shuffle(list)
lista = [1, 7, 6]
random.shuffle(lista)
print(lista) #con solo listas




# D A T E T I M E
#2 principales modulos dentro de este, date y datetime

#DATE
#actual
dia_actual = datetime.date.today() #fecha actual
#datetime.date(year, month, day)
print(dia_actual) #dia_actual.month (mes), dia_actual.year (año), dia_actual.day (dia)
#2022-07-28

#establecer
dia = datetime.date(1, 1, 1)
print('fecha con datetime.date(year, month, day:', dia)#1.manera de crear
#fecha con datetime.date(year, month, day: 0001-01-01


#DATETIME (mas precision)
#fecha actual y tiempo transcurrido
inicio_tiempo= datetime.datetime.now() # esque es lo mismo que datetime.date.today()
#
#PROCESO
#
final_tiempo= datetime.datetime.now()
#tiempo que toma
#minutos, segundo y microsegundo
tiempo_tomado = (final_tiempo - inicio_tiempo).min
print(tiempo_tomado, 'minuto')
tiempo_tomado = (final_tiempo - inicio_tiempo).seconds
print(tiempo_tomado, 'segundo')
tiempo_tomado = (final_tiempo - inicio_tiempo).microseconds
print(tiempo_tomado, 'microsegundos')

#establecer fecha
#nueva_fecha_datetime = datetime.datetime(año, mes, dia)
#o tambien:
#nueva_fecha_datetime = datetime.datetime(año, mes, dia, minutos, segundos, milisegundos)

nueva_fecha_datetime = datetime.datetime(2022, 7, 12, 00, 30, 000)#2.manera de crear
print(nueva_fecha_datetime)
#2022-07-12 00:30:00

#timedelta
fecha_mas_un_dia = nueva_fecha_datetime + datetime.timedelta(days=1, seconds=1) #sumar 1 dia
#weeks=x, days=x, hours=x, minutes=0, seconds=x, milliseconds=x, microeconds=x.
#con numeros positivo o negativos(pasado)
print(fecha_mas_un_dia)
#2022-07-13 00:30:01

#editar la muestra de fechas (string function time)
print(fecha_mas_un_dia.strftime('%d, %b, %Y'))
#13, Jul, 2022
#AÑO
# % Y (2014) <> (0000-9999, son los años 'normales', %y es pero de 00-99 y 00-9999)

#MES
# % m (0) <> (0-12 numeros de los meses)
# % B (July) <> (nombre de meses en ingles, %b lo abrevia)

#SEMANA
# % W (53) <> (00-53, semanas del año en numeros)

#DIA
# % j (365) <> (001-366, dias del año en numero)
# % d (01) <> (01-31 numeros de los dias)
# % A (Sunday) <> (dias de la semana en ingles, %a lo abrevia)

#TIEMPO
# % H (23) <> (0-23, hora larga o militar)
#
# % I (12) <> (0-12 hora regular)
# % p (AM) <> (AM, PM, es la que acompaña a %I)
#
# % M (59) <> (0-59, minutos)
#
# % S (59) <> (0-59, segundos)
#
# % f (999999) <> (000000-999999, microsegundos)





#O T R O S
#CALENDAR
import calendar
#saber un mes en un formato familiar, sabiendo el año y el mes a representar
year = 2022
mes = 7
print(calendar.month(year, mes)) # mes y año para un calendario
#     July 2022
#Mo Tu We Th Fr Sa Su
#             1  2  3
# 4  5  6  7  8  9 10
#11 12 13 14 15 16 17
#18 19 20 21 22 23 24
#25 26 27 28 29 30 31


#COUNTER
from collections import Counter
numeros = (4, 5, 3, 2, 5, 13, 6, 13, 6)#lista o tuplas
conteos = Counter(numeros) #crea diccionario que cuenta en los valores las repeticiones de un elemento clave
print(conteos) #Counter({5: 2, 13: 2, 6: 2, 4: 1, 3: 1, 2: 1})


#PERMUTACIONES
from itertools import permutations
lista=[1, 2, 3, 4]
lista_variacion_en_n=permutations(lista, 2)#variacion en k = 2
#una lista con tuplas de la variacion en k!
for e in lista_variacion_en_n:
    print(e)
#(1, 2) #(1, 4) #(2, 3) #(3, 1) #(3, 4) #(4, 2)
#(1, 3) #(2, 1) #(2, 4) #(3, 2) #(4, 1) #(4, 3)
# variacion = 12