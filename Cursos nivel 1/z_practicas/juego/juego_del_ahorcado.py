import os
from random import choice
def actualizar_dic(diccionario, letra_nueva, palabra_adivinar):
    '''
    la funcion actualiza letras de la lista que esta en el diccionario
    parametros:
    1.diccionario (dict)
    2.letra_nueva (str)
    3.palabra_adivinar (str)
    la funcion no retorna, pero si modifica el diccionario
    '''
    for indice in range(len(palabra_adivinar)):
        if palabra_adivinar[indice] == letra_nueva:
            diccionario[palabra_adivinar][indice] = letra_nueva #reasignar una letra en la lista del dict


def main():
    #abrir el archivo texto y leerlo y en un lista colocar todas las palabras por renglon
    with open('texto_juego.txt', 'r', encoding='utf-8') as palabras:
        lista_palabras_1 = [palabra.rstrip('\n') for palabra in palabras] # todas las palabras por renglon agregarlas a la lista sin el salto de linea
        lista_palabras = list(map(lambda x : x.lower(), lista_palabras_1)) # a cada letra colocarle .lower ya que en la letra input tambien tiene .lower
        palabra_adivinar = choice(lista_palabras) #aleatoria eleccion entra las palabras
    diccionario_palabra = {}
    lista_letras = []

    for letra in palabra_adivinar:
        lista_letras.append('_')
    diccionario_palabra[palabra_adivinar] = lista_letras #esto es innecesario pero sirve para estructurar

    while True:
        print('¡Adivina la palabra!')

        #mostrar _ _ _ _ ...
        for letra in diccionario_palabra[palabra_adivinar]:
            print(f'{letra}', end=' ')
        print()

        try:
            letra_nueva = input('Ingresa una letra: ')
            assert len(letra_nueva) != 0, ' Ingresar algo'
            assert letra_nueva.isalpha(), ' Ingresar letras'
            letra_nueva = letra_nueva.lower()
        except:
            print('Error\nIngresa letras')
            continue

        actualizar_dic(diccionario_palabra, letra_nueva, palabra_adivinar)#actualizar

        contador = 0 #comenzar contador para ver si el condador coincide con el numero de letras de la palabra_adivinar

        for indice in range(len(palabra_adivinar)):
            if palabra_adivinar[indice] == diccionario_palabra[palabra_adivinar][indice]:
                contador += 1
        if contador != len(palabra_adivinar): #claro si al final no todas son iguales no dara que una sea igual a la otra
            os.system('cls') #reinicio y prosigo
        else:
            break#termino
    os.system('cls')
    print(f'¡Ganaste! La palabra era {palabra_adivinar}')


if __name__ == '__main__':
    main()
