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
# Esto seria igual a : (212 – 32) * 5 / 9 = 100 ºC

n = [212, 104, 50]
# n = 'almohabana' 

def grados_celsius(n) -> str:
    print(n)
    # implementar lambda
    # c = lambda f : (f - 32)*5/9
    # print(c)
    # hacer un map de lamda
    
    def myFuncion(a):
        return a + a
    salida = map(myFuncion, str(n))
    
    print(salida)
    
    
    
    
    # try:
    #     acá va la función
    # except:
        
    #     print('Error al convertir los grados, revise los datos de entrada')
        
grados_celsius(n)
    
    




