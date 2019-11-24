#factorial de un numero
import os
i=int(os.sys.argv[1])


while(i<=0):
    print("Numero incorrecto")
    i=int(input("Ingrese variable correcta:"))
#fin_while

factorial=1
while(i>0):
    factorial *= i
    i-=1
#fin_while

#output
print("El factorial es:", factorial)
