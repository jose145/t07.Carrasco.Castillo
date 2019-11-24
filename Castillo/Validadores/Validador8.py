import os

# Validar que el total a pagar este entre os.sys.argv[1] y os.sys.argv[2]
total_pagar= 0
monto_invalido= True

while (monto_invalido == True):
    total_pagar= input("Ingrese total a pagar:")
    monto_invalido = (total_pagar< os.sys.argv[1] or total_pagar> os.sys.argv[2])
#fin_while
print("Fin del bucle")
