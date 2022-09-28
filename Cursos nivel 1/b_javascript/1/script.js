// Es un lenguaje interpretado
// Es completamente orientado a objetos
// Imperativo: lee y ejecuta línea por línea
// Case sensitive: detecta mayúsculas y minúsculas
// Basado en prototipos-----------------------------no entendi bien
// Tipado déibil: no tienen tanta especificación de tipos de variable
// Lenguaje dinámico: Las variables se adapdan al dato(1+1 es 2 entero; a es 'a').

// --------------
// MANDAR ALERTAS
// alert(mensaje como ventana emergente)
// document.write(mensaje en documento)
// console.log(mensaje en consola)


// --------------
// TIPOS DE DATOS

// Entero (int)
// 1, 4, 7

// Flotante (float)
// 1.4, 3.1416

// Texto (string)
// "hola", "1" (comillas dobles)
// 'hola', '1' (comillas simples)
// `hola`, `1` (backticks o acento)

// Booleano (bool)
// true, false (a veces da 1 y 0)

// Especiales
// Undefined (si no se define el valor de una variable)
// Null (se define un valor vacío a una variable)
// Nan (Un valor erroneo a una variable)


// -----------------
// TIPO DE VARIABLES

// Const
// para declarar algo constante, su nombre en general en UPPERCASE.
// const GRAVEDAD = 9.81, const NACIMIENTO = '20/04/2005'
// (const no puede tener el valor undefined, esta se tiene que inicializar al inicio(definir el valor), ya que no se le podrá cambiar o asignar después)

// Let (Variable de poco alcance)
// para declarar algo que varia dinamicamente, su nombre en general con camelCase.
// let edadMia = 17, let limones = 3

// Var (Variable de alto alcance)
// como se verá en scope, si algo es declarado como var es algo global (camelCase).
// var numero = 3
// numero = 3 ( si no se coloca nada es como colocar var )

// -----
// SCOPE
// donde se puede contar como inicializado algo
/*

if (3==3) {
  var numero = 3
}
alert(numero)

(si fuera con let, solo se podría utilizar dentro del if)

*/

// --------
// HOISTING
// Como algo puede er inicializado despúes pero usado antes


// -----------
// PEDIR DATOS
// cont NOMBRE = prompt('Dime tu nombre: ')


// ----------------------
// OPERADORES DE ASIGNACIÓN
// x = y (son variables iguales)

// x += y (se le suma y a x)

// x -= y (se le resta y a x)

// x *= y (se multiplican x con y)

// x /= y (se dividen x con y (el cociente))

// x%= y (se divide x con y (el resto, no el cociente))

// x **= y (se potencia x en y veces)

// en todos se actualiza el valor de x


// ----------------------
// OPERADORES ARÍTMERICOS
// operaciones entre números

// Suma ( + )
// 1 + 4 (da 5)

// Resta ( - )
// 4 - 3 (da 1)

// Incremento ( ++ )
// 4++ (da 5 (se le suma 1))

// Decremento ( -- )
// 4-- (da 3 (se le resta 1))

// Multiplicación ( * )
// 3 * 4 (da 12)

// División ( / )
// 6 / 3 (da 2)

// División entera ( // )
// 7 / 3 (da 2)

// Potencia ( ** )
// 3 ** 3 (da 27)

// Resto ( % )
// 9 % 2 (da 1 (impar))

// Negar ( -number )
// -(9) (da -9)


// -------------
// CONCATENACIÓN
// es la unión literal de string o carrácteres

// Concatenación con +
// se hace una unión con carrácteres no numéricos
// 'hola ' + 'niño' = 'hola niño'

// Concatenación con + forzada
// se hace una unión con carrácteres no númericos y números
// 'hola' + 22 = 'hola22'
// '' + 1 + 1 = 11 (con un string vacío hace que el resto sea texto)

// Concatenación con .concat()
// saludo = 'hola'.concat(' bienvenido')
// 'hola bienvenido'

// Concatenación con ${}
/*
nombre = 'leito';
frase = `hola ${leito}` 
(solo funciona con los backticks)
*/

// Observaciones:
// si se usan comillas dobles, adentro solo se puede usar simples y biseversa
// si se usan backtricks se pueden usar las dos
// a esto se le llaman escapes


// -------------------------
// OPERADORES DE COMPARACIÓN
// compara 2 expresiones y devuelve un booleano

// Igualdad (a == b)
// 2 == 2 = true
// 2 == '2' = true
// 2 == 3 = false

// Desigualdad (a != b)
// 2 != 2 = false
// 2 != '2' = false
// 2 != 3 = true

// Identico (a === b) -> tambien evalua el tipo
// 2 === 2 = true
// '2' === '2' = true
// 2 === '2' = false
// 2 === 3 = false

// No Identico (a !== b)
// 2 !== 2 = false
// '2' !== '2' = false
// 2 !== '2' = true
// 2 !== 3 = true

// Mayor que (a > b)
// 3 > 2 = true
// 3 > 3 = false
// 3 > 4 = false

// Mayor o igual que (a >= b)
// 3 >= 2 = true
// 3 >= 3 = true
// 3 >= 4 = false

// Menos que (a < b)
// 3 < 4 = true
// 3 < 3 = false
// 3 < 2 = false

// Menor o igual que  (a <= b)
// 3 <= 4 = true
// 3 <= 3 = true
// 3 <= 2 = false



// ------------------
// OPERADORES LÓGICOS

// Copulativa (valor && valor)
// true && true = true
// true && false = false
// false && true = false
// false && false = false

// Disyuntiva (valor || valor)
// true || true = true
// true || false = true
// false || true = true
// false || false = false

// Negativa (!valor)
// !true = false
// !false = true


// ----
// TIPS

// las constantes van con UPPERCASE (se llaman también raw (all caps))
// las variables van con camelCase
// los objetos y clases van con PascalCase (en ocaciones los objetos no)
// todo en HTML y CSS va con kebab-case

// todo en python va con snake_case
// la normal es lowercase (se llaman también raw)


// 
// CONDICIONALES
// parte de los bloques de control

// Estructura básica
// If
/*
if (condición) {
  sentencia
}
---------------------------------
if (true) {
  Se ejecuta lo que hay aca
}
---------------------------------
if (false) {
  No se ejecuta lo que hay aca
}
*/

// Estructura básica
// Else
/*
if (condición) {
  sentencia
} else {
  Sentencia recursiva
}
---------------------------------
if (true) {
  Se ejecuta
} else {
  No se ejecuta
}
---------------------------------
if (false) {
  No se ejecuta
} else {
  Se ejecuta
}
*/

// Estructura básica
// Else if
/*
if (condición) {
  sentencia
} else if (condición secundaria) {
  sentencia secundaria
} else {
  Sentencia recursiva
}
---------------------------------
if (true) {
  Se ejecuta
} else if (false) {
  No se ejecuta
} else {
  No se ejecuta
}
---------------------------------
if (false) {
  No se ejecuta
} else if (true) {
  Se ejecuta
} else {
  No se ejecuta
}
---------------------------------
if (false) {
  No se ejecuta
} else if (false) {
  No se ejecuta
} else {
  Se ejecuta
}
-----------------------------------------------------
(pueden ir cuanyas sentencias se quieran con else if)
*/


// ------------------
// CONVERTIR A ENTERO
// parseInt('3') = 3