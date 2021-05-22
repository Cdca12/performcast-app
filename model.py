# Importamos las librerías a usar
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

# dataSet = pd.read_csv('hiring.csv')

# dataSet['experience'].fillna(0, inplace=True)
# dataSet['test_score'].fillna(dataSet['test_score'].mean(), inplace=True)

# X = dataSet.iloc[:, :3]

# #Converting words to integer values
# def convert_to_int(word):
#     word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
#                 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, 0: 0}
#     return word_dict[word]

# X['experience'] = X['experience'].apply(lambda x : convert_to_int(x))

# y = dataSet.iloc[:, -1]

# Leer data del csv
dataSet = pd.read_csv('rendimientos.csv');

# Rellenar data en celdas vacias
dataSet['indices_depresion'].fillna('Medio', inplace=True)
dataSet['nivel_estres'].fillna('Medio', inplace=True)
dataSet['factores_socioeconomicos'].fillna('Clase media', inplace=True)

print('---------------------------')

# Obtenemos datos de entrada
X = dataSet.iloc[:, :5]

# Convertir datos cualitativos en cuantitativos
# Se les da un valor numérico para poder hacer operaciones y entrenar el modelo

def nivel_indices_to_int(word):
     word_dict = {'Bajo' : 1, 'Medio' : 2, 'Alto' :3, 0: 0}
     return word_dict[word]

def factores_to_int(word):
     word_dict = {'Clase baja' : 1, 'Clase media baja' : 2, 'Clase media' :3, 'Clase media alta' : 4, 'Clase alta' : 5, 0 : 0}
     return word_dict[word]

X['indices_depresion'] = X['indices_depresion'].apply(lambda x : nivel_indices_to_int(x))
X['nivel_estres'] = X['nivel_estres'].apply(lambda x : nivel_indices_to_int(x))
X['factores_socioeconomicos'] = X['factores_socioeconomicos'].apply(lambda x : factores_to_int(x))

# Obtenemos los resultados existentes
Y = dataSet.iloc[:, -1]


# Como tenemos un dataset pequeño, entrenaremos el modelo con toda la información disponible

# Se usa un Algoritmo de Regresión Lineal
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

# Ajustamos modelo con la data entrenada
regressor.fit(X, Y)

# Guardamos el modelo en disco
try:
     pickle.dump(regressor, open('model.pkl','wb'))
     print('¡El modelo se ha generado con éxito!')
except Exception as e:
     raise Exception("No se pudo generar el modelo", e)

########################################################

# Test:
# Cargamos modelo para comparar resultados
try:
     model = pickle.load(open('model.pkl','rb'))
     print("Predicción de prueba:", model.predict([[5, 138, 1, 3, 5]]))
except Exception as e:
     raise Exception("No se pudo ejecutar la prueba del modelo", e)


