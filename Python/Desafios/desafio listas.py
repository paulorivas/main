lista_producto = []
lista_pk = []
codigo = 000
producto_final = ''
contador = 0
producto = ''
opc = 0

com_nom = ''
def validacion(texto):
    producto = input(f'Producto a {texto}: ')
    while not producto.isalpha():
        print('Ingresa un nombre valido')
        producto = input('Producto a modificar: ')
    return producto

################################################################################################################################################################################################################################################################
while True:
    print('''
-----------Bienvenido al Almacen Duoc----------------
1) Agregar Producto
2) Buscar Producto
3) Listar Producto
4) Modificar Producto 
5) Eliminar Producto  
6) Salir
-----------------------------------------------------
    ''')

    opc = input('Opcion: ')

    while not opc.isnumeric():
        print('El valor indicado es incorrecto... seleccione una opcion con un valor numerico')
        opc = input('Opcion: ')
    
    if int(opc) == 1:
        producto = validacion('Agregar')
        contador = lista_producto.count(producto.lower().title())
        if contador == 1:
            print(f'Actualmente existe el {producto}')
            contador = 0
        else:
            lista_producto.append(producto.lower().title())
            codigo = codigo + 1
            lista_pk.append('8787'+str(codigo))
            print(lista_pk)
    elif int(opc) == 2:
        busqueda = input("Busca por codigo: ")
        while not busqueda.isnumeric():
            print('Codigo invalido, ingrese solo numeros...')
            busqueda = input("Busca por codigo: ")
        for i in range(len(lista_pk)):
            if busqueda == lista_pk[i]:
                print(f'''
                Producto localizado:
    Producto: {lista_producto[i]}      Código: {busqueda}
                ''')
            else:
                print('El código ingresado no se encontró')
    elif int(opc) == 3:
        print('------------------------------------')
        for x in lista_producto:
            print(f'|{lista_pk[lista_producto.index(x)]} {x}')
        print('------------------------------------')
    elif int(opc) == 4:
        busqueda = input("Codigo del producto: ")
        while not busqueda.isnumeric():
            print('Codigo invalido, ingrese solo numeros...')
            busqueda = input("Busca por codigo: ")
        contador = lista_pk.count(busqueda)
        if contador == 1:
            x = lista_pk.index(busqueda)
            com_nom = input('Cambiar nombre del producto: ')
            lista_producto.pop(x)
            lista_producto.insert(x, com_nom.lower().title())
        else:
            print('No existe el producto ingresado')
    elif int(opc) == 5:
        busqueda = input("Codigo del producto: ")
        while not busqueda.isnumeric():
            print('Codigo invalido, ingrese solo numeros...')
            busqueda = input("Busca por codigo: ")
        contador = lista_pk.count(busqueda)
        if contador == 1:
            x = lista_pk.index(busqueda)
            lista_producto.pop(x)
            lista_pk.pop(x)
            print('Se elimino de manera exitosa el producto')
        else:
            print('No existe el producto ingresado')
    elif int(opc) == 6:
        print('Nos vimo')
        break
    else:
       print('El valor indicado es incorrecto... seleccione una opcion con un valor numerico')