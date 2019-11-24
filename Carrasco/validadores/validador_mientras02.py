import os
# declaración de variables
total_pagar, cliente, nro_asiento, nro_dni, costo_pasaje, fecha, ruta =  0.0 , " " , 0 , 0 , 0.0 , " " , " "
# input
cliente = os.sys.argv [ 1 ]
nro_dni = int (os.sys.argv [ 2 ])
costo_pasaje = float (os.sys.argv [ 3 ])
fecha = os.sys.argv [ 4 ]
ruta = os.sys.argv [ 5 ]
nro_asiento = int (os.sys.argv [ 6 ])
igv = 0.1
# procesign
total_pagar = (costo_pasaje + (costo_pasaje * igv))


#validador
while(nro_asiento>50 or nro_asiento<0):
    nro_asiento=int(input("Ingrese numero de asiento:"))
    print("asiento invalido")



# salida
print ( " # Empresa de Transporte: Turela " )
print ( " Cliente: " , cliente)
print ( " Asiento: " , nro_asiento)
print ( " Nro de DNI: " , nro_dni)
print ( " Costo del pasaje " , costo_pasaje)
print ( " Fecha: " , fecha)
print ( " Ruta: " , ruta)
print ( " Total a pagar " , total_pagar)

