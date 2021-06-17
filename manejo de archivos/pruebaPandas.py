import pandas as pd
import numpy as np

datos = {
        'Nombre': ['Silvana','Claudia','Rebeca','Elizabeth', 'Diana','Salome'],
        'Edad': ['41','35','34','30', '29','28'],
        'Profesion': ['Enfermera','Modista','Arquitecta','Trabajadora social', 'Manicurista','Ganoexceleadora'] 
        }

df = pd.DataFrame(datos)

print(df)
print('\n*2')

# Datos no validos

datos2 = {
        'Nombre': ['Silvana','Claudia','Rebeca','Elizabeth', 'N/A','Salome'],
        'Edad': ['41','35',np.nan,'30', '29','28'],
        'Profesion': ['Enfermera','Modista','Arquitecta','Trabajadora social', 'Manicurista','N/A'] 
        }

df2 = pd.DataFrame(datos2)
print(df2)
print('\n*2')
print(df2.info())
print('\n*2')