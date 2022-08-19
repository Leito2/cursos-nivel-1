#F U N C I O N E S      I N T E G R A D A S
print(abs(4)) # valor absoluto
print(round(3.1415, 2)) # aproximacion de 3 decimales
print(type('hola')) #tipo de objeto (str) << exiten (str, int, float, bool, list, tuple, set, dict, iteradores...)
isinstance(3, int) #mirar si el elemento es de tipo o clase...
print(id('hola')) #la id del objeto en memoria
#para comvertir o otra cosas utiles (con doble parentesis o sea con tuplas)
print(bool('True')) #tipo bool
print(list((4, 5))) #tipo lista
print(tuple((4,))) #tipo tupla
print(set((4, 5))) #tipo conjunto
print(dict(((4, 'cuatro'), (6, 'seis')))) #tipo diccionario

print(iter((1, 4, 5))) #iterador
iterador = iter(('holo', 4, 5))
print(next(iterador)) # primer valor del iterador es 'holo'

print(pow(2, 3)) #potencia ( 2**3 )
#sum
#sirve para sumar los elemento de listas, tuplas, sets, y claves de un diccionario
print(sum(list((1, 5, 7, 8))))
print(sum(dict(((1, 'uno'), (2, 'dos'))))) #sumar claves de un diccionario
#print(sum(diccionario.values()))#sumar valores de un diccionario

#eval
print(eval('5+3+100*3')) #realiza las operaciones en str = 308
num = 100
print(eval('num*3'))

#zill
numero= '19'# con 2 cifras
print(numero.zfill(4))# 4 cifras <-- 0019 (str)

#max y min de colecciones
print('Maximo de {3, 5}:', max(set((5, 3))))
print('Maximo de (5, 6, 7):', min(tuple((6, 5, 7))))
#otras como oct() es para un numero como octogonal, otras para empresas o algo asi son credits(), copyright(),

#importante
#para librerias
import math
funcionalidades = dir(math)#funciones, clases, modulos y elementos con...
print(funcionalidades)
#['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']