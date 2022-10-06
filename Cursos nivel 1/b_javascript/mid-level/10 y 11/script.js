// SWITCH

// Estructura básica
/*
switch (variable) {
  case valor a igualar:         ← esto es como un if
    ──sentencia──
    break
  case otro valor a igualar:    ← esto es como un else if
    ──sentencia──
    break
  case otro valor a igualar:    ← esto es como un else if
    ──sentencia──
    break
  default:                      ← esto es como un else
    ──sentencia──
}
────────────────────────────
switch (fruta) {
  case 'manzana':
    document.write('es una fruta dulce')
    break;
  case 'banana':
    document.write('es una fruta neutra')
    break
  case 'limon':
    document.write('no es fruta...')
    break
  default:
    document.write('no se que es')
}
*/


// MANEJO DE EXEPCIONES

// Try | Catch
// Estructura básica
/*
try{ 
  ──error (no de sintáxis)──
} catch {
  ──manejo del error──
}
─────────────────────────────────|
try {
  hola
} catch {
  console.log('ocurrió un error')
}
─────────────────────────────────
(dice: ocurrió un error)
─────────────────────────────────|
*/

// Catch (error)
// Manejo del error
/*
try{ 
  ──error (no de sintáxis)──
} catch (error) {
  ──manejo del error con variable error──
}
───────────────────────────────────────────|
try {
  hola
} catch (error) {
  console.log('ocurrió un error: ' + error)
}
─────────────────────────────────────────────────────────────
(dice: ocurrió un error: ReferenceError: hola is not defined)
─────────────────────────────────────────────────────────────|
*/

// Finally
// Acción obligatoria
/*
try{ 
  ──error (no de sintáxis)──
} catch (error) {
  ──manejo del error con variable error──
} finally {
  ──se ejecuta dandole igual el resultado del error──
}
───────────────────────────────────────────|
try {
  hola
} catch (error) {
  console.log('ocurrió un error: ' + error)
} finally {
  console.log('fin')
}
─────────────────────────────────────────────────────────────
(dice:
ocurrió un error: ReferenceError: hola is not defined
fin
)
─────────────────────────────────────────────────────────────|
[cuando se tiene que retornar un valor el que tiene prioridad es finally respecto a try y obvio respecto a catch]
*/

// Throw
// Lanzar error personalizado
/*
try{ 
  ──error (no de sintáxis)──
  throw error                    ← podría ser un objeto, array, variable, etc...
} catch (error) {
  ──manejo del error con variable error──
} finally {
  ──se ejecuta dandole igual el resultado del error──
}
───────────────────────────────────────────|
try {
  throw 'solo coloqué hola'
} catch (error) {
  console.log('ocurrió un error: ' + error)
} finally {
  console.log('fin')
}
─────────────────────────────────────────────────────────────
(dice:
ocurrió un error: solo coloqué hola
fin
)
─────────────────────────────────────────────────────────────|
[si se lanzan o ocurren varios errores el que entra a catch es el primero]
*/

// [ cosas como estas, los condicionales o bucles son ESTRUCTURAS DE CONTROL ]



// 11

/*
saber que hay metodos como bold(), sup(), 
que ya son obsoletos
y que para determinar algo obsoleto la mejor manera es ir a la documentación
-también saber que el signo de experimento es que es algo funcional el progreso de ser estandar
*/