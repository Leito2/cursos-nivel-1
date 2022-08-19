#Primero vamos a hacer diferentes aclaraciones que pueden ayudar a comprender el tema como a repasar el tema de manera efectiva
#1. (1) DIFERENTE A (1.0)
#2. (2) DIFERENTE A ('2')
#3. (True) DIFERENTE A ('True')
#4. (6) DIFERENTE A ('0b110)
#5. (9) DIFERENTE A ('0x9')
#6. ('\t') DIFERENTE A ('  ')


# 1     I N T   -   F L O A T
entero = 1 #transformo el entero 1 a flotante con:
# float(entero) = 1.0

flotante = 1.0 #transformo el flotante a entero con:
# int(entero) = 1

entero_a_natural = abs(-1) #( 1 ) valor absoluto

#'son lo mismo' pero '1.0' es diferente a '1' y cuando hacemos algunas cosas son diferente

#2      N U M E R O   -   S T R I N G
entero = 3
entero_texto = str(entero) #esto sera igual a '3' y lo podemos concatenar con otro texto
entero_otra_ves = int(entero_texto) # es como int('3') <-- y ahora con esto podemos hacer todas las operaciones aritméticas con otros números

flotante = 3.5
flotante_texto = str(flotante) #esto sera '3.5'
flotante_otra_ves = float(flotante_texto) #esto volvera a 3.5

#3      B O O L E A N O S   -   S T R I N G
booleano = True
booleano_texto = str(booleano) #esto no es muy util pero se puede
booleano_otra_ves = bool(booleano_texto) #vuelve a ser un valor  1 0 un booleano de verdadero y falso

#4      D E C I M A L   -   B I N A R I O

decimal_a_binario = bin(10) # con bin(decimal) <-- podemos convertir un numero ENTERO a binario(que es como un texto '0b[binario]')

binario_a_decimal = int('0b1010', 2) # con int(binario) <-- podemos convertir un binario texto (el cual es en base 2 por eso luego se coloca 2) a un entero o del sistema normal decimal por ser de base 10

#5      D E C I M A L   -   H E X A D E C I M A L

decimal_a_hexa = hex(12) # con hex(decimal) <-- podemos convertir un numero ENTERO a hexadecimal(que es como un texto '0x[hexadecimal]')

hexa_a_decimal = int('0xc', 16) # con int(hexadecimal) <-- podemos convertir un hexadecimal texto (el cual es en base 16) a un entero

#6      S T R I N G     A   S T R I N G C   C R U D O
#como \n es un enter y \t es un tab
tabla = 'nombre\tapellidos\tedad' #esto se ve así |nombre   apellidos   edad| (como una tabla)
tabla_sin_ser_tabla = r'nombre\tapellidos\tedad' # literal es 'nombre\tapellidos\tedad'