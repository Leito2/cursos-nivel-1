// Programación orientada a objetos

// Es un paradigma o concepto principal y padre de JavaScript.
// El cual nos ayuda a crear clases y objetos.


// -----
// CLASE
// Es la definición de un tipo de objetos y de su estructura interna

// Estructura básica 
/*
class NombreClase {
  constructor(parametro1, parametro2, parametro3) {   <- CONSTRUCTOR es obligatorio
    this.parametro1 = parametro1;
    this.parametro2 = parametro2;
    this.parametro3 = parametro3
  }
}
-------------------------------------------------------------------
class Animal {
  constructor(especie, edad, color) {
    this.especie = especie;
    this.edad = edad;
    this.color = color;
    this.lindo = true    <-- se pueden colocar más carracterísticas
  }
}
(está creando un animal con carracterísticas como especie, edad, color)
*/


// ------
// OBJETO

// Estructura básica 
/*
(crear)
const NombreObjeto = new nombreClase(argumento1, argumento2, argumento3)
// ATRIBUTOS
(para acceder)
nombreObjeto.parametro1 = argumento1;
nombreObjeto.parametro2 = argumento2;
nombreObjeto.parametro3 = argumento3
--------------------------------------------------------------------------------------------
const rayo = new Animal('perro', 9, 'amarrillo')   <-- esto seria instanciar o crear un objeto
console.log(rayo)
( aparece:
Animal {
  color: 'amarillo',
  edad: 9,
  especie: 'perro'
} )
(si ahora se puso naranjado solo colocar rayo.color = 'naranjado' y mostrarlo con console.log('Soy de color: ' + rayo.color))
*/


// -------
// MÉTODOS
// Son las habilidades de una clase de lo que se puede hacer (son funciones dentro de las clases).
/*
class NombreClase {
  constructor (parametro1, parametro2, parametro3) {   <- CONSTRUCTOR es obligatorio
    this.parametro1 = parametro1;
    this.parametro2 = parametro2;
    this.parametro3 = parametro3
  };
  metodoClase (parámetros) {
    Bloque de código de la función
  }
}
(las funciones flecha no pueden ser usadas para crear metodos)
----------------------------------------------------------------------------------------------------
class Animal {
  constructor(especie, edad, color) {
    this.especie = especie;
    this.edad = edad;
    this.color = color
  };
  saludar () {
    console.log(`hola soy un ${this.especie}, tengo ${this.edad} años y soy de color ${this.color}.`)
  }
}
(luego los metodos se llaman como una función pero con el nombre del objeto antes)
rayo.saludar()
(hola soy un perro, tengo 9 años y soy de color naranja)
*/


// ---------------
// OTROS CONCEPTOS

// Abstracción
// Tratar de resumir un objeto lo más posible tratar de simplificar sus componentes básicos.

// Modularidad
// Dividir un problema en componentes o en pedazos para reducir su complejidad y la mantener una unidad con cada componente que creemos.
// por ejemplo modularizar con funciones.

// Encapsulamiento
// Es tratar de que la información o datos se mantengan seguros y no al alcance del cliente.

// Polimorfismo
// Como un objeto maneja un metodo de forma distinta a otro objeto de su misma clase por las propiedades que tiene.
// por ejemplo si un conejo camina en 2 patas esto ya lo afecta en su metodo .caminar()(se podría mirar con condicionales de cuantas patas tiene o algo así).


// --------
// HERENCIA
// No todos los animales ladran por lo que para un animal heredar carrácteristicas solo de caninos, entonces se utiliza la herencia.
// Esta es una forma de modularización ya que se pueden crear otras clases generales para encerrar carrácteristicas heredables.
// Heredar es como tener 2 o más clases un objeto.

// Estructura extends
/*
class NombreClaseHeredada extends NombreClase {
  constructor (parametro1, parametro2, parametro3, parametro4) {   <-- ahora hay 4 parámetros
    super(parametro1, parametro2, parametro3);                     <-- herede los 3
    this.parametro4 = parametro4                                   <-- creé un 4
  };
  metodoDeLaOtraClase (parámetros) {                               <-- metodo separado a la clase original
    Bloque de código de la función
  }
}
(se hereda todo lo de la clase NombreClase y además consige otras cosas)
(y para crear el objeto con '2 clases')
const NombreObjeto = new NombreClaseHeredada(argumento1, argumento2, argumento3, argumento4)
----------------------------------------------------------------------------------------------------------
class Perro extends Animal {
  constructor(especie, edad, color, raza) {
    super(especie, edad, color);
    this.raza = raza
  };
  ladrar () {
    console.log('¡Waw!')
  }
}
const rayo = new Perro('perro', 9, 'amarrillo', 'pincher');
rayo.ladrar()
(rayo es animal y además tiene carracterísticas perro)
*/


// -----------------
// METODOS ESTÁTICOS
// Es un metodo en donde no se utilizan carracterísticas del constructor.

// Estructura básica
/*
class NombreClase {
  constructor (parametro1, parametro2, parametro3) {
    this.parametro1 = parametro1;
    this.parametro2 = parametro2;
    this.parametro3 = parametro3
  };
  static metodoEstaticoClase (parámetros) {
    Código sin uso de this.parametros
  }
}
(para llamarlo sin crear objetos o instanciar es con)
NombreClase.metodoEstaticoClase(argumentos)
----------------------------------------------------
class Animal {
  constructor(especie, edad, color) {
    this.especie = especie;
    this.edad = edad;
    this.color = color
  };
  static saludar (aspecto) {
    console.log(`hola soy un animal ${apecto}`)
  }
}
Animal.saludar('lindo') <-- se podría llamar directamente la clase para invocar el metodo estático
(dice: hola soy un animal lindo)
*/

// -----------------
// METODOS GET y SET
// Es un metodo GET en donde se retorna un valor y SET en donde se pide un parametro de un metodo, colocando el argumento como valor de una variable.

// GET
/*
class NombreClase {
  constructor (parametro1, parametro2, parametro3) {
    this.parametro1 = parametro1;
    this.parametro2 = parametro2;
    this.parametro3 = parametro3
  };
  get metodoSetClase () {
    retornar un valor
  }
}
(para llamarlo)
variable = NombreObjeto.metodoGetClase()
----------------------------------------------------
class Animal {
  constructor(especie, edad, color) {
    this.especie = especie;
    this.edad = edad;
    this.color = color
  };
  get aspectoAnimal () {
    return 'lindo'
  }
}
aspecto = rayo.aspectoAnimal() <-- Estoy obteniendo un valor
(la variable agarró el valor de 'lindo')
*/

// SET
/*
class NombreClase {
  constructor (parametro1, parametro2, parametro3, parametro4) {
    this.parametro1 = parametro1;
    this.parametro2 = parametro2;
    this.parametro3 = parametro3;
    this.parametro4 = null   <-- por ejemplo cuando no se define a la primera un valor
  };
  set metodoSetClase (parámetro) {
    this.parametro4 = parámetro
  }
}
(para llamarlo)
NombreObjeto.metodoSetClase = argumento
----------------------------------------------------
class Animal {
  constructor(especie, edad, color, viejo) {
    this.especie = especie;
    this.edad = edad;
    this.color = color;
    this.viejo = null
  };
  set vejesAnimal (vejes) {
    this.viejo = vejes
  }
}
const rayo = new Animal('gato', 10, 'blanco');
rayo.vejesAnimal = true;
console.log(rayo)
(Animal { especie: 'gato', edad: 10, color: 'blanco', viejo: true })
(el valor false se guardo en la variable que es un metodo set de una clase)
*/