import os
#verififcador de edad
numero=int(os.sys.argv[1])


while(numero<0):
    print("Numero invalido")
    numero=int(input("ingrese numero:"))
#fin while

for i in range(numero+1):
    i=2019- numero
    numero-=1
    print("el valor es:", str(i))
#fin while

