# By: Esteban Iafrancesco
# curso MinTIC
# 20-06-2021

import pandas as pd

def CasosCovid(ruta_archivo_csv: str ) -> dict:
    if ruta_archivo_csv.endswith('.csv'):
        try:
            data = pd.read_csv(ruta_archivo_csv)
        except:
            return 'Error al leer el archivo de datos'
        dataEntrante = data[['ID de caso','Ciudad de ubicación','Edad','Sexo', 'Estado']]
        # print(dataEntrante)
        dataFiltrada = data[['ID de caso', 'Estado']]
        data_salida = dataFiltrada.groupby(['Estado']).count()
    else:
        return 'Extensión inválida'
    
    data_salida = data_salida.to_dict()
    return data_salida

# print(CasosCovid('https://raw.githubusercontent.com/bernoulli/MisionTIC2022/main/casos_covid_19.csv'))
            