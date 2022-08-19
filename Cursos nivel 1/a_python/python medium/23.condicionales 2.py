#otra manera if / else
print('3 es mayor a 2') if 3 > 2 else print('3 es menor a 2')
#(accion True) if (condicion) else (accion False)


#condicional range
numero = int(input('Escribir un numero: '))

if numero in range(10, 31):
    print('El numero esta en el rango 10 al 30')


# ANY Y ALL
numeros = [1, 3, 6]
numeras = (1, 2)

if all(son > 0 for son in numeros):#evalua que todos los que se retornen en all(los elementos de numeros), sean | mayores que 0 | (booleano)
    print('mis numeritos', numeros, 'son mayores que 0')
else:
    print('mis numeritos', numeros, 'no son mayores que 0 :C')
numeros = [1, 3, -6]
if all(son > 0 for son in numeros):
    print('mis numeritos', numeros, 'son mayores que 0')
else:
    print('mis numeritos', numeros, 'no son mayores que 0 :C')
if any(numero == 3 for numero in numeros):
    print(f'{numeros} Tiene un 3')
else:
    print(f'{numeros} no tiene 3')
if any(numero == 3 for numero in numeras):
    print(f'{numeras} Tiene un 3')
else:
    print(f'{numeras} no tiene 3')