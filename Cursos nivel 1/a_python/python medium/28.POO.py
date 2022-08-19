'''
class NombreDeClase():
    def __init__(self,Parametro1,Parametro2):
        self.Parametro1 = Parametro1
        self.Parametro2 = Parametro2
    def OtraFuncion(self):
        (conjunto de acciones)
        return o print(self.Parametro1)

sabiendo que self es nuestro objeto
'''
from turtle import color


class perro(): #recomendado colocar las camelCase siempre
    def __init__(self, raza, nombre, color, puntos=False):#self es el nombre de la clase
        #Atributos
        self.raza = raza#siempre se hace esto para luego crear otras funciones que usen self(todas lo usan xD)
        self.nombre = nombre
        self.color = color
        #valor boolean True or False
        self.puntos = bool(puntos)
    def tengo_puntos(self):#definir funcion la cual utilizare con NombreDeClase.NombreFuncion()
        if self.puntos:
            print('Tengo manchas')
        else:
            print('No tengo manchas')
huskie = perro(raza='huskie', nombre='Sam', color='blanco', puntos=True)#definir una clase de perro (huskie) < es el self
pincher = perro(raza='pincher', nombre='Canela', color='negra')#si no definimos puntos, es False
lista_perros= (huskie, pincher)#tupla :v
for doge in lista_perros:
    if doge.raza == 'huskie':#(nombre de clase.parametro despues de self)
        print(f'{doge.nombre} es huskie y {doge.color}')
    else:
        print(f'{doge.nombre} es {doge.color} pero no es huskie, es {doge.raza}')#compilacion > al usar{} y format o ''+''
    print(doge.puntos)
print()
print('Ahora')
print(huskie.nombre)
huskie.tengo_puntos()#llamar funciones de clase
print(pincher.nombre)
pincher.tengo_puntos()
print('\n')

#herencia: utilizar una clase ya definida para crear otra clase, como una herencia de la clase principal
#polimorfismo: darle varias formas a una clase con varias clases

print('polimorfismo y herencia')
print()
class Animal():
    def __init__(self, animal):
        print('Animal creado')#funcion inicial de la clase principal
        self.animal = animal
    def quien_soy(self):#funcion a utilizar
        print(f'soy un {self.animal}')
    def comer(self):#funcion de más
        print('estoy comiendo')

class Perro(Animal):#herencia
    def __init__(self, animal, color):#parametros que tiene que tenr la clase
        Animal.__init__(self, animal)#llamar la funcion inicial de la funcion principal con el parametro de self(obvio) y animal (de la class Perro)
        Animal.quien_soy(self)#llamar funcion de la funcion principal con self(siempre)
        if self.animal=='perro':#en donde mira si el parametro animal de la clase perro, es 'perro'
            print('Perro creado')#imprime esto
        self.color = color#    |Es para volver a
        self.animal = animal#  |definir más funciones(a parte de la default (se inicia sola))
    def quien_soy(self):# solo para ejecutar en perros(por eso coloco un condicional en linea 24 y 28)
        print(f'soy un perro {self.color}')# si el condicional se cumple, coloca esto y el color del perro

Canela= Perro('perro', 'negro')#definir el self(Canela), en la clase Perro
if Canela.animal=='perro':#El condicional
    Canela.quien_soy()
print()
leo= Perro('conejo', 'negro')#hacer lo mismo que con la clase de perro Canela
if leo.animal=='perro':#el segundo condicional
    leo.quiensoy()
print('\n')

#otra ejemplo para ejecutar una clase y || __str__ || (ejecutar como texto el nombre de una clase(self))
print('__str__')
class Persona:
    def __init__(self, nombre, edad, colorfav):
        self.nombre= nombre
        self.edad = edad
        self.colorfav = colorfav
    def __str__ (self):#representar self(como un teto) para saber a que nos referimos de la persona
        return (f'Nombre: {self.nombre}\nEdad: {self.edad}\nColor Favorito: {self.colorfav}')
juanito = Persona('juanito', 17, 'blanco')#tambien se puede carracterizar una clase de esta manera
print(juanito) #el __str__
print()
print(f'Juanito tiene {juanito.edad} años')
print('\n')

#jerarquia de herencia basica

print('jerarquia de herencia basica')
class Persona:
    def __init__(self, documento, nombre, correo):
        self.documento = documento
        self.nombre = nombre
        self.correo = correo


class Estudiante(Persona):
    def __init__(self, documento, nombre, correo, carnet, carrera):
        super().__init__(documento, nombre, correo)#para llenar la clase (Persona) de la funcion init
        self.carnet = carnet#                       super() se utiliza para llamar funciones de persona
        self.carrera = carrera#                     es igual a Persona.__init__(self, documento, nombre, correo)


german = Estudiante('123', 'Germán', 'german@gmail.com', '987', 'Computación')
print(isinstance(german, Estudiante))#mirar si la persona pertenece a la clase o tipo(type) Estudiante
print(isinstance(german, Persona))#lo mismo pero con Persona