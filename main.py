def cargar_atletas(cantidad):
  atletas=[]

  for _ in range(cantidad):
    nombre=input("Ingrese el nombre:")
    apellido=input("Ingrese el apellido:")
    pais=input("Ingrese el pais:")
    edad=int(input("Ingrese la edad:"))
    medalla=input("Ingrese la medalla(Oro/Plata/Bronce/No obtuvo medalla):")

    atleta=[nombre,apellido,pais,edad,medalla]

    atletas.append(atleta)

  return atletas

def rusos_oro(atletas):
  for atleta in atletas:
    pais=atleta[2]
    medalla=atleta[4]

    if pais.lower() == "rusia" and medalla.lower() == "oro":
      return atleta[0],atleta[1]


def japones_mas_joven(atletas):
  edad_minimo=9999
  mas_joven=atletas[0]
  for atleta in atletas:
    edad=atleta[3]
    pais=atleta[2]

    if pais.lower()=="japon" and edad < edad_minimo:
      edad_minimo=edad
      mas_joven=atleta[0],atleta[1],atleta[3]
  return mas_joven

def alemanes_sin_medalla(atletas):
  suma=0
  cantidad=0

  for atleta in atletas:
    pais=atleta[2]
    edad=atleta[3]
    medalla=atleta[4]

    if pais.lower() == "alemania" and medalla.lower() == "no obtuvo medalla":
      suma=edad+suma
      cantidad=cantidad+1
  if cantidad > 0:
    promedio= suma/cantidad
  else:
    promedio=0
  return promedio


def menu(atletas):
  opcion=input("Ingrese:\nA-Mostrar nombre y apellido de los atletas rusos que ganaron una medalla de oro. \nB-Mostrar al atleta japones más joven del torneo. \nC-Mostrar el promedio de edad de los atletas alemanes que no ganaron una medalla. \nD-Salir:")
  while opcion.lower()!="d":
    if opcion.lower()=="a":
      print(rusos_oro(atletas))
    elif opcion.lower() =="b":
      print(japones_mas_joven(atletas))
    elif opcion.lower() =="c":
      print(alemanes_sin_medalla(atletas))
    else:
      print("Opcion invalida")
    opcion=input("ingrese otra opcion, ingrese D para salir:")
      

cantidad=int(input("Introduzca una cantidad:"))
atletas=cargar_atletas(cantidad)

menu(atletas)






  

    



      

  












  
    
    










  



