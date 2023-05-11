opc = 0
nombre = ''
total = 0
numero_uno = 0
numero_dos = 0

while True:
  print('''
-----------------------
|Menú
| 1) Saludar       
| 2) Contar
| 3) Sumar
| 4) Salir
-----------------------
  ''')
  opc = int(input('Respuesta: '))

  if opc == 1:
    print('Saludar')
    nombre = input('Nombre: ')
    print(f'Hola {nombre}')
    input('Enter para continuar...')
  elif opc == 2:
    print('Contar')
    total += 1
    print(f'Total {total}')
    input('Enter para continuar...')
  elif opc == 3:
    print('Sumar')
    numero_uno = int(input('Numero Uno: '))
    numero_dos = int(input('Numero Dos: '))
    print(f'El resultado es: {numero_uno + numero_dos}')
    input('Enter para continuar...')
  else:
    print('Adiós.')
    break