
import pandas as pd

datos = {
    'Nombres': ['Esteban', 'Claudia', 'Rebeca', 'Lichi'], 
    'Ciudad': ['New York','Bogota','Celestial','Batrrrcelona'], 
    'Comida': ['Pasta','Sancocho','Tiramisu','Obleas'], 
    'Pais' : ['Estados Unidos','Colombia','Cielo','Colombia']
    }

df = pd.DataFrame(datos)
print(df)
