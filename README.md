# TresEnRaya
Implementacion del juego Tres en raya 

El presente programa permite  al  usuario  jugar  “Tres  en  raya”.  El  usuario  deberá  de ingresar un número, indicando el casillero (0-8) que desea marcar con “O” o “X” (estos se  llenarán   automáticamente).  El  programa  terminará  al  rellenarse  todos los casilleros.

###Descripcion del codigo 
Primero declaramos una lista L la cual contiene los elementos de la matriz y luego declaramos las variables i, j como iteradores.
Luego definimos la función imprimir_matriz para imprimir la matriz del juego.
Escribimos print("|"+L[i]+"|" +L[i+1]+"|" +L[i+2]+"|") tres veces para poder seleccionar el casillero del juego el cual queramos marcar.
Finalmente pedimos las posiciones dentro de la matriz para mostrar el avance del juego.
Al momento de ejecutar:
print("|"+L[i]+"|" +L[i+1]+"|" +L[i+2]+"|")
	i = i+3
	print("|"+L[i]+ "|"+L[i+1]+"|" +L[i+2]+"|")
	i = i+3
	print("|"+L[i]+ "|"+L[i+1]+"|" +L[i+2]+"|")
La interfaz del juego se verá de tal forma que cada casillero contendrá un valor el cual va a ser i+1 e i+2 y así sucesivamente hasta llegar a 8, ya que el valor de i es 0, empezando con una casilla con el valor 0 y terminando en la novena casilla con el valor 8:

Posteriormente, mostrará un input que nos pedirá el número del casillero que queramos marcar, del 0 al 8, de esta manera:

Ingrese el número del casillero(0-8) : 

Nosotros al digitar un número del 0 al 8, la variable "valor" tomará el valor del número que digitemos y reemplazará el subguión de la interfaz del juego por el símbolo X, el siguiente turno realizará lo mismo pero esta vez, con el símbolo O.


