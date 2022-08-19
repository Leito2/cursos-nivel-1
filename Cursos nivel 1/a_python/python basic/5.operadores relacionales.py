#Primero para saber que son los operadores que relacionan, tenemos que saber que estos unicamente pueden dar 2 valores; exacto los booleanos o los binarios, dan True o False

# M A Y O R     Y   M E N O R
verdad = 2 > 1 #el 2 es mayor a
falso = 2 < 2 #el 2 no es menor a 2, aunque si es igual (pero no biene al caso)

# M A Y O R (O IGUAL)   Y   M E N O R (O IGUAL)
verdad = 3 >= 1 # el 3 es mayor al 1, al 2 y igual al 3, por lo que es verdad, hablando de flotantes como enteros
verdad = 3 >= 3 # es True porque 3 es igual a 3 pero no mayor, pero si igual
falso = 3 <= 2 # el 3 no es menor ni tampoco igual a 2

# I G U A L D A D
verdad = 3 == 3.0 # esto es true y es que el valor que tienen los 2 es exactamente el mismo
falso = '3' == '3.0' # pero si los comvertimos a string ya no serian lo mismo y esto es False
falso = 3 is '3' #esto es decir si algo es el mismo objeto en memoria que otro, por ejemplo para cuando una lista se escribe igual para otra variable

# D E S I G U A L D A D
verdad = 3 != 4 # True: 3 es diferente de 4
falso = 3 != 3 # False: 3 es igual a 3 por lo que NO son diferentes