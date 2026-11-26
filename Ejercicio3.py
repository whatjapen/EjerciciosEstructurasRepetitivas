#Ejercicio 3
#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.
#Fecha: 24/11/2026
#Por: Juan Agea Rodríguez
#Intentos iniciales
n = 1
#Historial de numeros insertados
historial=[]
#Pedir numeros
num = (int(input("Ingrese un numero: ")))
#"Mientras que sea diferente a 0"
while n != 0:
    historial.append(num)
    num = (int(input("Ingrese un numero: ")))
    #por cada intento se suma 1
    n=n+1
    #Si numero es igual a 0 entonces sumartodo el historial y imprimir
    if num==0:
        resultado=sum(historial)
        print(resultado)