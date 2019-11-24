import  os

#Verificador de numero positivos y negativos
n=int(os.sys.argv[1])

while(n<0):
        print("numero invalido")
        n=int(input("Cuantos numeros va a introducir:"))
#fin while

verificador_negativo=0
verificador_positivo=0
while(n>0):
    numero=int(input("Introduzca numero:" ))
    if(numero<0):
        verificador_negativo+=1
    if(numero>0):
        verificador_positivo+=1
    n-=1
    print("el numero es correcto")
#fin while

#output
print("se tiene", str(verificador_negativo)+" negativos y", str(verificador_positivo)+" positivos")
