import os

# Mostrar mensaje "Desea continuar" si o no ?
dia= ""
dia_invalido=True

while(dia_invalido):
    dia= input("Ingrese el dia: ")
    dia_invalido= (dia != os.sys.argv[1] and dia != os.sys.argv[2] and dia != os.sys.argv[3] and dia != os.sys.argv[4] and dia != os.sys.argv[5])
#fin_while
print("Fin del bucle")
print("La respuesta es :", dia)

