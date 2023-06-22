import random
vehiculos = []
vehiculo = []
lista_tipo = []
multas = []
multas_actual = []
lista_patente = []
opcion = 0
marca = ''
precio = 0
fecha_registro = ''
opcion_multa = ''
dueno = ''
monto = ''
fecha = ''
encontrado = False

def menu():
    while True:
        print('''
        ----- AUTOMOTORA AUTO SEGURO -----
1. Grabar vehículo
2. Buscar vehículo por patente
3. Imprimir certificados
4. Salir
        ''')

        opcion = input("Ingrese el número de la opción que desea ejecutar: ")
        
        if int(opcion) == 1:
            grabar_vehiculo()
        elif int(opcion) == 2:
            buscar_vehiculo()
        elif int(opcion) == 3:
            imprimir_certificados()
        elif int(opcion) == 4:
            print("¡Gracias por utilizar el programa!, Paulo Rivas v1.0")
            break
        else:
            print("Opción inválida, Por favor, ingrese un número del 1 al 4.")

def grabar_vehiculo():
    print('''
           |AUTO-SEGURO|
         INGRESE LA PATENTE   
                            -------------------------------------------------
      ▄▄▐▀▀▀▀▀▀▀▀▀▀▀▌▄▄     |     _      ____     ____   ____    _   ____   |
     ▄▄▄█▄▄▄▄▄▄▄▄▄▄▄█▄▄▄    |    / \    | __ )   / ___| |  _ \  / | |___ \  | 
    █▄█░░█▓█▓█▓█▓█▓░░█▄█▌   |   / _ \   |  _ \  | |     | | | | | |   __) | |
   ▓▓█▀█   ABCD79    █▀█▓▓  |  / ___ \  | |_) | | |___  | |_| | | |  / __/  |
   ▓▓▀▀               ▀▀▓▓  | /_/   \_\ |____/   \____| |____/  |_| |_____| |
                            -------------------------------------------------
    ''')
    
    patente = input("Ingrese la patente del vehículo: ")
    while not patente.isalnum():
        print('Ingrese una patente válida.')
        patente = input("Ingrese la patente del vehículo: ")
        
    if patente.upper() in lista_patente:
        print(f'Ya existe un vehículo registrado con la patente: {patente.upper()}')
        input('Presione Enter para continuar')
        
    lista_patente.append(patente.upper())
    
    print('''
------------------------------------------------------
|                                                    |
| 1) SUV                   ▄▄▐▀▀▀▀▀▀▀▀▀▀▀▌▄▄         |       
| 2) MOTOCICLETAS         ▄▄▄█▄▄▄▄▄▄▄▄▄▄▄█▄▄▄        |
| 3) FURGON               █▄█░░█▓█▓█▓█▓█░░█▄█▌       |
| 4) PICKUP               ▓▓█▀████████████▀█▓▓       |
|                         ▓▓▀▀            ▀▀▓▓       |                                                         
|                           - AUTO_SEGURO -          |
------------------------------------------------------
    ''')
    tipo = input("Ingrese el tipo de vehículo: ")
    
    while not tipo.isnumeric():
        print('Ingrese una opción válida.')
        tipo = input("Ingrese el tipo de vehículo: ")
        
    if int(tipo) == 1:
        tipo = 'SUV'
    elif int(tipo) == 2:
        tipo = 'MOTOCICLETA'
    elif int(tipo) == 3:
        tipo = 'FURGON'
    elif int(tipo) == 4:
        tipo = 'PICKUP'
    else:
        print('Tipo de vehículo inválido.')
        input('Presione Enter para continuar')
        menu()

    lista_tipo.append(tipo)
    
    marca = input("Ingrese la marca del vehículo: ")
    while not marca.isalpha() or len(marca) < 2 or len(marca) > 15:
        print('Ingrese una marca válida (2 a 15 caracteres).')
        marca = input("Ingrese la marca del vehículo: ")
    
    precio = input("Ingrese el precio del vehículo: ")
    while not precio.isdigit() or int(precio) < 5000000:
        print('Ingrese un precio válido (mayor a 5 millones).')
        precio = input("Ingrese el precio del vehículo: ")
    
    multas = []
    
    while True:
        opcion_multa = input("¿Desea agregar una multa al vehículo? (S/N): ")
        if opcion_multa.upper() == "S":
            monto = random.randint(1500, 3500)
            fecha = input("Ingrese la fecha de la multa: ")
            multa = [monto, fecha]
            multas.append(multa)
            print(f'Se agregó una multa por {monto}, con fecha {fecha}')
        elif opcion_multa.upper() == "N":
            break
        else:
            print("Ingrese una opción válida.")
    
    fecha_registro = input("Ingrese la fecha de registro del vehículo: ")
    dueno = input("Ingrese el nombre del dueño del vehículo: ")
    
    vehiculo = [
        tipo,
        patente.upper(),
        marca.upper(),
        precio,
        multas,
        fecha_registro,
        dueno.capitalize()
    ]
    
    vehiculos.append(vehiculo)
    print("El vehículo ha sido registrado exitosamente.")

def buscar_vehiculo():
    patente = input("Ingrese la patente del vehículo que desea buscar: ")
    encontrado = False
    for vehiculo in vehiculos:
        if vehiculo[1] == patente.upper():
            encontrado = True
            print(f'''
----- INFORMACIÓN DEL VEHÍCULO -----
Tipo: {vehiculo[0]}
Patente: {vehiculo[1]}
Marca: {vehiculo[2]}
Precio: {vehiculo[3]}
Fecha de Registro: {vehiculo[5]}
Dueño: {vehiculo[6]}

----- MULTAS DEL VEHÍCULO -----
            ''')
            if vehiculo[4]:
                print('El vehículo posee multas.')
            else:
                print("El vehículo no tiene multas.")
            break
    if not encontrado:
        print("No se encontró ningún vehículo con la patente ingresada.")

def imprimir_certificados():
    patente = input("Ingrese la patente del vehículo que desea buscar: ")
    encontrado = False
    for vehiculo in vehiculos:
        if vehiculo[1] == patente.upper():
            encontrado = True
            print(f'''
----- CERTIFICADO DE ANOTACIONES VIGENTES -----
Dueño: {vehiculo[6]}
      CERTIFICADO DE REGISTRO
Tipo: {vehiculo[0]}
Patente: {vehiculo[1]}
Marca: {vehiculo[2]}
Precio: {vehiculo[3]}
Fecha de Registro: {vehiculo[5]}
            ''')
            if vehiculo[4]:
                print('      MULTAS DEL VEHÍCULO     ')
                for multa in vehiculo[4]:
                    print(f'Monto: {multa[0]} Fecha: {multa[1]}')
            else:
                print("El vehículo no tiene multas.")
            break
    if not encontrado:
        print(f'No se encontró ningún vehículo con la patente {patente.upper()}.')

menu()