import os
from datetime import datetime
os.system("cls")

#          Chip    TM       Nombre      Edad  Sexo  Peso  Vacunado
mascotas=["M001", "Perro",  "Firulais",  4,   "M",  2.9,  True,
          "M002", "Gato",   "Tato",      1,   "M",  2.1,  False,
          "M003", "Canario","Daisy",     2,   "F",  1.3,  True,
          "M004", "Erizo",  "Sonic",     1,   "M",  1.7,  True]

#Definir variables
chip= ""
tipoMascota= ""
nombre= ""
edad= 0
sexo= ""
peso= 0.0
Vacunado= True or False
fecha= datetime.now().strftime("%d-%m-%Y")
opcion= 0
Menu= True

while Menu:
    os.system("cls")
    print('''
            CRUD DE MASCOTAS
            ----------------
        1) Agregar
        2) Buscar
        3) Eliminar
        4) Modificar
        5) Listar
        6) Salir

    ''')
    opcion=int(input("Ingrese una opcion entre 1 y 6: "))

    os.system("cls")

    if opcion == 1:
        print("    AGREGAR DATOS DE MASCOTA    ")
        print("    ------------------------    ")
        
    if opcion == 2:
        pass
    if opcion == 3:
        pass
    if opcion == 4:
        pass
    if opcion == 5:
        pass
    if opcion == 6:
        print("Fin del menu")
        os.system("pause")
        os.system("cls")
        break
