lista_nombres = ['Michael', 'Paulo', 'Martin']
lista_apellidos = ['Catalán', 'Rivas', 'Zuazo']
lista_personas = [lista_nombres, lista_apellidos]

identificador=input('ID de la persona: ')
while not identificador.isnumeric():
    print('Ingresa un valor correcto.')
    identificador=input('ID de la persona: ')

print(f'''
Nombre: {lista_personas[0][int(identificador)]}
Apellido: {lista_personas[1][int(identificador)]}  
    ''')