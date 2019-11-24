import os
#Registar cuenta de facebook

#declaracion de variables
nombre,apellido,correo,contraseña,edad="","","","",0

#input
nombre=os.sys.argv[1]
apellido=os.sys.argv[2]
correo=os.sys.argv[3]
contraseña=os.sys.argv[4]
edad=int(os.sys.argv[5])



#validador
while(edad<18 or edad>=100):
    edad=int(input("Ingrese edad:"))
    print("Ingrese edad correcta")


#fin_while

#output
print("####Registar cuenta en facebook###")
print("Nombre:", nombre)
print("Apellido:", apellido)
print("Correo:", correo)
print("Edad:", edad)
