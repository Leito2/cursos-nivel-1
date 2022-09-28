// -----------------------
// ARRAYS COMUNES (listas)
// Es una variable la cual puede almacenar varios valores de distintos tipos y los llama del 0 para arriba.

// Estructura básica
/*
nombreLista = [valor, valor, valor];
----------------------------------------
misDatos = ['leandro', 24, true];
*/

// Llamar un elemento del array
/*
nombre = misDatos[0] = 'leandro'
(el último elemento sería el índice -1, como el penúltimo sería -2)
(mirarlos)
estado = misDatos['leandro'] = true <- (si lo encuentra)
*/


// --------------------------------
// ARRAYS ASOCIATIVAS (diccionario)
// Es una variable la cual puede almacenar varios valores de distintos tipos y los llama por su nombre.

// Estructura básica
/*
nombreListaAsociativa = {
  clave: valor,
  clave: valor,
  clave: valor
};
-------------------------
misDatos = {
  nombre: 'leandro',
  edad: 24,
  comida: true
};
*/

// Llamar un elemento del array asociativo
/*
nombre = lista['nombre'] = 'leandro'
*/


// -----------
// BUCLE WHILE
// parte de los bloques de control
// Es un condicional el cual si es false sigue el flujo del JS, pero si es true, repite la condición y luego el bloque de código.
// para un ciclo hay que haber un aumento o decremento para que este no sea infinito.

// Estructura básica
/*
while (condición) {
  bloque de código o iteración + aumento o decremento
};
------------------------------
let i = 0;
while (i < 10) {
  i++
  console.log(i);
};
(manda números de 1 al 9)
*/


// --------------me tira los números impares ya que al dividirlos entre 2 si da 0 entonces continua iterando
// Es un condicional el cual si es false sigue el flujo del JS, pero si es true, repite el bloque de código y luego hace la condición.


// Estructura básica
/*
do {
  bloque de código o iteración + aumento o decremento
} while (condición);
------------------------------
let i = 0
do {
  i++
  console.log(i)
} while (i < 10);
(manda números de 1 al 10)
*/


// ---------
// BUCLE FOR
// es un ciclo determinado ya que en su misma declaración y condición se define cuandas iteraciones se realizarán.

// Estructura básica
/*
for (let indice = valor; condición; aumento o decremento) {
  iteración o bloque de código
}
(a 'for (let indice = valor;) -> también se le puede llamar declaración)
-----------------------------------------------------------
for (let index = 1; index < 10; index++) {
  console.log(index)
}
(coloca los números de 1 al 9)
(se suma y luego se condiciona como while | index es una variable que solo va existir en ese bloque de código)
*/


// ------------
// BUCLE FOR IN
// es un ciclo determinado ya que utiliza un iterador como una lista para poder iterar n veces sus indices.

// Estructura básica
/*
let elementos = [valor, valor, valor];
for (elemento in elementos) {
  iteración o bloque de código
}
(recorre el indice o clave de cada elemento del iterador)
----------------------------------------------------------------------------------------------------
let elementos = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve'];
for (elemento in elementos) {
  console.log(elemento)
}
(coloca los números de 0 al 9 (sus indices))
*/


// ------------
// BUCLE FOR OF
// es un ciclo determinado ya que utiliza un iterador como una lista para poder iterar n veces sus valores.

// Estructura básica
/*
let elementos = [valor, valor, valor];
for (elemento in elementos) {
  iteración o bloque de código
}
(recorre el valor de cada elemento del iterador)
----------------------------------------------------------------------------------------------------
let elementos = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve'];
for (elemento in elementos) {
  console.log(elemento)
}
(coloca los números de 'cero' al 'nueve' (sus valores))
*/


// ------------------------
// INTERRUPCIONES DE BUCLES
// es un ciclo se pueden colocar condiciones internas en donde si ocurre algo se pare ese ciclo o continue la iteración sin haber terminado toda la iteración.

// Continue
/*
ciclo {
  condición {
    continue
  }
}
(continue lo que hace es dejar el resto de codigo de la iteración sin ejecutar y volver a la declaración y condición del ciclo)
-------------------------------------------------------------------------------------------------------------------------------
let i = 1;
while (i <= 10) {
  if (i%2 === 0) {
    i++;             <--- lo coloco porque sino se me queda en un número par
    continue
  }
  console.log(i);
  i++
}
(coloca: 1, 3, 5, 7, 9)
(me tira los números impares ya que al dividirlos entre 2 si da 0 entonces continua iterando)
*/

// Break
/*
ciclo {
  condición {
    break
  }
}
(break rompe el ciclo por completo, lo da por terminado)
--------------------------------------------------------
let i = 1
while (i <= 100) {
  if (i === 11) {}
    break
  }
  console.log(i)
  i++
}
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
(cuando llega a ser i igual a 11 se rompe el ciclo entrando a la condición)
*/


// ---------------
// LABEL EN BUCLES
// a la hora de llamar continue o break estamos afectando a ese bloque del ciclo.
// pero label sirve para afectar a un bucle más grande que ese mismo.

// Estructura básica
/*
nombreLabel:
ciclo {
  ciclo {
    break nombreLabel
  }
}
(el break se le hace al ciclo más grande)
-----------------------------------------
cicloMayor:
for (let i = 1; i <= 3; i++) {
  for (let j = 4; j <= 6; j++) {
    console.log(j);
    break cicloMayor
  }
  console.log(i)
}
(solo coloca 4 ya que entre al ciclo pequeto y rompio el ciclo grande despues de colocar j que es 4)
()
*/


// ---------
// FUNCIONES
// es una nueva utilidad reutiliable de código la cual nos ayuda a resumir, modularizar y acotar nuestro código.
// se le pueden pasar parámetros que son variables locales de la función

// Estructura básica declararla o crearla
/*
function nombre(parámetros) {
  Código de la función
}
(otra manera es)
const nombre = function(parámetros) {
  Código de la función
}
(otra manera es con función flecha (arrow function))
const nombre = (parámetros) => {
  Código de la función
}
(o)
const nombre = parámetro => {
  Código de la función
}
(si es solo un parámetro se puede dejar así)
(o para retornar una sola línea de código)
const nombre = parámetro => línea de código
[ESTAS FUNCIONES CON COMO LAS FUNCIONES LAMBDA DE PYTHON]
---------------------------------------------
function saludar(nombre) {
  console.log(`hola mi increíble ${nombre}`)
}
*/

// Estructura básica usarla
/*
nombre(argumentos)
(al usar la funcion los parámetros pasan a ser llamados argumentos)
---------------------------------------------
let miNombre = 'leandro';
saludar(miNombre);
let suNombre = 'david';
saludar(suNombre)
(en este caso saludé 2 veces a personas distintas)
*/


// Return
/*
function nombre(parámetros) {
  (Código de la función)
  return resultado
};
variable = nombre(argumentos) <--- resultado
---------------------------------------------
function sumar(a, b) {
  return a + b
};
variable = sumar(1, 5) <--- 6
*/


// ----------------------------------------
// MATRIZ (tablas)
// son arrays dentro de arrays.

// Definir
/*
tabla = [[lista], [lista], [lista]]
--------------------------------------
cosas = [['pera', 'banana'], ['pc', 'iphone']]
*/

// Llamar
/*
tabla[lista][elemento]
(es como elejir a nivel de listas y luego a nivel de elementos dentro de la lista seleccionada)
----------------------
cosas[0][1]='banana'
*/