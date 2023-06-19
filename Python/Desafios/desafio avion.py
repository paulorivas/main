bandera=True #bandera para menu de aerolinea
bandera2=True #bandera para sub menu modificar datos del pasajero
asiento_normal=78900 #variable para guardar el valor de un asiendo normal
asiento_vip=240000 #varible para guardar el valor de un asiento vip
descuento_banco_duoc=15
asientos_x_pasajero_dict = {}
contador=0
linea=""
total_a_pagar=0 #variable para almacenar el total a pagar

asientos_dict = {}
for i in range(1, 43):  #itera desde 1 hasta 42
  asientos_dict[i]=str(i) #almacena en un diccionario los asientos clave numero de asiento valor numero de asiento

while bandera:
    print('''
¡hola bienvenido a aerolineas latam!.

1)	Ver asientos disponibles
2)	Comprar asiento
3)	Anular vuelo
4)	Modificar datos de pasajero
5)	Salir

    ''')
    opc = input('Opción: ')
    while not opc.isnumeric():
      print('Ingresa una opción valida.')
      opc = input('Opción: ')
      input('Presiona enter para continuar...')
    if int(opc) == 1:  # Si la opción es 1, muestra asientos disponibles
      for x in asientos_dict.keys(): #itera sobre los asientos creados
        linea += asientos_dict[x].rjust(5," ") # concatena los asientos y le añade 5 espacios a la derecha
        contador=contador + 1 #aunmenta contador
        if x == 31: #si el numero de asiento es 31 agrega una separacion
          print('| ------------------------------ |')
          print('| ------------------------------ |')
        if contador == 6: # pregunta si el contador es 6
          linea.ljust(5," ") #añade 5 espacios a la izquierda
          print(f'| {linea} |') # imprime linea con 6 asientos
          contador=0 #vuelve el contador a 0
          linea="" #vuelve la linea a un str vacio
    elif int(opc) == 2:  # Si la opción es 2, compra un asiento
      nombre_pasajero = input('nombre pasajero...  ') #captura el nombre del pasajero
      rut_pasajero = input('rut pasajero...') #captura el rut del pasajero
      telefono_pasajero = input('telefono pasajero...  ') #captura el telefono del pasajero
      banco_pasajero = input('banco pasajero...  ') #captura el banco del pasajero
      asiento = int(input('selecciona un asiento...  ')) #captura el asiento
      if asiento > 30: #pregunta por la pocicion del asiento si es mayor a 30 es un asiento vip
        total_a_pagar = asiento_vip #asigna valor de asiento vip
      else:
        total_a_pagar = asiento_normal #asigna valor de asiento normal
      if banco_pasajero == 'bancoDuoc': #pregunta si pertenece al banco duoc para aplicar descuento
        total_a_pagar = int((total_a_pagar - ((descuento_banco_duoc*total_a_pagar)/100))) #aplica descuento por ser bancoDuoc
      print(f'el total a pagar es: {total_a_pagar}') #imprime el total a pagar
      asientos_dict[asiento]="X" #marca el asiento como no disponible
      datos_pasajero_dict = {} # se declara diccionario vacio
      datos_pasajero_dict["nombre"] = nombre_pasajero #almacena el nombre del pasajero en el diccionario datos_pasajero_dict con la clave nombre
      datos_pasajero_dict["rut"] = rut_pasajero #almacena el rut del pasajero en el diccionario datos_pasajero_dict con la clave rut
      datos_pasajero_dict["telefono"] = telefono_pasajero #almacena el telefono del pasajero en el diccionario datos_pasajero_dict con la clave telefono
      datos_pasajero_dict["banco"] = banco_pasajero #almacena el banco del pasajero en el diccionario datos_pasajero_dict con la clave banco
      asientos_x_pasajero_dict[asiento]=datos_pasajero_dict #almacena el asiento con la clave numero de asiento y el valor con los datos del pasajero en el diccionario asientos_x_pasajero_dict
    elif int(opc) == 3:  # Si la opción es 3, anula vuelo
      asiento = int(input('cual es el asiento que desea anular...  ')) # pregunta cual es numero de asiento a anular
      asientos_x_pasajero_dict.pop(asiento) # elimina los datos del pasajero asociado al numero de asiento
      asientos_dict[asiento]=str(asiento) #vuelve a dejar disponible el asiento que fue anulado
    elif int(opc) == 4:  # Si la opción es 4, modifica datos del pasajero
      rut_pasajero = input('rut pasajero...') #captura el rut del pasajero
      asiento = int(input('asiento pasajero...  ')) #captura el asiento
      datos_pasajero_dict = asientos_x_pasajero_dict[asiento] #recupera los datos del pasajero asociados a un numero de asiento
      while bandera2: # bandera de sub menu para modificar los datos del pasajero
        print('datos del pasajero')
        print(f'nombre: {datos_pasajero_dict["nombre"]}, rut: {datos_pasajero_dict["rut"]}') #imprime los datos del pasajero
        print(f'telefono: {datos_pasajero_dict["telefono"]}, banco: {datos_pasajero_dict["banco"]}')  #imprime los datos del pasajero
        print('')
        print('''
          1)	modificar nombre pasajero
          2)	modificar telefono pasajero
          3)	Salir
        ''')
        opcion = input('Opción: ')
        while not opcion.isnumeric():
          print('Ingresa una opción valida.')
          opcion = input('Opción: ')
          input('Presiona enter para continuar...')
        if int(opcion) == 1: #opcion para modificar el nombre del pasajero
          print(f'el nombre actual del pasajero es: {datos_pasajero_dict["nombre"]}') #imprime el valor actual del nombre del pasajero
          nuevo_nombre_pasajero = input('nuevo nombre pasajero...') #captura el nuevo nmbre del pasajero
          datos_pasajero_dict["nombre"] = nuevo_nombre_pasajero #actualiza el nuevo nombre del pasajero
          asientos_x_pasajero_dict[asiento] = datos_pasajero_dict
        elif int(opcion) == 2: #opcion para modificar el telfono del pasajero
          print(f'el telefono actual del pasajero es: {datos_pasajero_dict["telefono"]}') #imprime el valor actual del telefono del pasajero
          nuevo_telefono_pasajero = input('nuevo telefono pasajero...') #captura el nuevo telefono del pasajero
          datos_pasajero_dict["telefono"] = nuevo_telefono_pasajero #actualiza el nuevo telefo del pasajero
          asientos_x_pasajero_dict[asiento] = datos_pasajero_dict
        elif int(opcion) == 3:  # Si la opción es 3, romper el bucle y salir del programa
          break
        else:  # Si la opción no es válida, mostrar un mensaje de error
          print('Opcion incorrecta')
    elif int(opc) == 5:  # Si la opción es 5, romper el bucle y salir del programa
      break
    else:  # Si la opción no es válida, mostrar un mensaje de error
      print('Opcion incorrecta')