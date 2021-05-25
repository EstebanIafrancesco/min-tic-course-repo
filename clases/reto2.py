# By Esteban Iafrancesco
# 24-05-2021
# Reto 2 curso de programacion Mision TIC

# Se requiere que usted como personal del área de desarrollo que por favor escriba una función
# qué reciba cómo parámetro: un diccionario llamado paciente en el cual las llaves son los
# nombres de las siguientes variables:
    # Mensajes
    # mensaje1 = "Realiza actividad fisica"
    # mensaje2 = "Realiza actividades de meditacion"
    # mensaje3 = "Requiere ayuda psicologica"
    # mensaje4 = "Requiere tratamiento farmacologico"

paciente = {    
    "id_persona": 12345,
    "edad": 60,
    "nombre": "Juan",
    "apellido": "Perez",
    "prueba_ansiedad": "Grave",
    "fobia": False,
    "panico": True,
    "ansiedad_generalizada": False,
    
}

def sint_ansiedad(paciente:dict)->str:
    # Tiene ansiedad generalizada o prueba = "leve"
    if((paciente["prueba_ansiedad"] == "Leve") or (paciente["ansiedad_generalizada"])):
        mensaje = "Realiza actividad fisica"
    elif((paciente["prueba_ansiedad"] == "Moderada") or (paciente["fobia"])):
        mensaje = "Realiza actividades de meditacion"
    elif((paciente["prueba_ansiedad"] == "Grave") and (paciente["panico"])):
        mensaje = "Requiere tratamiento farmacologico"
    else:
        mensaje = "Requiere ayuda psicologica"
    
    return mensaje

print(sint_ansiedad(paciente))

