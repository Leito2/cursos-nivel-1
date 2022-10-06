// WINDOW
// Es el elemento de la web más grande y de mayor jerarquía



// VARIOS
/*
let url = 'https://youtube.com'; // guardo la url
let ventana = window.open(url); // lo mismo que open(url) <-para abrir una ventana
ventana.closed;  // preguntar si una ventada esta cerrada (si ventana es un open(url) guardado en una variable)
ventana.close(); // cerrar la ventana que se abrió

window.stop; // para de cargar la página

window.prompt(); // lo mismo que prompt() <- para pedir un mensaje
window.alert(mensaje); // lo mismo que alert() <- para colocar un mensaje
window.confirm(mensaje); // lo mismo que confirm() <- para colocar un mensaje para aceptar o rechazar

window.print(); // lo mismo que print() <- para imprimir
*/


// SCREEN
/*

console.log(window.screen): // screen un objeto pantalla

document.write(window.screen.height); // altura de la pantalla al estar normal o maximizada o lo que sea
document.write(window.screen.width); // anchura de la pantalla al estar normal o maximizada o lo que sea

document.write(window.screen.availHeight); // altura de la pantalla al estar normal
document.write(window.screen.availWidth); // anchura de la pantalla al estar normal

document.write(window.screenLeft + '<br><br>'); // posición de la ventana desde la izquierda a la derecha (en pixeles)
document.write(window.screenTop); // posición de la ventana desde arriba hacia abajo (en pixeles)


*/


// SCROLL
/*

alert(window.scrollY); // lo mismo que scrollY <- el scroll vertical que tengamos (en pixeles)
alert(window.scrollX); // lo mismo que scrollX <- el scroll horizontal que tengamos (en pixeles)

window.scroll(0,500); // lo mismo que scroll(x,y) <- mover 0 en X y 500 en Y(solo funciona en la consola al parecer)
*/


// LOCACIÓN
/*

document.write(window.location.href); // mirar la locación del archivo como ruta http

document.write(window.location.protocol); // mirar solo el protocolo http
document.write(window.location.hostname); // mirar solo el subdominio y dominio del sitio
document.write(window.location.pathname); // mirar la ruta del archivo nada más
document.write(window.location.assign('https://youtube.com')); // nos carga una nueva href o documento o página

*/



// 8
/*

puede ser util rehacer con Control + Y

el 85% de los usuarios se van si la página tarda 5 segúndos en cargar

*/
/*
Los Snippets en Soursces de las Dev Tools sirven para automatizar cierto codigo en una página web
*/




// saber que los objetos barprop no sirven casi nada