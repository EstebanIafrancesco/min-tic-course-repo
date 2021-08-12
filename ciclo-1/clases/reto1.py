# By Esteban Iafrancesco
# 08-05-2021
# Reto 1 curso de programacion Mision TIC

# Se requiere que usted como personal del área de desarrollo que por favor escriba una función
# qué reciba cómo parámetros: un número entero con el número de identificación del paciente,
# un número entero con la edad del paciente y un número entero (Por ejemplo 24) con el valor
# total del resultado de la prueba realizada así (id, age, ans) y retorne un mensaje con el nivel
# de ansiedad, que le proporcione al profesional la información que desea obtener.
# Si el valor total se encuentra entre (0 a 7) debe mostrar “Mínima”, si se encuentra entre (8 y
# 15) debe mostrar un mensaje “Leve” , si se encuentra entre (16 y 25) debe mostrar el mensaje
# “Moderada”, y si se encuentra entre (26 y 63) debe mostrar el mensaje “Grave”. Si el valor
# es mayor a 63 se debe mostrar “El valor no es valido”.
# La cadena de salida debe tener la siguiente estructura: "El nivel de ansiedad del paciente
# identificado con {id}, cuya edad es: {age}, es {resp}" dónde, el valor total debe cumplir con
# las especificaciones (que sea entero, en un rango entre 0 y 63).

def ansiedad(id, age, ans):
    
    # if ans<0 or ans>64 : # Filtro para nivel de ansiedad entre 0 y 63
    #     nivelAns = "El valor no es valido"
    # elif age>110 : # Filtro de edad menor a 110 para evitar edades ilógicas
    #     mensaje'Parametro incorrecto,  age debe estar entre 0 y 110'
    # else:
    if 0 < ans < 8:
        nivelAns = 'Minima'
    elif 7 < ans < 16:
        nivelAns = 'Leve'
    elif 16 < ans < 26:
        nivelAns = 'Moderada'
    elif 26 < ans < 64:
        nivelAns = 'Grave'
    else :
        nivelAns = 'El valor no es valido'
    mensaje = "El nivel de ansiedad del paciente identificado con " + str(id)  + ", cuya edad es: " + str(age) + ", es " + nivelAns
    return mensaje
	
print(ansiedad(12345, 45, 28))
print(ansiedad(12346, 20, 55))
print(ansiedad(12347, 50, 25))
print(ansiedad(12348, 18, 63))
print(ansiedad(12348, 18, 64))
print(ansiedad(12348, 18, 80))