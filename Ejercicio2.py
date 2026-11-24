#Ejercicio 2
#Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación, va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, además de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al límite de intentos te muestra el número que había generado.
#Fecha: 24/11/2026
#Por: Juan Agea Rodríguez
import random
#Variable de intentos (estetica)
n=10
#Numero aleatorio entre 1-100
ales=random.randint(1, 100)
#10 intentos
for i in range(10):
    num=(int(input("Ingrese un numero: ")))
    #Si es igual que termine el programa
    if num==ales:
        print("El numero es igual")
        break
    # Si es diferente que compare el numero con la variable y diga si es mayor menor
    else:
        #(si fallas te resta 1 intento)
        n = n - 1
        print("incorrecto, le quedan", n, "/10 intentos")
        if num>ales:
            print ("PISTA: el numero es mas pequeño")
        if num<ales:
            print ("PISTA: el numero es mas grande")
# Si lo has sacado bien te dira (es) si fallaste te lo dice con un (era), esto es algo estetico sin mucha funcionalidad.
if n>0:
    print("El numero es", ales)
elif n==0:
    print("El numero era", ales)