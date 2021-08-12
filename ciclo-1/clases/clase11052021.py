import builtins


# tenemos 3 lotes
# cantidad_buses es lo mismo que  número de parqueaderos
# numero_bus es el número asignado al builtins

def dondeVaMiBus(cantidad_buses, numero_bus):
    if (cantidad_buses % 3 == 0) and (cantidad_buses >= numero_bus):
        # si entró acá significa que caben los buses
        tamanioLote = cantidad_buses // 3
        if numero_bus <= tamanioLote: lote = '1'
        elif numero_bus <= tamanioLote*2: lote = '2'
        elif numero_bus <= tamanioLote*3: lote = '3'
        mensaje = "\nSu bus va en el lote numero: " + lote
    else:
        mensaje = "\nSolo tenemos " + str(cantidad_buses) + " parqueaderos"
        
    return mensaje
print( dondeVaMiBus(93,93))



# solución de los compañeros
# def parqueadero_buses(cantidad_buses, numero_bus):
#     respuesta = 0
#     if (cantidad_buses % 3 == 0) and (numero_bus <= cantidad_buses):
#         x = cantidad_buses/3
#         y = numero_bus/x
#         #print(y)
#         #print("respuesta)
#         if y <= 1:
#             mensaje = "\nSu bus va en el lote numero: 1" 
#         if (y > 1 and y <= 2):
#             mensaje = "\nSu bus va en el lote numero: 2" 
#         if (y > 2) and (y <= 3):
#             mensaje = "\nSu bus va en el lote numero: 3" 
#         #print(y)
#     else: mensaje = "\nSolo tenemos " + str(cantidad_buses) + " parqueaderos"
#     return mensaje

# print(parqueadero_buses(45,19))
