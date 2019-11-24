import os
#programa para que pida la edad
edad=int(os.sys.argv[1])

while(edad<0 or edad>100):
    print("edad incorrecta")
    edad=int(input("Ingrese edad:"))
#fin while

for i in range(edad):
    print("la edad=", i+1)
#fin bucle
