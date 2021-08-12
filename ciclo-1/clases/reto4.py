# By Esteban Iafrancesco
# 15-06-2021
# Reto 4 curso de programacion Mision TIC


# Se requiere que escriba una función qué reciba cómo parámetros:
# una lista de grados Farenheit, y que con ayuda de las funciones map y lambda muestre o
# devuelva la lista de los grados convertidos a Celsius:
# Para convertir de Farenheit a Celsius:
# Se debe aplicar la formula (F – 32) * 5 / 9, donde es F son los grados en Farenheit.
# En caso de que la respuesta tenga varios decimales se debe redondear a un decimal.
# Ejemplo:
# Convertir 212 ºF a ºC
# Esto seria igual a : (f - 32) * 5 / 9 = 100 ºC, si f ==212

# n = [212, 104, 50]
n = [50, 176, 104]
# n = [104, 320, 50]

def grados_celsius(n) -> str:
    try:
        c = lambda n : round(((n - 32) * 5 / 9),1)
        celsius = list(map(c, n))
        return str(n) + ' en grados Farenheit corresponde a ' + str(celsius) + ' en grados Celsius respectivamente'
    except:
        return 'Error al convertir los grados, revise los datos de entrada'
    
print()
print(grados_celsius(n))
print()

