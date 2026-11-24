#Ejercicio 3
#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.
#Fecha: 24/11/2026
#Por: Juan Agea Rodríguez
n = 1
while n!=0:
    num = (int(input("Ingrese un numero: ")))
    historial = []
    historial.append(num)
    n=n+1
    if num==0:
        resultado=sum(historial)
        print(resultado)
## POR HACER