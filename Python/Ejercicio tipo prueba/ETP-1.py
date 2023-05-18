banderados=True
while banderados:
    total=0
    precio=0
    cantidad=0
    descuento=0
    jornada=0
    bandera=True
    opc=0
    descuento=0
    tradicional=0
    peperoni=0
    carnes=0
    totaldescuento=0

    while bandera:
        print('''
        Bienvenido al menú principal de PizzaDuoc,
        Seleccione lo que desea llevar:
        
        1. Pizza Tradicional
        2. Pizza Peperoni
        3. Pizza All Carnes
        4. Anular pedido
        5. Salir
        6. Pagar
        ''')
        opc = input('Opción: ')
        while not opc.isnumeric():
            print('Ingresa un valor correcto')
            opc = input('Opción: ')
        if int(opc) == 4:
            print('Pedido anulado')
            bandera=False
        elif int(opc) == 1:
            print('¿Cuantas Pizzas de este tipo deseas llevar?')
            cantidad=input('Cantidad: ')
            while not cantidad.isnumeric():
                print('Ingresa un valor correcto')
                cantidad = input('Cantidad: ')
            while int(cantidad) <= 0:
                print('Ingresa un valor superior a 0')
                cantidad = input('Cantidad: ')
            precio = 12000 * int(cantidad)
            total = total + precio
            tradicional=tradicional+int(cantidad)
        elif int(opc) == 2:
            print('¿Cuantas Pizzas de este tipo deseas llevar?')
            cantidad=input('Cantidad: ')
            while not cantidad.isnumeric():
                print('Ingresa un valor correcto')
                cantidad = input('Cantidad: ')
            while int(cantidad) <= 0:
                print('Ingresa un valor superior a 0')
                cantidad = input('Cantidad: ')
            precio = 14000 * int(cantidad)
            total = total + precio
            peperoni=peperoni+int(cantidad)
        elif int(opc) == 3:
            print('¿Cuantas Pizzas de este tipo deseas llevar?')
            cantidad=input('Cantidad: ')
            while not cantidad.isnumeric():
                print('Ingresa un valor correcto')
                cantidad = input('Cantidad: ')
            while int(cantidad) <= 0:
                print('Ingresa un valor superior a 0')
                cantidad = input('Cantidad: ')
            precio = 17000 * int(cantidad)
            total = total + precio
            carnes=carnes+int(cantidad)
        elif int(opc) == 5:
            print('Vuelva pronto!, adios')
            bandera=False
            banderados=False
        elif int(opc) == 6:
            print('''
            ¿Que categoria de usuario eres?

            1. Administrativo
            2. Estudiante Diurno
            3. Estudiante Vespertino
            ''')
            opc = input('Opción: ')
            while not opc.isnumeric():
                print('Ingresa un valor correcto')
                opc = input('Opción: ')
            while int(opc) < 0:
                print('Ingresa un valor superior a 0')
                opc = input('Opción: ')
            while int(opc) > 3:
                print('Ingresa un valor superior a 0')
                opc = input('Opción: ')

            if int(opc) == 1:
                descuento=0
                print(f'Okay, se te aplicará un {descuento}% de descuento')
            elif int(opc) == 2:
                descuento=12
                print(f'Okay, se te aplicará un {descuento}% de descuento')
            elif int(opc) == 3:
                descuento=10
                print(f'Okay, se te aplicará un {descuento}% de descuento')
            else:
                print('Has elegido una opción que no existe')

            totaldescuento = int(total * descuento) // 100
            print(f'''
            PizzasDuoc
            -------------------------
            {tradicional} Pizza Tradicional:    \t${12000*tradicional}
            {peperoni} Pizza Peperoni:          \t${14000*peperoni}
            {carnes} Pizza All Carnes:          \t${17000*carnes}
            -------------------------
            SubTotal: ${total}
            Descuento: {descuento}%
            -------------------------
            Total a pagar: ${total - totaldescuento}
            '''.expandtabs(2))
            bandera=False
            banderados=False
        else:
            print('Has elegido una opción que no existe')