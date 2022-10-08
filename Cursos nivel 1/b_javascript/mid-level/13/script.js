// JSON
// es un tipo de objeto especial usado para procesos con el protocolo HTTP
// la diferencia entre una lista asociativa y un json es que las claves se colocan en comillas como en un diccionario de python:
// esta diferencia es porque en el momento de mandar información sin comillas al servidor pueden haber muchos problemas
/*
let nombreObjetoJson = {
  'nombre': 'leandro',
  'edad': 17
}
console.log(nombreObjetoJson); ← es como un objeto normal
console.log(nombreObjetoJson.nombre); ← se accede como un objeto normal
*/


// SERIALIZACIÓN Y DESERIALIZACIÓN
// se necesita serializar un json para poder mandarlo en texto a la red
/*
let nombreJson = {
  'nombre': 'leandro',
  'edad': 17
} ← deserializado
( se puede serializar con JSON.stringify() (es como comvertir a texto))
let nombreSerializarJson = JSON.stringify(nombreJson); ← pasar de un json deserializado a un json serializado
(
`{
  "nombre": "leandro",
  "edad": 17
}` (a esto lo convierte JSON.stringify())
)
let nombreStringJson = '{"nombre":"leandro","edad": 17}' // serializado (otra manera)
(solo deja deserializarlo con estas comillas en este orden)
let nombreDeserializarJson = JSON.parse(nombreStringJson); // pasar de un json serializado a un json deserializado
(
{
  "nombre": "leandro",
  "edad": 17
} (pasa a ser esto con JSON.parse())
)
*/


// Estados de petición
/*
404: error 404 no se encontraron recursos
403: error 403 no se tiene acceso a recursos
201 | 200: se tuvo acceso correcto al recurso
...
*/
// codigo de respuesta 3-4, stado 200 o 201

// PETICIONES AJAX

// Crear petición AJAX
// se tiene que estar en un servidor
/*
const request = new XMLHttpRequest();
(para microsoft explorer:)
const request = new ActiveXObject('Microsoft.XMLHTTP')
*/

// Petición GET con AJAX
/*
request.open("GET","archivo.txt");
request.send();
(resivimos el archivo con '{"nombre" : "leandro", "edad" : 17}')
*/

// Diferencias entre GET y POST
/*
-Los datos son visibles en el metodo GET, en el POST no
-Los datos pueden estar en el historial en GET, en el POST no
-GET se da pur URL por lo que tiene límite de datos de 2083
-POTS no admite texto con datos binarios
-los datos con GET se podrían recuperar con el caché
-es más facil hackear datos con un metodo GET
*/
// Petición POST con AJAX
/*
request.open("POST","https://page.com");
(al enviar un con POST se necesita un encabezado que determine el tipo de dato)
(con json:)
request.setRequestHeader('Content-type', 'application/json;charset=UTF8')
(luego lo enviamos)
request.send(JSON.stringify({
  'nombre': 'leandro',
  'edad': 17
})); ← le enviamos este json serializado
(enviamos el archivo con POST y luego lo podemos ver)
*/

// Obtener los datos
// el archivo solo se puede viualizar cuando tenga un código de respuesta de 4 y un estado 200 o 2001, por lo que así se puede monitorear
/*
request.addEventListener('readystatechange', () => { ← se activa cada que cambia el código de respuesta
  if (request.readyState >= 3 && (request.status == 200 || request.status == 201)) {
    let respuesta = request.response; ← lo trae serializado
    console.log(JSON.parse(respuesta)) ← lo deserializamos
  } else {
    console.log('no se cargo de forma completamente correcta')
  }
})
(ahora hay otra forma)
request.addEventListener('load', () => {
  if (request.status == 200 || request.status == 201) {
    let respuesta = request.response;
    console.log(JSON.parse(respuesta))
  } else {
    console.log('no se cargo de forma completamente correcta')
  }
})
*/


// PETICIONES FETCH

// GET
/*
const request = fetch('https://page.com'); ← esto devuelve una promesa
(con text)
request
  .then(response => response.text()) ← como la promesa esta encapsulada, nos regresa con .text() en json con stringify
  .then(response => console.log(JSON.parse(response))); ← ya podemos usar el string si deserializarlo
(con json)
request
  .then(response => response.json()) ← nos regresa con .json() en json convertido
  .then(response => console.log(JSON.stringify(response))); ← ya podemos usar el json y serializarlo
*/

// POST
/*
const request = fetch('https://page.com', { // segúndo parámetro un objeto para configurar headers
  method: 'POST', // especificar que es post
  body: JSON.stringify({ // aca va el archivo json serializado
    'nombre': 'leandro'
  }),
  headers: {'Content-type': 'application/json'} // cabecera y valor de cabecera
});
( blob (sirve por ejemplo para representar imagenes) )
const imagen = document.querySelector('.imagen');
request
  .then(response => response.blob()) ← nos regresa un objeto en representación de la información
  .then(response => imagen.src = URL.createObjectURL(response)); ← creamos una url para imagen a partir de un objeto creado por blob
( .src es una propiedad del objeto imagen por ejemplo podemos crear objetos imagen con new Image() )
*/

// en un tipo de resumen podríamos decir que con get obtenemos y con post podemos enviar y recibir


// LIBRERÍA AXIOS https://github.com/axios/axios (aca se ve algo para colocarlo como link en html)
// Es bueno para cuando es código muy grande
// Está basado en promesas igual que fetch

// GET
/*
const request = axios('archivo.txt');
request.then(response => console.log(response.data));
(el contenido del response esta en el atributo data)
*/

// POST
/*
const request = axios.post('archivo.txt', {
  'nombre': 'leandro'
});
request.then(response => console.log(response.data));
(con esto enviamos con post)
(otra manera:)
const request = axios('archivo.txt', {   ← como fetch es primer parámetro el link y el segúndo la configuración
  method: 'post',
  data: {
    'nombre': 'leandro' ← no hace falta serializar (porque esto es un json ya)
  }
});
*/


// TRABAJAR CON ASINC | AWAIT

/*
const obtenerValor = () => {
  fetch('archivo.txt') ← se puede hacer así y no crear la variable request
    .then(response => {
      if (response.ok) Promise.resolve(response); ← esto es como ver si estado de la respuesta esta bien y el request es promesa por lo que se puede manejar un resolve
      else Promise.reject(response) ← también se puede manejar un reject
    })
    .then(response => console.log(response)) ← se coloca otro then porque se creo otra promesa arriba
    .catch(error => console.log(error)) ← tira la response de arriba
}
(todo lo de arriba no funciona porque como tarde en ejecutarse la petición entonces la función al final retorna en consola undefined)
const obtenerValorAsync = async () => {
  request = await fetch('archivo.txt'); ← el await podría estar solo aca
  response = await request.json(); ← se puede sin usar then, utilizar el .json(), como .text(), etc...
  console.log(response) ← esto si funciona y nos daría los datos despues de hacer la petición y despúes de convertir a json
}
*/