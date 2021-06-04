cadena = " hola como estas que me cuentas"
numeritos = "123123123"
lista = list(numeritos)
variableX = int(numeritos)/1000
# print(variableX)
# print(lista)

cad = "hola"
cad2 = "que me cuentas"
num = 22
tupla1 = tuple(cad)

# print (tupla1, num , tuple(cad2))
# --------------------------------------------------------------------
cadena = "hola"
listica = list(cadena)
# print(listica)
listicaUnida = ''.join(listica)
# print(listicaUnida)
# ---------------------------------------------------------------------


saludo = "hola como estas"
lista1 = list(saludo)
lista1.append(123)
# print(lista1)
entuplada = tuple(lista1)
print(entuplada)
# ---------------------------------------------------------------------------

def cuadrado (el = 0):
    return el*el
lista = [1,2,3,4,6,81]
resultado = list(map(cuadrado, lista))
# print(resultado)
