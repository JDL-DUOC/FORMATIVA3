import os
import time

cargos=["ceo","desarrollador","analista"]
LCEO=[]
LDES=[]
LANA=[]

def agregadatos():
    secu=True
    while secu==True:
        os.system("cls")
        nom=input("Ingrese nombre y apellido :")
        ter=True
        while ter==True:
            car=input("Ingrese cargo del trabajador (ceo / desarrollador / analista) : ").lower()
            if car not in cargos:
                print("Este cargo no existe, reintentar")
                time.sleep(2)
                continue
            else:
                suelb=int(input("Ingrese sueldo base de trabajador $ :"))
                salud=suelb * 0.07
                afp=suelb * 0.12
                sbruto=suelb-salud-afp
                if car=="ceo":
                    LCEO.append([nom,car,suelb,salud,afp,sbruto])
                    break
                elif car=="desarrollador":
                    LDES.append([nom,car,suelb,salud,afp,sbruto])
                    break  
                elif car=="analista":
                    LANA.append([nom,car,suelb,salud,afp,sbruto])
                    break
        otro=input("Desea agregar otro usuario S/N :")
        if otro=="s" or otro=="S":
            continue
        else:
            break

def listartrabajadores():
    opc1=int(input("Como desea listar trabajadores? [1].Cargo [2].Todos :"))
    if opc1==1:
        r=True
        while r==True:
            listado=input("Ingrese cargo a listar (ceo / desarrollador / analista)  :")
            if listado not in cargos:
                print("Este cargo no existe, intente nuevamente ")
                time.sleep(2)
                continue
            else:
                if listado=="ceo":
                    print("Nombre trabajador, cargo, sueldo bruto,descuento salud,descuento AFP,Sueldo liquido ")
                    for a in LCEO:
                        print(a)
                    tec=input("Presione [ENTER], para continuar")
                    r=False
                    break
                       
                elif listado=="desarrollador":
                    print("Nombre trabajador, cargo, sueldo bruto,descuento salud,descuento AFP,Sueldo liquido ")
                    for b in LDES:
                        print(b)
                    tec=input("Presione [ENTER], para continuar")
                    break
                             
                elif listado=="analista":
                    print("Nombre trabajador, cargo, sueldo bruto,descuento salud,descuento AFP,Sueldo liquido ")
                    for c in LANA:
                        print(c)  
                    tec=input("Presione [ENTER], para continuar")
                    break
    elif opc1==2:
        print("Nombre trabajador, cargo, sueldo bruto,descuento salud,descuento AFP,Sueldo liquido ")
        for elemento2 in LCEO:
            print(elemento2)                    
        for elemento3 in LDES:
            print(elemento3) 
        for elemento4 in LANA:
            print(elemento4)     
        tec=input("Presione [ENTER], para continuar")


def imprimetrabajadores():
    opcn=int(input("Como desea imprimir liquidacion de sueldo los trabajadores? [1].Cargo [2].Todas :"))
    if opcn==1:
        re=True
        while re==True:
            listado=input("Ingrese cargo a listar (ceo / desarrollador / analista)  :")
            if listado not in cargos:
                print("Este cargo no existe, intente nuevamente ")
                time.sleep(2)
                continue
            else:
                if listado=="ceo":
                    with open ("liquidacion_ceo.txt","w") as liqui:
                        liqui.write("Nombre trabajador, cargo, sueldo bruto,descuento salud,descuento AFP,Sueldo liquido\n")
                        for x in LCEO:
                            liqui.write(str(x)+ "\n")
                    tec=input("Archivo creado con exito, presione [ENTER], para continuar")
                    re=False
                    break
                       
                elif listado=="desarrollador":
                    with open ("liquidacion_desarrolladores.txt","w") as liqui1:
                        liqui1.write("Nombre trabajador, cargo, sueldo bruto,descuento salud,descuento AFP,Sueldo liquido\n")
                        for x1 in LDES:
                            liqui1.write(str(x1)+ "\n")
                    tec=input("Archivo creado con exito, presione [ENTER], para continuar")
                    re=False
                    break
                             
                elif listado=="analista":
                    with open ("liquidacion_analistas.txt","w") as liqui2:
                        liqui2.write("Nombre trabajador, cargo, sueldo bruto,descuento salud,descuento AFP,Sueldo liquido\n")
                        for x2 in LANA:
                            liqui2.write(str(x2)+ "\n")
                    tec=input("Archivo creado con exito, presione [ENTER], para continuar")
                    re=False
                    break
    elif opcn==2:
        with open ("liquidaciones.txt","w") as liqui3:
                        liqui3.write("Nombre trabajador, cargo, sueldo bruto,descuento salud,descuento AFP,Sueldo liquido\n")
                        for x3 in LCEO:
                            liqui3.write(str(x3)+ "\n")
                        for x4 in LDES:
                            liqui3.write(str(x4)+ "\n")
                        for x5 in LANA:
                            liqui3.write(str(x5)+ "\n")
                                                 
                        tec=input("Archivo creado con exito, presione [ENTER], para continuar")
                        re=False
                      
def menu():
   princi=True
   while princi==True: 
        os.system("cls")
        print(" MENU PRINCIPAL ")
        print("[1]..Agregar datos de trabajadores\n[2]..Listar trabajadores\n[3]..Imprimir trabajadores\n[4]..Salir ")
        try:
            opc=int(input("Ingrese su eleccion : "))
        except ValueError:
            print("Error, debe seleccionar valor numerico ")
            time.sleep(2)
            continue
        if opc==1:
           agregadatos()

        elif opc==2:
           listartrabajadores()
        
        elif opc==3:
            imprimetrabajadores()

        elif opc==4:
            break
        else:
            print("Opcion no valida ")
            time.sleep(2)
            continue

menu()


        
