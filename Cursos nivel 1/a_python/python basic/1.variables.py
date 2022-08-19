#DEFINICION:
#1.Simbolo el cual es suceptible de tomar diferentes valores para ser utilizado en un ambito de lógica, algoritmos o formulas.
#2.Es una caja la cual puede contener un valor en determinado momento y en otro momento otro, o siempre el mismo.

# V A R I A B L E S     N U M E R I C A S
N = 30 # se acostumbra que las constantes se escriben todo en mayusculas
x = 4 # (int) <-- son los enteros
y = 8.5 # (float) <-- son los reales o flotantes

# V A R I A B L E S     T E X T O
nombre = 'Leandro' # (str) <-- cadena de carracteres o texto, o en ingles string
empresa = '''
esto es un bloque de codigo
que respeta todas mis espaciaciones
    se hace con 3 comillas
'''

# V A R I A B L E S     B O O L E A N A S
verdadero = True    #(bool) <- es como un 1 en binario, este representa que algo esta encendido o permite    hacer una accion
falso = False       #(bool) <- es como un 0 en binario, este representa que algo esta apagado   o permite NO hacer una accion

# V A R I A B L E S     O T R A S
binario = '0b1010' #numero 10 en decimal
binario = format(10, '0b') #lo mismo
hexadecimal = '0xb' #numero 11 en decimal
binario = format(11, '0x') #lo mismo
direccion = r'D:\desktop\nombre\tasblas' # r de raw (crudo) significa que cosas especiales como ( \n ) no funcionan y es un texto sin más, en general se usa para direcciones
bytes_ = b'hola' #de carracteres a bytes, es lo mismo de abajo
bytes_ = bytes('h', 'utf-8') #o con este generador que debe ser guardado en una coleccion si son mas de 1 carracter

# E X T R A
#1.el nombre que le colocamos se llama identificador
#2.variable se le designa a la funcion del identificador de guardar tipos de conjuntos de carracteres
#4.las variables se escriben sin numeros al inicio y con snake_case: significa que todo en minusculas y las palabras se separan con ( _ ) (guion bajo)
#5. no asignar variables con nombre de variables reservadas como:
'''
False       await       else        import      pass
None        break       except      in          raise
True        class       finally     is          return
and         continue    for         lambda      try
as          def         form        nonlocal    while
assert      del         global      not         with
async       elif        if          or          yield
'''