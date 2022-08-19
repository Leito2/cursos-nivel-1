# F U N C I O N E S     C O N   R E T O R N O
def nombre_funcion(parametro1, parametro2):
    retorno = parametro1 * parametro2 #cualquier cosa que quieras hacer con o sin el parametro
    return retorno #con el valor return se puede retornar un retorno y este debe ser obligatoriamente utilizado para output o para almacenarlo como un dato dentor de una variable

argumento1 = 3
argumento2 = 'hola'

hola_hola_hola = nombre_funcion(parametro1 = argumento2, parametro2 = argumento1) #esto prueba que en si argumento y parametro es distinto y que podemos asignar en desorden nuestros argumentos a lo parametros que quiere o necesita la función

#saber que no se puede que la funcion no la utilicemos para algo, como las de sin retorno que se colocan así sin más porque esto retorna algo y esto debe ser utilizado para algo, o no ser utilizado sin más

#las funciones con retorno en general retornan algo con la palabra: return

'''
en realidad cuando se arranca un programa se debe hacer con una funcion llamada run o main
otras funciones:
    pass
_____________
def main():
    pass
o con:
def run():
    pass
______________

pero tambien con:
if __name__ == '__main__':
    run()
    o
    main()

lo cual es que __name__ es que si queremos ejecutar codigo debemos estar en ese archivo, y __name__ retorna el texto:
'__main__' cuando esto sucede

claro, en pass debemos colocar todo nuestro codigo con sus algoritmos
'''