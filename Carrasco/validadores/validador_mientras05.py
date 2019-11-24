import os
# declaración de variables
diagonal_menor, diagonal_mayor, altura,area = 0.0 , 0.0 , 0.0 ,0.0

# input
diagonal_mayor = float (os.sys.argv [ 1 ])
diagonal_menor = float (os.sys.argv [ 2 ])
altura = float (os.sys.argv [ 3 ])

# procesamiento
area = float (((diagonal_mayor + diagonal_menor) * altura) // 2 )

#while
while(diagonal_mayor<diagonal_menor):
    diagonal_mayor=float(input("Ingrese diagonal mayor(Diagonal mayor>diagonal menor):"))


# salida
print ( " Area de un Rombo " )
print ( " Diagonal Mayor: " , diagonal_mayor)
print ( " Diagonal Menor: " , diagonal_menor)
print ( " Altura: " , altura)
print ( " Área: " , area)

