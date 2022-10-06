// algo muy importante saber:
// Elementos HTML: elementos con etiquetas normales dentro de la <html></html>
// Nodos: Todo en HTML es un nodo, desde el Document o nodo raíz como <html></html>, elementos html, atributos comentarios, doctype, y texto, el cual esta entre etiquetas(en general).


// SELECCIÓN DE ELEMENTOS HTML

const pUnicoId = document.getElementById('unico'); // obtiene un elemento html por su ID
const pVariosId = document.querySelectorAll('#varios'); // obtiene uno o varios elementos por su ID o CLASS (retorna una nodelist (no es array se comporta similar es un objeto))
const pUnicoClass = document.querySelector('.unico'); // obtiene un elemento por su ID o CLASS
const pVariosClass = document.getElementsByClassName('varios'); // obtiene varios elementos por su CLASS (retorna html colección (no es array se comporta similar es un objeto))
// estos son objetos los cuales se recomienda ser constantes


// ATRIBUTOS DE ELEMENTOS HTML

pUnicoId.setAttribute('tabindex', 'nada'); // colocar atributos validos, y el valor de este
let atributoDeClass = pUnicoId.getAttribute('id') // retornarvalor  del atributo que posee (en este caso el id es: unico)
pUnicoId.removeAttribute('tabindex'); // quitar atributos que tiene
// los atributos que se encuentran en cualquier elementos son:
// class | contentEditable | dir | hidden | id | style | tabindex | title | role | aria-* | etc...

// ATRIBUTOS DE INPUTS

//____________________________________________
const input = document.getElementById('input');

let valor = input.value; // retorna el valor de el atributo value (en este caso el valor es: texto)
input.type = 'file'; // cambiarle el tipo a un input
input.accept = 'image/gif'; // esto funciona para restrinjir la busqueda del input type='file' (solo busca gifs)
input.form = 'id'; // esto sirve para hacer que un input type='submit' envie un formulario con su id y no necesariamente el boton debe de estar dentro del form
input.minLength = '5'; // minimo de letras
input.maxLength = '5'; // maximo de letras
input.placeholder = 'placeholder'; // el texto de fondito de los type='text'
input.required = 'true'; // el atributo booleano de required


// ESTILOS EN ELEMENTOS HTML

//__________________________________________________
const elemento = document.getElementById('elemento');

elemento.style.color = '#a55';
elemento.style.margin = '50px 0 0';
elemento.style.transform = 'scale(3)';
elemento.style.background = '#33f';
elemento.style.padding = '10px';
elemento.style.content = 'holaaa';
// etc...


// CLASES EN ELEMENTOS HTML

let claseElemento = elemento.className; // retorna la clase del elemento

elemento.classList.contains // primero mirar si el objeto o elemento html tiene clases (en este caso: false)
elemento.classList.add('nombre-de-clase'); // se puede agregar una clase y si se ejecuta varias veces se puede colocar más (no se recomienda colocar varias ala vez con comas)
elemento.classList.add('para-eliminar'); // crear más clases de esta manera (separada)
elemento.classList.remove('para-eliminar'); // se puede eliminar las clases
elemento.classList.replace('nombre-de-clase', 'nuevo-nombre-de-clase'); // se puede remplazar una clase ( si esta retorna true, sino retorna false y no remplaza ni agrega nada)
elemento.classList.item(0); // retorna la clase que esta en cierto índice
elemento.classList.toggle('clase'); // mira si la clase la tiene y si no la coloca
elemento.classList.toggle('clase'); // mira si la clase la tiene y si si la quita
elemento.classList.toggle('clase', false); // mira si la clase la tiene y si no igual lo deja sin clase (tambien funciona true)


// COTENIDO DE UNA ETIQUETA HTML

let texto = elemento.textContent; // retorna el contenido raw de un elemento (sin contar las etiquetas y atributos que tenga adentro)
elemento.textContent = 'HOLA'; // se puede directamente editar ese contenido (no se podrían colocar etiquetas html (solo texto))

