// EVENTOS
// es la manera con la que el navegador puede escuchar una acción del usuario
/*
Eventos posibles básicos:
-'click' = 'onclick' (apretar y soltar el click a el mismo elemento)
-'mausedown' (solo cuando se apreta el mause)
-'mauseup'   (solo cuando se suelta el mause)
-'keypress'  (cuando se apreta y suelta la tecla en el mismo elemento)
-''
*/


// AÑADIR EVENTOS

/*
elemento.addEventListener('evento', función);
(el elemento se le agrega un evento, luego eso ejecuta una función)
(si la función tiene un parámetro es el objeto evento que detecta el navegador)
elemento.addEventListener('evento', función(event)); <- en general 'e' o 'event'
-------------------------------------------------------------------------------
const button = document.querySelector('.btn');
const saludar = () => {
  alert('hola')
};

button.addEventListener('click', saludar);
(o)
button.addEventListener('click', () => {
  alert('hola')
});
*/


// QUITAR EVENTOS

/*
elemento.removeEventListener('evento', función);
(solamente podemos eliminar las funciones con nombre)
--------------------------------------------
button.removeEventListener('click', saludar)
(pero de los 2 eventos que antes le agregé solo se elimina el primero)
});
*/


// PARÁMETRO EVENT

/*
elemento.addEventListener('evento', función(parámetro));

{ (dentro de la función)
  //mause//
  parámetro.x                 <- posición en x del document
  parámetro.y                 <- posición en y del document
  parámetro.pointerType       <- tipo de toque 'mouse' o 'touch'

  //keyboard//
  parámetro.key               <- nombre de la tecla precionada
  parámetro.keyCode           <- código de la tecla precionada

  //casi todos//
  parámetro.target            <- el botón o elemento que encadenó el evento)
  parámetro.timeStamp         <- tiempo que demoró en activarse el evento desde que la página cargó
}

*/


// FLUJO DE EVENTOS

/*
BURBUJA (por defecto)
Un evento ocurre primero en un elemento co mayor especificación o los hijo
mientras que luego ocurren los eventos de los padres o elementos menos especificos
CAPTURA
ocurre alrevez primero el menos especifico y luego hasta el más especifico
(pero esto se tiene que poder modificar)

PARA MODIFICAR
contenedor.addEventListener('evento', función, true); // primero este
hijo.addEventListener('evento', función); // segúndo este
(esto sería un captura)
---------------------------------------------------------------------
contenedor-pequeño.addEventListener('evento', función, true); // primero este
contenedor-grande.addEventListener('evento', función); // tercero
hijo.addEventListener('evento', función); // segúndo este // segundo

PARAR ESA PROPAGACIÓN DE EVENTOS
Dentro de la función del evento que se ejecuta ya sea de primero o como sea
colocar:
event.stopPropagation()

PARA QUITAR FUNCIONALIDADES COMO:
-submit
-reset
-<button/>
cololar:
event.preventDefault()
*/


// EVENTOS DE MAUSE

/*
-'click' = 'onclick' (apretar y soltar el click a el mismo elemento)
-'dbclick'           (apretar 2 veces seguídas(500ms) el click)
-'mousedown'         (solo cuando se apreta el mause)
-'mouseup'           (solo cuando se suelta el mause)
-'mouseover'         (cuando el mause se mueve por encima de un elemento o sus hijos)
-'mouseout'          (cuando el mause se va de encima de un elemento o sus hijos)
-'mousemove'         (cuando el mause se mueve dentro de ese elemento)
-'mouseleave'        (cuando el mause se mueve fuera de ese elemento)
-'contextmenu'       (cuado se le dá click derecho y abre un menú)
[saber que mausecenter existe para microsoft explorer]
*/


// EVENTOS DE TECLADO

/*
-'keydown'           (solo cuando se apreta la tecla en ese elemento)
-'keypress'          (cuando se apreta y suelta la tecla en el mismo elemento)
-'keyup'             (solo cuando se suelta la tecla en ese elemento)
[tanto en mause como en teclado el evento keypress se ejecuta primero que keyup]
*/


// OTROS EVENTOS

/*
-'load'             (cuando un archivo multimedia carga)
-'error'            (cuando un archivo multimedio da error de carga)
-'resize'           (cuando se cambia la resolución de la pantalla)
-'scroll'           (cuando se hace scroll)
-'select'           (después de que se selecciona algo de texto)
[con select se puede usar el parámetro event.target.selectionStart y
event.target.selectionEnd, para luego hacer algo con la selección de texto]
*/


// TEMPORIZADORES

/*
let nombreDeTimer = setTimeout(función, milisegundos); <- para un tiempo y ejecuta la función
clearTimeout(nombreDeTimer); <- si no pasa ese tiempo podemos cancelar que suceda

let nombreDeIntervalo = setInterval(función, milisegundos); <- se ejecuta la función cada cierto tiempo
clearInterval(nombreDeIntervalo); <- deja de ejecutarse

[es interesante y se pueden combinar ambos]
{consumen muchos recursos por lo que es recomendable usarlos poco}
*/
