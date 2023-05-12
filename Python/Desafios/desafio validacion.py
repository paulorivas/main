bandera = True
opc = 0
nombre = ''
edad = 0
genero = ''
correo = ''

while bandera:
  print('''
  Menu
  --------------------------------------
  1) Agregar Nombre
  2) Agregar Edad
  3) Agregar Genero
  4) Agregar Correo
  5) Mostrar Informacion
  6) Salir
  --------------------------------------
  ''')
  opc = int(input('Opcion Menú: '))

  if opc == 1:
    nombre = input('Nombre: ')
    while len(nombre) < 5:
      print('Ingresa al menos un nombre de 5 caracteres.')
      nombre = input('Nombre: ')
  elif opc == 2:
    edad = input('Agregar edad: ')
    while not edad.isnumeric():
      print('El valor tiene que ser numerico')
      edad = input('Agregar edad: ')
    while int(edad) > 151:
      print('El rango maximo de edad es de 151 años.')
      edad = input('Agregar edad: ')
  elif opc == 3:
    print('''
Selecciona tu genero:

1) Masculino
2) Femenino
3) Otro
    ''')
    opc = input('Opcion Genero: ')
    while not opc.isnumeric():
      print('El valor tiene que ser numerico')
      opc = input('Opcion: ')
    while int(opc) > 3:
      print('La opción ingresada no es valida.')
      opc = input('Opcion: ')
    if int(opc) == 1:
      genero = 'Masculino'
    elif int(opc) == 2:
      genero = 'Femenino'
    elif int(opc) == 3:
      genero = 'Otro'
    else:
      print('Opción invalida.')
  elif opc == 4:
    correo.isalnum
    correo = input('Correo: ')
    while not '@' in correo:
      print('Has ingresado un correo invalido, reingresa tu email.')
      correo = input('Correo: ')
  elif opc == 5:
    print(f'''
    Nombre: {nombre}
    Edad: {edad}
    Genero: {genero}
    Correo: {correo}
    '''
    )
  elif opc == 6:
    print('Okay, adiós.')
    break