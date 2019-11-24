import os

# Mostrar mensaje "Desea continuar" si o no ?
elemento= ""
elemento_invalido=True

while(elemento_invalido):
    elemento= input("Ingrese el elemento: ")
    elemento_invalido= (elemento != os.sys.argv[1] and elemento != os.sys.argv[2] and elemento != os.sys.argv[3] and elemento != os.sys.argv[4])
#fin_while
print("Fin del bucle")
print("La respuesta es :", elemento)

