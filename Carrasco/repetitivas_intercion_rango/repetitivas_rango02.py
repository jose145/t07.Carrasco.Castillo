#estaciones "IOPV"
import os
palabra=os.sys.argv[1]



for estacion in palabra:
    if(estacion=="V"):
        print("Verano")
    if(estacion=="P"):
        print("Primavera")
    if(estacion=="O"):
        print("Otoño")
    if(estacion=="I"):
        print("Invierno")

    #fin bucle


