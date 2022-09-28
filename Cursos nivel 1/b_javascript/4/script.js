// MÉTODOS DE CADENAS
let cadena = new String('cadena de prueba')   // recordar que las cadenas son inmutables
//let cadena = 'cadena de prueba';           // lo mismo
console.log(cadena.length);               // numero de carracteres (carracterpistica en realidad de arrays)

console.log(cadena.concat(' hola'));      // Es como contatenar o unir algo al final

console.log(cadena.startsWith('cadena'));     // cadena inicial
console.log(cadena.endsWith('prueba'));      // cadena final
console.log(cadena.includes(' de '));       // cadena incluida
console.log(cadena.indexOf('d'));          // indice inicial de cadena incluida
console.log(cadena.lastIndexOf('d'));     // indice final de cadena incluida
console.log(cadena.indexOf('z'));        // indice -1 si no la encuentra

console.log(cadena.padStart(20, '12'));       // rellenar al inicio si no llega a más de 20 carrácteres
console.log(cadena.padEnd(20, '12'));        // rellenar al final si no llega a más de 20 carrácteres
console.log(cadena.repeat(2));              // repetir la misma cadena n cantidad de veces

let resultado;

resultado = cadena.split(' ');                // crea una lista separando elementos por la sección de cadena que le metamos
//resultado: [ 'cadena', 'de', 'prueba' ]
resultado = ['cadena', 'de', 'prueba'];
resultado = resultado.toString();          // volver a convertir a string (es como una variación de join)
//resultado: 'cadena,de,prueba'

resultado = cadena.substring(0, 6);           // crea una nueva cadena con los indices iniciales y finales de la cadena original
//resultado: 'cadena'
// comienza en 0 y termina en 6 sin incluir por lo que termina en la 5
// (incio, final) o (inicio) <-- si se coloca solo el inicio el va hasta el ultimo carrácter

resultado = cadena.toLowerCase();             // crea una nueva cadena en minúsculas
//resultado: 'cadena de prueba'
resultado = cadena.toUpperCase();           // crea una nueva cadena en mayúsculas
//resultado: 'CADENA DE PRUEBA'

resultado = '   hola   ';
resultado = resultado.trim();                 // eliminar carrácteres espacio del inicio y el final
//resultado: 'hola'
resultado = resultado.trimStart();          // eliminar carrácteres espacio del inicio
//resultado: 'hola   '
resultado = resultado.trimEnd();          // eliminar carrácteres espacio del final
//resultado: '   hola'


// obviando que existe la propieda lista.lenght en arrays
// MÉTODOS DE ARRAYS ( TRANSFORMADORES )
// modifican el array padre y retornan un valor

let lista;

lista = ['pedro', 'maría', 'jorge'];
let pop = lista.pop();                        // quita y retorna el ultimo elemento del array
//pop: 'jorge'
//lista: ['pedro', 'maría']
let shift = lista.shift();                    // quita y retorna el primer elemento del array
//shift: 'pedro'
//lista: ['maría']

lista = ['pedro', 'maría', 'jorge'];
let push = lista.push('leo', 'leito');        // coloca 'leo' y 'leito' al final y retorna la nueva cantidad de elementos
//push: 5
//lista: ['pedro', 'maría', 'jorge', 'leo', 'leito']
let unshift = lista.unshift('nico', 'laura'); // coloca 'nico' y 'laura' al inicio y retorna la nueva cantidad de elementos
//unshift: 7
//lista: ['nico', 'laura', 'pedro', 'maría', 'jorge', 'leo', 'leito']

lista = ['nico', 'laura', 'pedro', 'maría', 'jorge', 'leo', 'leito'];
let sort = lista.sort();                      // ordena la array(ordena según carrácteres) y la retorna
//sort:  ['jorge', 'laura', 'leito', 'leo', 'maría', 'nico', 'pedro'];
//lista: ['jorge', 'laura', 'leito', 'leo', 'maría', 'nico', 'pedro'];
let reverse = lista.reverse();                      // ordena al revés la array(ordena según carrácteres) y la retorna
//reverse: ['pedro', 'nico', 'maría', 'leo', 'leito', 'laura', 'jorge']
//lista:   ['pedro', 'nico', 'maría', 'leo', 'leito', 'laura', 'jorge']

lista = ['nico', 'laura', 'pedro', 'maría', 'jorge', 'leo', 'leito'];
let splice = lista.splice(1, 5, '|', 'vs', '|');  // (inicio, eliminados, agregar, agregar...) lo que hace es en un punto eliminar n elementos y agregar distintos elementos
//splice: ['laura', 'pedro', 'maría', 'jorge', 'leo'] <-- retorna lo que elimina como si fuera un pop
//lista:  ['nico', '|', 'vs', '|', 'leito']


