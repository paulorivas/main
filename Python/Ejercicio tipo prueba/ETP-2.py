bandera=True
while bandera:
    total=0
    opcion=0
    valor=0
    banderamenu=True
    banderadescuento=True
    entradasmenor=0
    entradasadultos=0
    entradasadulmayor=0
    totalentradasmenor=0
    totalentradasadultos=0
    totalentradasadulmayor=0
    totaldescuento=0
    desmenor=0
    desadul=0
    cantidad=0
    descuento=0

    print('Bienvenido al club "Buena Ventura", ¿Que entrada desea adquirir?')
    while banderamenu:
        print('''
----------------------------
| 1. Menores               |
| 2. Adultos               |
| 3. Adultos Mayores       |
| 4. Cancelar compra       |
| 5. Salir                 |
| 6. Mostrar boleta        |
----------------------------
        ''')

        opcion=input('Opción: ')

        while not opcion.isnumeric():
            print("Ingresa un número correcto!")
            opcion=input('Opción: ')
            input('Enter para continuar...')

        if int(opcion) == 1:
            print('Perfecto, ¿Cuantas entradas deseas adquirir?')
            cantidad=input('Cantidad: ')
            while not cantidad.isnumeric():
                print("Ingresa un número correcto!")
                cantidad=input('Cantidad: ')
                input('Enter para continuar...')
            valor=2500*int(cantidad)
            total=total+valor
            entradasmenor=entradasmenor+int(cantidad)
            totalentradasmenor=totalentradasmenor+valor
            print(f'Perfecto añadiste {entradasmenor} entradas de niño al carro, por {valor} pesos.')
            input('Enter para continuar...')
        ########################################################
        elif int(opcion) == 2:
            print('Perfecto, ¿Cuantas entradas deseas adquirir?')
            cantidad=input('Cantidad: ')
            while not cantidad.isnumeric():
                print("Ingresa un número correcto!")
                cantidad=input('Cantidad: ')
                input('Enter para continuar...')
            valor=5000*int(cantidad)
            total=total+valor
            entradasadultos=entradasadultos+int(cantidad)
            totalentradasadultos=totalentradasadultos+valor
            print(f'Perfecto añadiste {entradasadultos} entradas de niño al carro, por {valor} pesos.')
            input('Enter para continuar...')
        ########################################################
        elif int(opcion) == 3:
            print('Perfecto, ¿Cuantas entradas deseas adquirir?')
            cantidad=input('Cantidad: ')
            while not cantidad.isnumeric():
                print("Ingresa un número correcto!")
                cantidad=input('Cantidad: ')
                input('Enter para continuar...')
            valor=1000*int(cantidad)
            total=total+valor
            entradasadulmayor=entradasadulmayor+int(cantidad)
            totalentradasadulmayor=totalentradasadulmayor+valor
            print(f'Perfecto añadiste {entradasadulmayor} entradas de niño al carro, por {valor} pesos.')
            input('Enter para continuar...')
        ########################################################
        elif int(opcion) == 4:
            print('Perfecto, compra cancelada.')
            banderamenu=False
            input('Enter para continuar...')
        ########################################################
        elif int(opcion) == 5:
            print('Okay, adiós')
            banderamenu=False
            bandera=False
        ########################################################
        elif int(opcion) == 6:
            while banderadescuento:
                descuento=0
                print('''
    ¿Tienes algún descuento?

    1. Menores.
    2. Adultos.
    3. Adultos Mayores.
    4. Continuar a la boleta.
                ''')
                opcion=input('Opción: ')
                while not opcion.isnumeric():
                    print("Ingresa un número correcto!")
                    opcion=input('Opción: ')
                    input('Enter para continuar...')

                if int(opcion) == 1:
                    descuento=10
                    print(f'Perfecto, se te aplicará un {descuento}% de descuento en las entradas de niños.')
                    desmenor=int(totalentradasmenor * descuento) // 100
                    input('Enter para continuar...')
                elif int(opcion) == 2:
                    descuento=5
                    print(f'Perfecto, se te aplicará un {descuento}% de descuento en las entradas de adultos.')
                    desadul=int(totalentradasadultos * descuento) // 100
                    input('Enter para continuar...')
                elif int(opcion) == 3:
                    print(f'Lo sentimos, esta categoria no posee descuentos.')
                    input('Enter para continuar...')
                elif int(opcion) == 4:
                    banderadescuento=False
                else:
                    print('Ingresaste una opción inválida.')
            
            totaldescuento=desmenor+desadul
            print(f'''
Entradas:
------------------------
•   {entradasmenor} Entradas Menor                           $ {totalentradasmenor}
•   {entradasadultos} Entradas Adultos                         $ {totalentradasadultos}
•   {entradasadulmayor} Entradas Adulto Mayor                    $ {totalentradasadulmayor}
------------------------
SubTotal                                        $ {total}
Descuentos                                      $ {totaldescuento}
------------------------
Total a pagar                                   $ {total - totaldescuento}
                    "Gracias por su compra!
            ''')
            banderamenu=False
            bandera=False
        ########################################################
        else:
            print("Ingresaste una opción inválida, reintentaló.")
            input('Enter para continuar...')