bandera=True
total=0
opc=0
valor=0
cantidad=0
completoita=0
sopaipilla=0
churrascoita=0
completodina=0
churrascochaca=0

while bandera:
    print('''
Hola, bienvenido al TIO ACEITE, ¿que deseas llevar?
*Suena música de americo.

1) Completo Italiano
2) Sopaipillas
3) Churrasco Chacarero
4) Completo Dinamico
5) Churrasco Italiano
6) Mostrar Boleta
7) Salir
    ''')
    opc = input('Opción: ')
    while not opc.isnumeric():
        print('Ingresa una opción valida.')
        opc = input('Opción: ')
        input('Presiona enter para continuar...')
    if int(opc) == 1:
        print('¿Cuantos Completo Italiano deseas añadir?')
        cantidad=input('Cantidad: ')
        while not cantidad.isnumeric():
            print('Ingresa un valor correcto.')
            cantidad=input('Cantidad: ')
        while int(cantidad) < 0:
            print('Ingresa un valor correcto.')
            cantidad=input('Cantidad: ')
        valor=1200*int(cantidad)
        total=total+valor
        completoita=completoita+int(cantidad)
        print(f'Añadiste {cantidad} Completo Italiano por {valor} pesos.')
        input('Presiona enter para continuar...')
    elif int(opc) == 2:
        print('¿Cuantas Sopaipillas deseas añadir?')
        cantidad=input('Cantidad: ')
        while not cantidad.isnumeric():
            print('Ingresa un valor correcto.')
            cantidad=input('Cantidad: ')
        while int(cantidad) < 0:
            print('Ingresa un valor correcto.')
            cantidad=input('Cantidad: ')
        valor=300*int(cantidad)
        total=total+valor
        sopaipilla=sopaipilla+int(cantidad)
        print(f'Añadiste {cantidad} Sopaipillas por {valor} pesos.')
        input('Presiona enter para continuar...')
    elif int(opc) == 3:
        print('¿Cuantos Churrasco Chacarero Italiano deseas añadir?')
        cantidad=input('Cantidad: ')
        while not cantidad.isnumeric():
            print('Ingresa un valor correcto.')
            cantidad=input('Cantidad: ')
        while int(cantidad) < 0:
            print('Ingresa un valor correcto.')
            cantidad=input('Cantidad: ')
        valor=3200*int(cantidad)
        total=total+valor
        churrascochaca=churrascochaca+int(cantidad)
        print(f'Añadiste {cantidad} Churrasco Chacarero por {valor} pesos.')
        input('Presiona enter para continuar...')
    elif int(opc) == 4:
        print('¿Cuantos Completo Dinamico deseas añadir?')
        cantidad=input('Cantidad: ')
        while not cantidad.isnumeric():
            print('Ingresa un valor correcto.')
            cantidad=input('Cantidad: ')
        while int(cantidad) < 0:
            print('Ingresa un valor correcto.')
            cantidad=input('Cantidad: ')
        valor=1500*int(cantidad)
        total=total+valor
        completodina=completodina+int(cantidad)
        print(f'Añadiste {cantidad} Completo Dinamico por {valor} pesos.')
        input('Presiona enter para continuar...')
    elif int(opc) == 5:
        print('¿Cuantos Churrasco Italiano deseas añadir?')
        cantidad=input('Cantidad: ')
        while not cantidad.isnumeric():
            print('Ingresa un valor correcto.')
            cantidad=input('Cantidad: ')
        while int(cantidad) < 0:
            print('Ingresa un valor correcto.')
            cantidad=input('Cantidad: ')
        valor=2600*int(cantidad)
        total=total+valor
        churrascoita=churrascoita+int(cantidad)
        print(f'Añadiste {cantidad} Churrasco Italiano por {valor} pesos.')
        input('Presiona enter para continuar...')
    elif int(opc) == 6:
        print(f'''
    Boleta TIO ACEITE

{completoita}       Completo Italiano
{sopaipilla}        Sopaipillas
{churrascochaca}    Churrasco Chacarero
{completodina}      Completo Dinamico
{churrascoita}      Churrasco Italiano

Total a pagar: {total}
        ''')
        input('Presiona enter para continuar...')
    elif int(opc) == 7:
        print('Okay, adios.')
        bandera=False
    else:
        print('La opción ingresada no es válida.')
        opc = input('Opción: ')
        while not opc.isnumeric():
            print('Ingresa una opción valida.')
            opc = input('Opción: ')
            input('Presiona enter para continuar...')