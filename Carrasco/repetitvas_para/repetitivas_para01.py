# sumatoria decreciente de numeros
import  os
i=int(os.sys.argv[1])

while(i<=0):
    i=int(input("Ingrese numero correcto:"))
#fin while
suma=0
while(i>0):
    suma+=i
    i-=1
#fin_while

#output
print("La suma es=", suma)
