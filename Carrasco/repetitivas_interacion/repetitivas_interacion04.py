import  os
#verificador de email
email=os.sys.argv[1]
verificador=False


for i in email:
    if(i=="@"):
        verificador=True

    #fin bucle

if(verificador==True):
    print("gmail es correcto")

else:
    print("gmail incorrecto")
