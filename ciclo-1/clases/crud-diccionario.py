# By Esteban Iafrancesco
# 26-05-2021
# Crud para lista de tareas
import os

# Diccionario basico de entrada
tareas = {}

# Menú de entrada
def menu() -> None:
    print('1. Create')
    print('2. Read')
    print('3. Update')
    print('4. Delete')
    print('5. Salir\n')
    a = int(input("Escoge una de las opciones de la lista "))
    opciones(a)

# Definición de opciones
def opciones(a):
    if(a == 1):
        create()
    elif(a == 2):
        read()
    elif(a == 3):
        update()
    elif(a == 4):
        delete()
    elif(a == 5):
        print('\n')
        print('Hasta luego ...')
        print()
        exit()
    else:
        print('Opcion incorrecta, debes escoger alguna de la lista ! ')
        print()
        print()
        menu()

# Create
def create():
    os.system("cls")
    print('Tarea creada...')
    print()
    menu()
    
    
# Reada
def read():
    os.system("cls")
    print('Lista de tareas: ')
    print()
    # print(tareas.keys("id"))
    
    
# Update
def update():
    os.system("cls")
    print('Lista de tareas actualizada...')
    print()
    
    
# Delete
def delete():
    os.system("cls")
    print('Borrando tarea...')
    print()


menu()



