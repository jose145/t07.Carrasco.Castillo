import os
# declaración de variables
nombre, nro_celular, carrera, fecha, modalidad, matricula = " " , 0 , " " , " " , " " ,0.0
# input
nombre = os.sys.argv [ 1 ]
nro_celular = int (os.sys.argv [ 2 ])
carrera = os.sys.argv [ 3 ]
fecha = os.sys.argv [ 4 ]
modalidad = os.sys.argv [ 5 ]
matricula = float (os.sys.argv [ 6 ])


#while
while(modalidad!="Ordinario" and modalidad!="Complementario"):
    modalidad=input("Ingrese modalidad(Ordinario/Complementario):")
    print("modalidad incorrecta")
#fin_while


# salida
print( " Universidad Nacional Pedro Ruiz Gallo " )
print( " Facultad de Ciencias Fisicas y Matematicas " )
print ( " #Constancia de Matricula " )
print ( " Nombre: " , nombre)
print ( " Numero de telefono: " , nro_celular)
print( " Carrera Profesional: " , carrera)
print ( " Fecha: " , fecha)
print ( " Modalidad de ingreso: " , modalidad)
print ( " La matricula: " , matricula)

