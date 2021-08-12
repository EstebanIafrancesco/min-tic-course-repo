import pandas as pd
import numpy as np
# from pandas.io.sql import DatabaseError

# datos = {
#         'Nombre': ['Silvana','Claudia','Rebeca','Elizabeth', 'Diana','Salome'],
#         'Edad': ['41','35','34','30', '29','28'],
#         'Profesion': ['Enfermera','Modista','Arquitecta','Trabajadora social', 'Manicurista','Ganoexceleadora'] 
#         }

# df = pd.DataFrame(datos)

# print(df)
# print('\n*2')

# # Datos no validos

# datos2 = {
#         'Nombre': ['Silvana','Claudia','Rebeca','Elizabeth', 'N/A','Salome'],
#         'Edad': ['41','35',np.nan,'30', '29','28'],
#         'Profesion': ['Enfermera','Modista','Arquitecta','Trabajadora social', 'Manicurista','N/A'] 
#         }

# df2 = pd.DataFrame(datos2)
# print(df2)
# print('\n*2')
# print(df2.info())
# print('\n*2')

# print(df2.describe())
# print('\n*2')

# daticos = {'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
#         'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
#         'age': [27, 31, 36, 53, 48, 36, 40, 34],
#         'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
#         'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]}


# datosDataFrame = pd.DataFrame(daticos)

# # print(datosDataFrame)

# datosDataFrame.to_csv('datosGuardados.csv')

# df = pd.read_csv(
#         'datosGuardados.csv', 
#         skiprows=1, 
#         names = ['esto de primero','nombre2','nombre3','nombre4','nombre5','nombre6'],
#         na_values=['?']
#         )

# print(df)

df = pd.read_csv('datosPruebas.csv', names=['Top PO Admin Number'])

print(df)

