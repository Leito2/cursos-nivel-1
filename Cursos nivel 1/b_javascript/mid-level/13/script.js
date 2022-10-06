// CALLBACKS
// es una función con un parámetro que es y se convierte en función
// es como una función que se le pasa como parámetro otra función

// Estructura básica
/*
function nombreFunción (nombreCallBack, parámetros) {
  ──más código de la función──
  nombreCallBack(argumentos)
}
function nombreCallBack (parámetros) {
  ──Código de la función call back──
}
nombreFunción(nombreCallBack, argumentos)
─────────────────────────────────────|
function funcion (callback, nombre) {          ←función normal
  callback(nombre)
}
function decirNombre (nombre) {          ←función call back
  console.log('su nombre es: ' + nombre)
}
funcion(decirNombre, 'leandro')
─────────────────────────────────────
(dice: 'leandro')
─────────────────────────────────────|
*/


// PROMISE
// las promesas son un tipo de manejo de callbacks especial

// Estructura «
/*
const nombrePromesa = new Promise((resolve, reject) => {
  if (condición) {
    resolve(response)    ← esto se retorna
  } else {
    reject(error)        ← o esto se retorna
  }
})
nombrePromesa
  .then(response => {
    ──Código con el parámetro response──
  })
  .catch(error => {
    ──Código con el parámetro error──
  })
─────────────────────────────────────────────────────────────────────────────────────────────|
let nombre = 'leandro';
const promesa = new Promise((resolve, reject) => { (aca se hace un tipo de manejo de errores)
  if (nombre === 'leandro') {
    resolve('leandro')
  } else {
    reject('no eres leandro')
  }
})
promesa
  .then(response => {
    console.log('Response:', response)
  })
  .catch(error => {
    console.log('Error:', error)
  })
─────────────────────────────────────────────────────────────────────────────────────────────
dice Response: leandro // sino diría: Error: no eres leandro
─────────────────────────────────────────────────────────────────────────────────────────────|
*/

// Estructura más completa «
// resolve | es como el resultado de un flujo normal
// reject  | es como el error
/*
const promesa1 = ((parámetros) => {
  return new Promise((resolve, reject) => {
    if (condición) reject(error)
    else resolve(response)        ← o el error o el response puede ir antes
  })
}) ← creando una función con parámetros para retornar las promesas para manejar con then
const promesa2 = ((parámetros) => {
  return new Promise((resolve, reject) => {
    if (condición) resolve(response)
    else if (condición) resolve(response) ← pueden haber else if pero con el response
    else reject(error)
  })
}) ← creando la segúnda función para manejar con el segúndo then
// si una función con parámetros retorna una promesa, puede ser manejada con .then
promesa1(argumentos)
  .then(response => {
    ──Código con el parámetro response──
    return promesa2(argumentos)    ← para que el otro then suceda, tiene que RETORNAR OTRA PROMESA
  })
  .then(response => {              ← aunque da igual que nombre de parámetro coloquemos
    ──Código con el parámetro response── ← este sería el response de la segúnda función
  })
  .catch(error => {
    ──Código con el parámetro error──
  })
(si alguna función en el manejo del .then tiene un error o un reject, este se salta el resto de funciones y ejecuta el .catch)
──────────────────────────────────────────────────────────────────────────────────────────────────|
let pera = {
  nombre: 'roberto',
  color: 'verde'
};
let manzana = {
  color: 'rojo'
};
let banano = {
  nombre: 'pedro'
};
const obtenerNombre = (fruta => {
  return new Promise((resolve, reject) => {
    if (fruta.nombre == undefined) reject('No tiene nombre')
    else resolve('Su nombre es: ' + fruta.nombre)
  })
})
const obtenerColor = (fruta => {
  return new Promise((resolve, reject) => {
    if (fruta.color == undefined) reject('No tiene color')
    else resolve('Su color es: ' + fruta.color)
  })
})
obtenerNombre(banano)
  .then(response => {
    console.log(response);
    return obtenerColor(banano)
  })
  .then(response => {
    console.log(response)
  })
  .catch(error => {
    console.log('Error:', error)
  })
(dice:
Su nombre es: pedro
Error: No tiene color
)
(con manzana no daría ya que saltaria el segundo then y pasaría al catch porque daría un error)
──────────────────────────────────────────────────────────────────────────────────────────────────|
*/


// FUNCIONES ASINCRONAS
// ASYNC | AWAIT
// Estas funciones surgén porque en el momento de obtener un response de una promesa con .then, se puede resivir un dato, pero si se ejecuta otro .then no se espera que el anterior se resiva, sino que también se ejecuta de manera sincronica, o a la vez que el otro .then.
// por lo que en una función Asycn se pueden obtener response en una variable con Await, una tras otra asincronicamente en tiempos conecutivos (otra diferencia es que se resive en una variable no en un parámetro)

// Estructura
/*
const promesa1 = ((parámetros) => {
  return new Promise((resolve, reject) => {
    ──código con: resolve(response)──   ← en await no persibe el reject o error
  })
}) ← creando una función con parámetros para retornar las promesas para manejar con await
const promesa2 = ((parámetros) => {
  return new Promise((resolve, reject) => {
        ──código con: resolve(response)──
  })
}) ← creando la segúnda función para manejar con el segúndo then

async function nombreFuncionAsincrona (parámetros) {
  variable1 = await promesa1(argumentos)   ← aca se resibe un response
  variable2 = await promesa2(argumentos)   ← aca se resibe el otro response
  ──Código con los parámetros response──
}
(se podría decir que no hay catch. Si tardan en llegar los datos, las variables de irían definiendo en orden de que se pidan)
[luego se llamaría con:
nombreFuncionAsincrona()
]
[otra estructura:
const nombreFuncionAsincrona = async (parámetros) => {
}
]
*/