import os
#sumatoria de numeros
numero=int(os.sys.argv[1])
suma=0

while(numero<0):
    print("numero invalido")
    numero=int(input("Ingrese numero a sumar:"))
    #fin while

for i in range(numero):
    i=numero
    suma+=i
    numero-=1
    print(i)
    #fin bucle
print("la suma es igual a=", suma)

