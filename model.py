# Importamos las librerías a usar
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import utils

# Leer data del csv
dataSet = pd.read_csv('rendimientos.csv');

# Rellenar data en celdas vacias
dataSet['indices_depresion'].fillna('Medio', inplace=True)
dataSet['nivel_estres'].fillna('Medio', inplace=True)
dataSet['factores_socioeconomicos'].fillna('Clase media', inplace=True)

# Obtenemos datos de entrada
X = dataSet.iloc[:, :5]


# Convertir datos cualitativos en cuantitativos
# Se les da un valor numérico para poder hacer operaciones y entrenar el modelo
X['indices_depresion'] = X['indices_depresion'].apply(lambda x : utils.nivel_indices_to_int(x))
X['nivel_estres'] = X['nivel_estres'].apply(lambda x : utils.nivel_indices_to_int(x))
X['factores_socioeconomicos'] = X['factores_socioeconomicos'].apply(lambda x : utils.factores_to_int(x))

# Obtenemos los resultados existentes
Y = dataSet.iloc[:, -1]

# Como tenemos un dataset pequeño, entrenaremos el modelo con toda la información disponible

# Se usa un Algoritmo de Regresión Lineal
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

# Ajustamos modelo con la data entrenada
regressor.fit(X, Y)

print('---------------------------')

# Guardamos el modelo en disco
try:
     pickle.dump(regressor, open('model.pkl','wb'))
     print('¡El modelo se ha generado con éxito!')
except Exception as e:
     raise Exception("No se pudo generar el modelo", e)

######################################################################################################

# Test:
# Cargamos modelo para comparar resultados
try:
     model = pickle.load(open('model.pkl','rb'))
     print("Predicción de prueba:", model.predict([[5, 138, 1, 3, 5]]))
except Exception as e:
     raise Exception("No se pudo ejecutar la prueba del modelo", e)

print('---------------------------')

