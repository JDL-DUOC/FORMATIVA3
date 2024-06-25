import os
import time
lista=[]
LCEO=[]
LDES=[]
LANALISTA=[]
cargos=["ceo","desarrollador","analista de datos"]
PRINCIPAL=True

def registrotrabajador(lista):
    secu=True
    nom=input("Ingrese nombre y apellido del trabajador :")
    while secu==True:
        cargo=input("Ingrese cargo del trabajador (ceo,desarrollador,analista de datos) :")
        if cargo not in cargos:
            print("Este cargo no existe")
            time.sleep(2)
            continue
        else:
            Sueldobruto=int(input("Ingrese sueldo bruto :"))
            break
    descuentoSALUD=Sueldobruto* 0.07
    descuentoAFP=Sueldobruto*0.12
    bruto=Sueldobruto-descuentoSALUD-descuentoAFP
    
    lista.append ({"nombre":nom,"Cargo":cargo,"SueldoBruto":Sueldobruto,"DescuentoSALUD":descuentoSALUD,"DescuentoAFP":descuentoAFP,"SueldoBruto":bruto})
    if cargo=="ceo":
        LCEO.append([nom,cargo,Sueldobruto,descuentoSALUD,descuentoAFP,bruto])
    elif cargo=="desarrollador":
        LDES.append([nom,cargo,Sueldobruto,descuentoSALUD,descuentoAFP,bruto] )
    elif cargo=="analista de datos":
        LANALISTA.append([nom,cargo,Sueldobruto,descuentoSALUD,descuentoAFP,bruto] )

def listadodetrabajadores(lista):
    plista=int(input("Desea imprimir [1].todo [2].Por cargo "))
    if plista==1:
        for x in lista:
            print(x)
        teclas=input("Presione [Enter] para continuar")
    elif plista==2:
        terce=True
        while terce==True:
            ingcargo=input("Ingrese cargo a imprimir por pantalla (ceo,desarrollador,analista de datos) : ")
            if ingcargo not in cargos:
                print("Cargo no existe")
                time.sleep(2)
                continue
            else:
                if ingcargo=="ceo":
                    print(LCEO)
                    T=input("Presione [ENTER], para continuar ")
                    break
                elif ingcargo=="desarrollador":
                    print(LDES)
                    T=input("Presione [ENTER], para continuar ")
                    break
                elif ingcargo=="analista de datos":
                    print(LANALISTA)    
                    T=input("Presione [ENTER], para continuar ")
                    break
            
def impresiontrabajadores():

    plistas=int(input("Que planillas de desea imprimir [1].todas [2].Por cargo "))
    if plistas==1:
       with open ("Todas_las_planillas.txt", "w") as escritor:
             escritor.write("Nombre trabajador,Cargo,Sueldo Bruto,DesSALUD,DesAFP,Sueldo Liquido\n")
             for planillas in LCEO:
                 escritor.write(str(planillas) + "\n")
             for planillas1 in LDES:      
                 escritor.write(str(planillas1) + "\n")
             for planillas2 in LANALISTA:      
                 escritor.write(str(planillas2) + "\n")                   
       print("Archivo planillas.txt creado con exito ")
       teclas=input("Presione [Enter] para continuar")
    
    elif plistas==2:
        cuar=True
        while cuar==True:
            ingcargos=input("Ingrese cargo para imprimir planillas de sueldo (ceo,desarrollador,analista de datos) : ")
            if ingcargos not in cargos:
                print("Cargo no existe")
                time.sleep(2)
                continue
            else:
                if ingcargos=="ceo":
                    with open ("Planilla_CEO.txt", "w") as escritorceo:
                        escritorceo.write("Nombre trabajador,Cargo,Sueldo Bruto,DesSALUD,DesAFP,Sueldo Liquido\n")
                        for planillas in LCEO:
                            escritorceo.write(str(planillas) + "\n")
                    print("Archivo Planilla_CEO.txt creado con exito ")
                    teclas=input("Presione [Enter] para continuar")
                    break
                
                elif ingcargos=="desarrollador":
                    with open ("Planilla_DESARROLADOR.txt", "w") as escritordes:
                        escritordes.write("Nombre trabajador,Cargo,Sueldo Bruto,DesSALUD,DesAFP,Sueldo Liquido\n")
                        for planillas in LDES:
                            escritordes.write(str(planillas) + "\n")
                    print("Archivo Planilla_DESARROLLADORES.txt creado con exito ")
                    teclas=input("Presione [Enter] para continuar")
                    break


                elif ingcargos=="analista de datos":
                        with open ("Planilla_ANALISTA.txt", "w") as escritorana:
                            escritorana.write("Nombre trabajador,Cargo,Sueldo Bruto,DesSALUD,DesAFP,Sueldo Liquido\n")
                            for planillas in LANALISTA:
                                escritorana.write(str(planillas) + "\n")
                        print("Archivo Planilla_DESARROLLADORES.txt creado con exito ")
                        teclas=input("Presione [Enter] para continuar")
                        break

def menu():
   while PRINCIPAL==True:
        os.system("cls")
        print("MENU PRINCIPAL")
        print("[1]..Registrar trabajador")
        print("[2]..Listar todos los trabajadores")
        print("[3]..Imprimir planillas de sueldo")
        print("[4]..Salir del programa")
        opc=int(input("Ingrese Opcion :"))
        if opc==1:
            registrotrabajador(lista)
        elif opc==2:
            listadodetrabajadores(lista)
        elif opc==3:
            impresiontrabajadores()
        elif opc==4:
             break           



menu()
