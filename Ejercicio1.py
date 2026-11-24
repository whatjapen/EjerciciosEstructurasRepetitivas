#Ejercicio 1
#Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. Por ejemplo, 5! = 1x2x3x4x5=120),
#Fecha: 24/11/2026
#Por: Juan Agea Rodríguez
#Pide un numero
num=(int(input("Ingrese un numero: ")))
#Se define lo que es la función factorial
def factorial(n):
    if n <=1:
        return 1
    return n*factorial(n-1)
#Imprime el resultado de la funcion con la variable num, el numero que se pide.
print(factorial(num))