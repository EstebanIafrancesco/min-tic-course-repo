#def numeroEnteroPositivo(num):
    # if num<0:
    #     return False
    # else:
    #     if num > 63:
    #         print('El valor debe ser menor que 63')
    #     else:
    #         if num%2 == 0:
    #             print('El numero esta entre 0 y 63 y es positivo')
    # if num<0 or num>63:
    #     mensaje = 'El valor no es valido'
    # else:
    #     mensaje = 'El valor está melo pa analizar'
   # print(mensaje)
       
        
    
    
#numeroEnteroPositivo(56)

# diccionario = {
#     "uno": True,
#     "dos": False
# }

# if (diccionario["uno"]):
#     print('Estoy en true mi pez')
# else:
#     print("Estoy en false jeje")


datos_basicos = {
    "nombres":"Leonardo Jose",
    "apellidos":"Caballero Garcia",
    "cedula":"26938401",
    "fecha_nacimiento":"03/12/1980",
    "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
    "nacionalidad":"Venezolana",
    "estado_civil":"Soltero"
}

clave = datos_basicos.keys()
print(clave)
valor = datos_basicos.values()
print(valor)

