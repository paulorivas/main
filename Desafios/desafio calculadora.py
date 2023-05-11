opc = 0
numero1 = 0
numero2 = 0

while True:
    print('''
Hola, bienvenido, que deseas realizar:

1) Sumar
2) Restar
3) Multiplicar
4) Dividir
5) Potencia
6) Salír
    ''')
    opc = int(input('Opción: '))
    if opc == 1:    
        numero1 = input('Numero 1: ')
        while numero1.isalpha():
            print('Ingresa nuevamente el valor.')
            numero1 = input('Numero 1: ')
        numero2 = input('Numero 2: ')
        while numero2.isalpha():
            print('Ingresa nuevamente el valor.')
            numero2 = input('Numero 2: ')
        print(f'La suma de los número es: {int(numero1)+int(numero2)}')
        input('Presione enter para continuar...')

    if opc == 2:    
        numero1 = input('Numero 1: ')
        while numero1.isalpha():
            print('Ingresa nuevamente el valor.')
            numero1 = input('Numero 1: ')
        numero2 = input('Numero 2: ')
        while numero2.isalpha():
            print('Ingresa nuevamente el valor.')
            numero2 = input('Numero 2: ')
        print(f'La resta de los número es: {int(numero1)-int(numero2)}')
        input('Presione enter para continuar...')

    if opc == 3:    
        numero1 = input('Numero 1: ')
        while numero1.isalpha():
            print('Ingresa nuevamente el valor.')
            numero1 = input('Numero 1: ')
        numero2 = input('Numero 2: ')
        while numero2.isalpha():
            print('Ingresa nuevamente el valor.')
            numero2 = input('Numero 2: ')
        print(f'La multiplicación de los número es: {int(numero1)*int(numero2)}')
        input('Presione enter para continuar...')
    
    if opc == 4:    
        numero1 = input('Numero 1: ')
        while numero1.isalpha():
            print('Ingresa nuevamente el valor.')
            numero1 = input('Numero 1: ')
        numero2 = input('Numero 2: ')
        while numero2.isalpha():
            print('Ingresa nuevamente el valor.')
            numero2 = input('Numero 2: ')
        print(f'La división de los número es: {int(numero1)/int(numero2)}')
        input('Presione enter para continuar...')

    if opc == 5:    
        numero1 = input('Numero 1: ')
        while numero1.isalpha():
            print('Ingresa nuevamente el valor.')
            numero1 = input('Numero 1: ')
        numero2 = input('Numero 2: ')
        while numero2.isalpha():
            print('Ingresa nuevamente el valor.')
            numero2 = input('Numero 2: ')
        print(f'La potencia de los número es: {int(numero1)**int(numero2)}')
        input('Presione enter para continuar...')
    
    if opc == 6:
        print('Adios.')
        break