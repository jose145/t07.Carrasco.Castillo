import os
#suma de numero introducidos
n=int(os.sys.argv[1])

while(n<0):
        print("numero invalido")
        n=int(input("Cuantos numeros va a introducir:"))
#fin while

suma_numeros_enteros=0

while(n>0):
    numero=int(input("Introduzca numero:" ))
    while(numero<0):
        print("Numero invalido" )
        numero=int(input("Introduzca numero denuevo:" ))
    n-=1
    print("el numero es correcto")
    suma_numeros_enteros+=numero
#fin while

#output
print("Suma de los numeros introducidos es:", suma_numeros_enteros)
