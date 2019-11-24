import os
#suma decrecente de dos numeros
numero01=int(os.sys.argv[1])
numero02=int(os.sys.argv[2])
suma=0
while(numero01<0):
    print("1er Numero invalido")
    numero01=int(input("Ingrese 1er numero:"))
#fin while

while(numero02<0):
    print("2do Numero invalido")
    numero02=int(input("Ingrese 2do numero:"))
#fin while

while(numero01>=0 and  numero02>=0):
    suma=suma + numero01+ numero02
    numero01-=1
    numero02-=1
#fin while

#output
print("Suma es:", suma)
