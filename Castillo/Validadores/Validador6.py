import os

# Validar la Password de una cuentade correo (2019)
Password= 0
Password_invalida=True

while(Password_invalida):
    Password= input("Ingrese la Password:")
    Password_invalida =(Password != os.sys.argv[1])
#fin_while

print("Fin del bucle")


