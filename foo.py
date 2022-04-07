#Declaramos la lista L, la cual contiene los elementos de la matriz
#Declaramos las variables i,j como iteradores
L= ["_", "_", "_", "_" ,"_" , "_", "_" ,"_" ,"_"]
j = 0
#Definimos la funcion imprimir_matriz, para mostrar la matriz del juego
def imprimir_matriz():
	i = 0
	print("|"+L[i]+"|" +L[i+1]+"|" +L[i+2]+"|")
	i = i+3
	print("|"+L[i]+ "|"+L[i+1]+"|" +L[i+2]+"|")
	i = i+3
	print("|"+L[i]+ "|"+L[i+1]+"|" +L[i+2]+"|")

imprimir_matriz()
#Pedimos las posiciones dentro de la matriz para mostrar el avance del juego
while j<9:
	valor = int(input("Ingrese el numero del casillero(0-8) : "))
	if j%2 == 0:
		L[valor] = "X"
	else :
		L[valor] = "O"

	imprimir_matriz()
	j = j+1




