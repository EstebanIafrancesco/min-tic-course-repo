# By Esteban Iafrancesco
# 01-06-2021
# Reto 2 curso de programacion Mision TIC

# Ee requiere que escriba una función qué reciba cómo parámetro:
# una lista de palabras y que con la ayuda de ciclos la salida muestre o devuelva las palabras
# abreviadas dentro de una lista así:

# Consideremos una palabra demasiado larga, si su longitud es estrictamente superior a 10
# caracteres. Todas las palabras demasiado largas deben reemplazarse por una abreviatura
# especial.
# Esta abreviatura se hace así: escribimos la primera y la última letra de una palabra y entre
# ellas escribimos el número de letras entre la primera y la última letra. Ese número está en
# sistema decimal y no contiene ceros a la izquierda.
# Por lo tanto, "Esternocleidomastoideo" se escribirá como "e20o" y "otorrinolaringólogo” se
# escribirá como "o17o".


lista = ['oro','localizacion','internationalizacion','electroencefalograma']
# By Esteban Iafrancesco
# 01-06-2021
# Reto 2 curso de programacion Mision TIC
def palabras(lista)->list:
    nuevaLista = []
    for elemento in lista:
        if len(elemento) <= 10:
            nuevaLista.append(elemento)
        else:
            logitudElemento = len(elemento)
            elementoEntuplado = tuple(elemento)
            nuevoElemento = elementoEntuplado[0] + str(logitudElemento-2) + str(elementoEntuplado[logitudElemento-1])
            nuevaLista.append(nuevoElemento)
    return nuevaLista
    
print()
print(palabras(['adrenomieloneuropatía', 'Hipopotomonstrosesquipedaliofobia','murcielago']))
print()