import os

# Validar el peso de un nino (os.sys.argv[1] - os.sys.argv[2]
peso = 0.0
peso_invalido=True
while (peso_invalido):
    peso=float(input("Ingrese peso:"))
    peso_invalido=(peso < float(os.sys.argv[1]) or peso > float(os.sys.argv[2]))
#fin_while

print("Fin del bucle")


