import os
os.system("cls") 


lAsignaturas=[]
vContador=0

while True:

    vAsignatura = input("Ingrese una asignatura : ")

    if vAsignatura == '':
        break

    try:
        vNota = float(input("Ingrese nota obtenida en " + vAsignatura +  ": "))
    except:
        vNota = 0.0
    #end try
        

    vContador = vContador + 1
    ListadoNotas = { 
                 'n°'         :  vContador,
                 'asignatura' :  vAsignatura,
                 'nota'       :  vNota, 
                }   
    
    lAsignaturas.append(ListadoNotas)


print("Se han registrado", vContador, "asignaturas")
print("las asignaturas reprobadas son : ")

for vTAsig in lAsignaturas :
    if vTAsig['nota'] < 4:
        print(vTAsig)
#end for