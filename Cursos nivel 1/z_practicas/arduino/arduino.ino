int bombillo = 13; //variables globales
int espera = 500;

//las variables de declaran con su tipo en lenguaje C

void setup() {
  pinMode(bombillo, OUTPUT);
  //arrancar en el puerto 13 output es para que salga la electricidad por ese cable en ese puerto
}

void loop() {
  digitalWrite(bombillo, HIGH);
  //digital es o 0 o los 5 voltio de electricidad, analogo es con ondas osea al final es la misma electricidad o funcion pero de diferente manera
  delay(espera);
  digitalWrite(bombillo, LOW);
  delay(espera);
}
