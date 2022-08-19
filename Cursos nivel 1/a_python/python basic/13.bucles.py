# W H I L E
#1.While (condicion): <--  mientras algo se cumpla, lo que esta dentro del bloque de while se ejecuta indefinidamente
#2.while True: <--  es un ciclo infinito
#3.(continue) sirve para parar de ejecutar el bloque y hacer otra nueva iteración o repetición
#4.(break)  sirve para parar por completo el bucle while
# ES IMPORTANTE EVITAR EL INFINITE LOOP

#1
numero = 0 #este va a ser el numero base que luego nos ayudara a dejar de cumplir la condición

while numero < 10:  #la condicion siempre cumple si numero es menor a 10
    print(numero, end=' ')   #mientras la condicion cumpla se ejecuta todo este bloque de codigo
    numero +=1      #luego para que numero vaya aumentando le sumamos 1 cada vez que el cliclo se repita

#2 3 4
numero = 1
while True: #bucle infinito solo se para con un break
    if numero == 10: #cuando la condicion, numero sea igual a 10 se cumpla...
        break        #el ciclo para
    numero +=1
    continue
    #lo que coloque despues de continue
    #no se ejecuta nunca
    #porque continue repite el ciclo desde ese punto
    #pero no lo rompe como break
    #pero tampoco es que sea decorativo como pass

# esto ejecutara en consola: 0 1 2 3 4 5 6 7 8 9
# 10 no se ejecuta porque 10 no es menor a 10 (recordar que por defecto un print tinene end='\n')


# F O R     R A N G E
#for variable in range(start, stop, step): <-- es un ciclo que se repite tantas veses como: '(stop-start)/step'

#start: indica con que valor numerico comienza variable
#stop: indica donde no se puede pasar el valor de la variable, sin llegar a ser stop
#step positivo: sumar por asignacion en cada ciclo
#step negativo: restar por asignacion en cada ciclo

#la variable toma valores segun el tipo de rango: [ (1, 11) del 1 al 10 ], [ (10, 0, -1) del 10 al 1 ]

for numero in range(0, 10, 1):  #por defecto esto es lo mismo que (0, 10) o (10) [por defecto start en 0 y step en 1]
    print(numero, end=' ')      #0 1 2 3 4 5 6 7 8 9    esto es lo mismo que el primer while
print('ciclo finalizado')


#F O R      E L E M E N T O     IN      S T R I N G
#por el momento este funciona solo en cadenas de carracteres
#for carracter in cadena: <-- es un ciclo que se repite como carracteres en la cadena, y guarda momentaneamente el carracter en la variable(carracter)

nombre = 'leandro' #cadena con 7 carracteres

for carracter in nombre: #el ciclo se repetira 7 veses y en la primera carracter: l y en la ultima carracter: o
    print(carracter + '.')
#esto imprime:
#l.
#e.
#a.
#n.
#d.
#r.
#o.