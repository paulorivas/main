lista_producto = []
producto_final = ''
contador = 0
producto = ''
opc = 0
x = 0
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
-----------Bienvenido al Almacen Duoc-----------
1) Agregar Producto
2) Buscar Producto (Verdadero o Falso)
3) Listar Producto
4) Modificar Producto 
5) Eliminar Producto  
6) Salir
    ''')

    opc = input('Opcion: ')

    while not opc.isnumeric():
        print('El valor indicado es incorrecto... seleccione una opcion con un valor numerico')
        opc = input('Opcion: ')
    
    if int(opc) == 1:
        producto = validacion('Agregar')
        producto_final = producto.lower().title()
        lista_producto.append(producto_final)
            
    elif int(opc) == 2:
        producto = validacion('Buscar')
        for x in lista_producto:
            if x == producto.lower().title():
                print('Se encuentra tu producto')
                break
            else:
                print(f'No se encuentra el producto: {producto}')
                break
                
            
    elif int(opc) == 3:
        print('------------------------------------')
        for x in lista_producto:
            print(f'| {x}')
        print('------------------------------------')
    elif int(opc) == 4:
        producto = validacion('Modificar')
        contador = lista_producto.count(producto.lower().title())
        if contador == 1:
            print('Se encuentra tu producto')
            x = lista_producto.index(producto.lower().title())
            com_nom = input('Cambiar nombre del producto: ')
            lista_producto.pop(x)
            lista_producto.insert(x, com_nom.lower().title())
        else:
            print('No existe el producto ingresado')
    elif int(opc) == 5:
        producto = validacion('Eliminar')
        contador = lista_producto.count(producto.lower().title())
        if contador == 1:
            lista_producto.remove(producto.lower().title())
            print('Se elimino de manera exitosa el producto')
        else:
            print('No existe el producto ingresado')
    elif int(opc) == 6:
        print('Nos vimo')
        break
    else:
        print('El valor indicado es incorrecto... seleccione una opcion con un valor numerico')