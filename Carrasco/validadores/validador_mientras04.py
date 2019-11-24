import os
# declaración de variables
nombre, años, fecha, hora, luga = " " , 0 , " " , " " , " "
# input
nombre = os.sys.argv [ 1 ]
años = int (os.sys.argv [ 2 ])
fecha = os.sys.argv [ 3 ]
hora = os.sys.argv [ 4 ]
lugar = os.sys.argv [ 5 ]

#while
while(años<0 or años>100):
    años=int(input("Ingrese el numero de años:"))
    print("Años invalido")
#fin_while


# salida
print ( " ☺ Te invito a mi fiesta de cumpleaños  " )
print ( " De: " , nombre)
print( " Cumple: " , años, " años " )
print ( " Fecha: " , fecha)
print ( " Hora: " , hora)
print( " Lugar: " , lugar)
print( " NO HAY FALTAS " )
