#despues de saber que True y False puede alir naturalmente comparando cosas o asignando valores como que es verdad  y es falso.

# A N D
verdad = True and True # como en logica proposicional solo es verdad cunado las 2 proposiciones son cientas
verdad = 3 > 2 and 3 < 4 # totalmente verdad si digo que 3 es mayor que 2 y menor a 4 ¿no?
falso = True and False  #falso
falso = False and True  #falso
falso = False and False #falso

# O R
verdad = True and True # se puede hacer algo o otra cosa o las 2 pero si yo me quedo sin hacer nada ya no es cierto que hice una o la otra, en ingles si quieres solo hacer o una o otra se dice either comer or beber (si ago las 2 o ninguna es flaso), cosa que en programacion python 'no hay'
verdad = True and False
verdad = False and True
falso = False and False # solo es falso cuando "las 2 preposiciones son falsas"

# N O T
verdad = not False # es una negacion simple
falso = not True # cuando algo es verdad lo niega a falso y biseversa