// MÉTODOS DE ARRAYS ( ACCESORES )
// no modifican el array pero retornan un valor

lista = ['nico', 'laura', 'pedro', 'maría', 'jorge', 'leo', 'leito'];
let join = lista.join();                      // convierte el array en un string con un separador(por defecto ',')
//join: nico,laura,pedro,maría,jorge,leo,leito
join = lista.join(' ');                     // en un document.write se podría colocar cosas como <br>Elemento: (esto iría antes de cada elemento)
//join: nico laura pedro maría jorge leo leito
// para listas también esta toString() sin embargo es mejor usar este igual

lista = ['nico', 'laura', 'pedro', 'maría', 'jorge', 'leo', 'leito'];
let slice = lista.slice(1, 2);                      // coge elementos de un array (inicio, final) (no incluye final)
//slice: ['laura']
slice = lista.slice(-1);                      // coge elementos de un array (inicio)
//slice: ['leito']

//entre splice y slice, splice(los quita y se los queda y pone más), slice(se los queda pero no los quita)
// slice es como substring(inicio, final)

// METODOS DE ARRAY QUE HAY EN CADENAS

lista = ['nico', 'laura', 'pedro', 'maría', 'jorge', 'leo', 'leito'];

console.log(lista.includes('maría'));       // elemento incluido
//dice: true
console.log(lista.indexOf('laura'));          // indice inicial de elemento incluido
//dice: 1
console.log(lista.lastIndexOf('leo'));     // indice final de elemento incluido
//dice: 5
console.log(lista.indexOf('z'));        // indice -1 si no la encuentra el elemento
//dice: -1


// MÉTODOS DE REPETICIÓN

lista = ['nico', 'laura', 'pedro', 'jorge', 'leo', 'leito'];

let forEach = lista.forEach(elemento => {
  console.log(`elemento ${lista.indexOf(elemento)}: ` + elemento)
}); // sirve para ejecutar una función que recorra un bloque de código por cada elemento
//dice:
/*
elemento 0: nico
elemento 1: laura
elemento 2: pedro
elemento 3: jorge
elemento 4: leo
elemento 5: leito
*/

lista = ['nico', 'laura', 'pedro', 'jorge', 'leo', 'leito'];

let filter = lista.filter(elemento => elemento.length > 4);  // utilia una función en este caso se le puede colocar la arrow function 
//filter: [ 'laura', 'pedro', 'jorge', 'leito' ] <-- los filtra si tienen más de 4 letras

filter = lista.filter(elemento => {
  console.log('holi');
  return elemento.length > 4  //como tieme más de 1 línea tengo que colocar return
}); // puede ser utilizado como forEach además de filtrar al mismo tiempo en una listas
//dice:
/*
holi
holi
holi
holi
holi
holi
*/
//filter: ['laura', 'pedro', 'jorge', 'leito']


// MATH
// un objeto interno de javascript

console.log(Math.sqrt(4)); // raíz cuadrada de 4 es 2
//dice: 2
console.log(Math.cbrt(64)); // raíz buadrada de 64 es 4
//dice: 4
console.log(Math.pow(4, 0.5)); // 4 elevado a la 0.5 (raíz)
//dice: 4

console.log(Math.min(64, 5, 67)); // el valor más pequeño
//dice: 5
console.log(Math.max(64, 5, 67)); // el valor más grande
//dice: 67

console.log(Math.random()); // número aleatorio entre 0 y 1
//dice por ejemplo: 0.15

console.log(Math.round(3.5)); // redondea al más cercano sin embargo si es .5 entonces va a el superior
//dice: 4
console.log(Math.floor(4.9999)); // redondea al entero menor (o como la funcion del mayor entero menor a n)
//dice: 4
console.log(Math.ceil(3.0001)); // redondea al entero mayor (o como la funcion del mayor entero menor a n+1)
//dice: 4
console.log(Math.trunc(4.99)); // quita decimales
//dice: 4
console.log(Math.fround(4.9999)); // redondea al binario de precisión simple (4 bytes) más cercano
//dice: 4.999899864196777


console.log(Math.PI); // número pí: 3.141592653589793238462643383279502884 (sin embargo aparece la presición simple)
console.log(Math.E);  // número e: 2.718281828
// Math.LN10 (logarítmo natural de 10), Math.LOG2E (logarítmo base 2 de e)


