import os

# Sumar los numeros pares

i=0
suma=0
rango= os.sys.argv[1]
while(i<= int(rango)):
    suma += i
    i += 2
#fin_while

print("La suma de los 300 primeros numeros pares es:", suma)
