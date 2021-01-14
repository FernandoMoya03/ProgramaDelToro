import articulo
import persona

listaPersona=[]
listaArticulos=[]
listaPrestamos=[]

idPer= 2
idArt= 2
idPres=0
ip=1
idP=2
i=1
menu = 1

def AgregarPersona(Nombre, idp):
    persona1=persona.Persona()
    persona1.idPer=idp+1
    persona1.Nombre=Nombre  
    listaPersona.append(persona1)
    print("Se ha registrado la persona exitosamente..." + persona1.Nombre)
   # return persona1

def AgregarArticulo(Nombre, ida):
    articulo1=articulo.Articulo()
    articulo1.idArticulo=ida
    articulo1.Description=Nombre
    print("Se ha registrado el articulo exitosamente...")

def PrestamoNew(persona, articulo, fecha):
    persona.prestamoArticulo=articulo
    persona.fecha=fecha
    print("Se ha registrado el prestamo exitosamente...")
    #return persona

def Devoluciones(idp, fecha):
    listaPrestamos[idp-1].fechaDevolucion=fecha
    print("Se ha hecho la devolucion exitosamente...")
        
persona1 = persona.Persona()
persona1.idPer=2
persona1.Nombre="Moya"
listaPersona.append(persona1)

articulo1=articulo.Articulo()
articulo1.idArticulo=2
articulo1.Description="Juguetes"
listaArticulos.append(articulo1)


while menu == 1:
    print("--------- MENU: -------------")
    print("1) REGISTRAR NUEVO USUARIO")
    print("2) NUEVO ARTICULO ")
    print("3) PRESTAMO")
    print("4) INVENTARIO")
    print("5) DEVOLUCION")
    print("-----------------------------")


    seleccion = input("Eliga la opcion: ")
    seleccion = int(seleccion)


    if seleccion == 1:
       nombre=input("Introduce el nombre a registrar: ")
       listaPersona.append(AgregarPersona(nombre, idP+1))
       idP=idP+1


    elif seleccion == 2:
        articuloo=input("Introduce el nombre del articulo: ")
        listaArticulos.append(AgregarArticulo(articuloo, idArt+1))
        idArt=idArt+1


    elif seleccion == 3:

        for i in listaPersona:
            print(ip, i.Nombre)
            ip=ip+1
        perso=int(input("Selecciona el Id de la persona (#):"))
        ip=1
        for i in listaArticulos:
            print(ip, i.Description)
            ip=ip+1
        artic=int(input("Seleccione el # del articulo")) 
        ip=1   
        fechaaaaa= input("Ingrese la fecha:")

        listaPrestamos.append(PrestamoNew(listaPersona[perso-1], listaArticulos[articuloo-1], fechaaaaa))

    elif seleccion == 4:

        for i in listaPrestamos:
            print("Numero: ", ip)
            print("Nombre: ", i.Nombre)
            print(i.prestamoArticulo.Description)
            print(i.fechaPrestamo)
            ip=ip+1

    elif seleccion == 5:
        for i in listaPrestamos:
            print(ip, i.Nombre, i.prestamoArticulo.Description, i.fechaPrestamo, i.fechaDevolucion)
            ip=ip+1
        perso=int(input("Selecciona el # de la persona:"))    
        ip=1
        fechaaaaa=input("Ingrese la fecha de devolucion...")
        Devoluciones(perso, fechaaaaa)
    else:
        print("No seleccionaste una opcion.... ")  
        menu = 2        


    
