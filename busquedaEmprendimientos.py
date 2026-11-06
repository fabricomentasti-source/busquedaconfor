def BuscarEmprendimientosRegistro(listaEmprendimientos): #David Lopez Cruz
    palabraBuscada = input("Que emprendimiento o descripcion quieres buscar? ").lower().strip()
    encontrado = False
    for emprendimiento in listaEmprendimientos:
        if palabraBuscada in emprendimiento["nombre"].lower() or palabraBuscada in emprendimiento["descripcion"].lower():
            print("Encontrado:", emprendimiento["nombre"], "-", emprendimiento["descripcion"])
            encontrado = True
    if not encontrado:
        print("No se encontro ningun emprendimiento con esa palabra.")

def BuscarEmprendimientosVentas(listaEmprendedores): #Fabricio Mentasti Raña
    palabraBuscador = input("Que emprendedor o capacidad de ventas quieres buscar? ").lower().strip()
    encontrado = False
    for emprendedor in listaEmprendedores:
        if palabraBuscador in emprendedor["nombre"].lower() or palabraBuscador in emprendedor["capacidadVentas"].lower():
            print("Encontrado:", emprendedor["nombre"], "-", emprendedor["capacidadVentas"])
            encontrado = True
    if not encontrado:
        print("No se encontro ningun emprendedor con esa palabra.")

BuscarEmprendimientosRegistro(listaEmprendimientos) #Exequiel Maya hizo los testeos y pruebas del codigo, arreglo algunas partes
BuscarEmprendimientosVentas(listaEmprendedores)