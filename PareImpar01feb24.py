#Realizar un programa donde se reciba un número flotante por teclado e imprima un mensaje
#diciendo si el número es par o impar y evaluar si es positivo/negativo.
#Output: 'El número: **X** es par/impar y positivo/negativo'
#Donde X es el número ingresado por teclado.

x=float(input("ingrese un numero decimal:"))
if x % 2 == 0:
    print(x, "es par")
else:
    print(x, "es impar")
if x < 0:
    print(x, "y negativo")
else:
    print(x, "y positivo")


