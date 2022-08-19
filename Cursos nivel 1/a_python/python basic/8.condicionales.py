# C O N D I C I O N A L E S
#en diagramas de flujo se representan como un rombo y sirven para dividir el camino de un algoritmo entre True y False

# I F   |   E L I F     |   E L S E
numero = int(input('Escribir un numero: '))

if numero > 1: # si la condicion se cumple entra a que el numero es mayor a 1
    print(f'{numero} es mayor a 1')

elif numero == 1: # elif puede estar cuantas veces quiere y es otra opcion if pero que esta unida al if principal entonces si este da el elif no se compara si booleano y nunca entra, pero si el if principal no da, los elif se evaluan
    print(f'{numero} es igual a 1')

else: # si ni el if principal ni los secundarios entrar o son True, entonces else se realiza
    print(f'de seguro que {numero} es menor a 1')