#Ejercicio 4
#Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
#Fecha: 26/11/2026
#Por: Juan Agea Rodríguez
mayores=0
menores=0
iguales=0
#Pide cantidad de numeros
cantidad=int(input("Ingrese la cantidad de numeros: "))
for i in range(cantidad):
    #Pide los numeros y los evalua dependiendo de si son mayores, menores o iguales a 0, se suma 1 valor a cada variable.
    numero=int(input("Ingrese un numero: "))
    if numero>0:
        mayores=mayores+1
    elif numero < 0:
        menores = menores + 1
    elif numero == 0:
        iguales = iguales + 1
#Te dice cuantos numeros de cada tipo hay
print("Hay", mayores,"numeros mayores que 0, ", iguales,"numeros iguales a 0, ", menores,"numeros menores a 0")