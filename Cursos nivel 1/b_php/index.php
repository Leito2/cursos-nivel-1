<?php
$variable = 'hola '; #crear variables
define('CONSTANTE', 3.14); #crear constantes
#Int (integer) = entero (pesa como 1 byte)
#float (float) = deicmales racionales (pesa como 2 bytes)
#Double () = irracinales procisos (pesa como 8 bytes)
#Charracter (Chat) = con los carracteres com numeros o letras
#String (str) = cadena de carracteres
#Bool (bool) = los True o False
#None y Undefined


$numero = '5';
var_dump($numero); #para ver informacion de algo
#string(1) '5'


$numero_10 = $numero + 5;
#string + int (php es permisivo)
echo "$numero_10 \n";


#covertir otros tipos (casting)

$numero = (int) $numero; #cambiar a entero

var_dump($numero);
#int(5)

$cero = 0; #asignar

$cero_bool = (bool) $cero; #asignar a otra variable

var_dump($cero_bool);
#bool(False)


#imprimir
print_r($numero);
echo "\n";
#5


$nombre = True;
$apellido = True;
$nombre_2 = False;
$correa = False;


// And
var_dump($nombre && $apellido); #True


// Or
var_dump($nombre_2 || $correa); #False


// Not
var_dump(!$nombre); #False
echo "\n";


$numero = (int) (7201/3600); # es como el //
echo $numero;
echo "\n";



// Operador realacional especial de php
echo 2 <=> 1; #si mayor derecha (1), si mayor izq (-1), si son iguales (0)


// Asignaciones

$edad_leandro = ($edad_canela = 1) + 16;

echo 'La edad de pepito es ' . $edad_leandro . "\n";
echo 'La edad de canela es ' . $edad_canela . "\n";


// Concatenacion

$nombre = 'Leandro';
$nombre .= ' ' . 'Cataño';
echo "$nombre\n";

// Presedencia
#para evitar errores de presedencia mejor colocar parentesis en las operaciones, aritmeticas, relacionales y logicas(conectores)

#prompt o input en php
$segundos = readline('Ingrese el tiempo en segundos: ');

#ejercicio
$horas = $segundos /3600;

$horas = (int) $horas;

$segundos = $segundos % 3600;

$minutos = $segundos /60;

$minutos = (int) $minutos;

$segundos = (int) ($segundos /60); # manera de hacer en 1 line


echo "Son $horas horas, $minutos minutos y $segundos segundos." # la ultima da igual
?>