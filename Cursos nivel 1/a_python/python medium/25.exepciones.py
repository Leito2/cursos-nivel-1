# E X C E P C I O N E S

while True:
    try:        #   INTENTAR ESTE BLOQUE PRINCIPAL
        numero = int(input('Digite un numero positivo: '))
        print(f'sumando 10 al numero queda {numero + 10}')

    except ValueError:     # SI TRY NO FUNCIONÓ ENTONCES HACER ESTE BLOQUE
        #ValueError es porque coloca int(a una cadena de carracteres y no numeros)
        #se pueden crear muchos except(con diferentes tipos de error como este), para no dejarlo como ( except: ) solito que es muy generico.
        print('Ha ocurrido un error') #en este caso especificamente Value Error
        #como no hay break nos devuelve a try porque estamos en un while infinito

    else:       # SI TRY FUNCIONÓ ENTONCE HACER ESTE BLOQUE
        print('Todo salió bien') # quiero que si se ejecuta try, entonces paro el ciclo y digo que todo bien
        break

    finally:    # DA IGUAL SI FUNCIONÓ O NO, FINALLY SE EJECUTA
        print('iteración procesada\n')

#para crear excepciones
# def verificarNumero(numero):
#   if numero < 0:             [error_de_valor]
#       raise ValueError ('numero debe ser positivo')

#   elif numero == 0:           [error_otro]
#       raise AnotherError ('numero no puede ser 0')
#   else:
#       bloque de codigo que queremos ejecutar
#
#numero = ''pedimos numero''
#try:
#   verificarNumero(numero) <-- este lanzará los 2 o más tipos de errores controlados (por lo que este se intenta)

#except ValueError as error_de_valor:  --  esa variable puede ser usada y es la que dice 'numero debe ser positivo'
#   bloque a ejecutar por el error cometido de ser numero negativo

#except AnotherError as eror_otro:  --  esa variable puede ser usada y es la que dice 'numero no puede ser 0'
#   bloque a ejecutar si es 0 o lo que sea

#else: si se ejeculo el else(de la función) y no ocurrio un error, tambien se ejecuta este else
#finally:
#   bloque a ejecutar de todas maneras

# A S I     P O D E M O S   C R E A R   E R R O R E S

#as es una palabra reservada para decir que lo que biene es una variable que se puede utilizar y esa variable es el texto que le definimos a nuestro error

#pueden ser: ValueError, IndexError, KeyError, ZeroDivisionError, TypeError, ImportError  (se llaman Traceback[traza del error])
#nunca se podra utilizar los: NameError o SuntaxError xD por ser errores sintaticos  para nosotros


# A F I R M A C I O N E S
#se tienen que dar por ciertas para el correcto funcionamiento del algoritmo
#ejemplo
def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es texto' #afirmacion 1
        assert len(palabra) > 0, 'No se permite texto vacio'  #afirmacion 2

        primeras_letras.append(palabra[0])

    return primeras_letras