let textoInner = elemento.innerHTML; // retorna el contenido ripe de un elemento (contando las etiquetas y atributos que tengo adentro)
elemento.innerHTML = '<b>Hola</b>' // se puede colocar etiquetas html funcionales

let textoOuter = elemento.outerHTML; // retorna lo mismo que inner sin embargo tambien se retorna el elemento mismo, con su etiqueta y atributos
elemento.outerHTML = '<p>Hola de nuevo</p>' // se puede colocar toda su estructura otra vez completa
//saber que se pueden sumar más elementos con la suma o la suma por asignación
// hay etiquetas como innerText outerText que no sirven ya


// CREAR ELEMENTOS

const contenedor = document.querySelector('.contenedor');
const contenedor2 = document.querySelector('.contenedor-2');

const nuevoElemento = document.createElement('P'); // crear elemento html con su nombre de etiqueta en mayúsculas

const nuevoNodoTexto = document.createTextNode('Este es un nodo texto'); // crear un nodo de texto, es como texto sin etiquetas


nuevoElemento.appendChild(nuevoNodoTexto); // agregarle el nodo de texto al <p></p> -->  <p>Este es un nodo texto</p>
// tambien se pudo haber colocado nuevoElemento.innerHTML = 'Este es un nodo texto'
contenedor.appendChild(nuevoElemento); // agregarle el <div><p>Este es un nodo texto</p></div>

// si se quiere añadir muchos elementos iguales estos se unen a un fragmento y luego este al contenedor
// con document.createDocumentFragment()


// SELECCIONAR HIJOS
// como propiedades de los padres...

contenedor.firstChild; // seleccionar el primer nodo hijo, en general no se usa porque selecciona el texto nodo
contenedor.lastChild; // lo mismo que firstChild pero con el ultimo nodo hijo

contenedor.firstElementChild; // seleccionar el primer elemento html hijo
contenedor.lastElementChild; // seleccionar el ultimo elemento html hijo

contenedor.childNodes; // seleccionar todos los nodos hijos
contenedor.children;  // seleccionar todos los elementos html hijos



// METODOS HIJOS
// como propiedades de los padres...

contenedor.hasChildNodes(); // primero mirar si tiene nodo hijos (en este caso true)
contenedor.appendChild(elemento); // añadir un nodo hijo
contenedor.removeChild(elemento); // eliminar un nodo hijo
contenedor.replaceChild(elemento, nuevoElemento); // remplazar un nodo por otro nodo, (nuevo, viejo)


// SELECCIONAR PADRES
// como propiedasdes de los hijos...

contenedor2.parentNode; // como saber cual es el nodo padre, no se usa mucho porque casi nunca hay diferencia entre el segundo y este (en este caso y el segúndo el padre es .contenedor)
contenedor2.parentElement; // como saber cual es el elemento html padre


// SELECCIONAR HERMANOS (SIBLINGS)
// como propiedasdes de los hijos...

pUnicoClass.nextSibling; // saber cual es el siguiente nodo hermano                        (en este caso texto nodo)
pUnicoClass.nextElementSibling; // saber cual es el siguiente elemento html hermano        (en este caso class='varios')
pUnicoClass.previousSibling; // saber cual es el anterior nodo hermano                     (en este caso texto nodo)
pUnicoClass.previousElementSibling; // saber cual es el anterior elemento html hermano     (en este caso id='varios')


// EXTRA

let contenedorCercano = contenedor2.closest('.contenedor'); // selecciona el elemento ascendente o más padre más cercano con la clase .contenedor (en este caso solo hay 1)



/*
agregar a html
atributo accept='image/png'
atributo form='id'
*/
/*
malas practicas:
colocar los atributos booleanos como required no como required='' porque en este cao fallaría
cuando se coloca un elemento no dejarlo indentado sino en la misma linea
*/