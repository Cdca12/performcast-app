# Importamos las librerías a usar
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import pyodbc

server = '10.10.99.113\sqlutilerias' 
database = 'pruebas' 
username = 'rwong' 
password = '456852' 
query = "SELECT * FROM Cat_Colores"
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

df = pd.read_sql(query, conn)
print(df)

#cursor = conn.cursor()
#cursor.execute('SELECT * FROM Cat_Colores')
#for row in cursor:
#   print(row)

dataSet = pd.read_csv('rendimientos.csv');
dataSet['indices_depresion'].fillna('Medio', inplace=True)
dataSet['nivel_estres'].fillna('Medio', inplace=True)
dataSet['factores_socioeconomicos'].fillna('Clase media', inplace=True)

print('---------------------------')
X = dataSet.iloc[:, :6]

def nivel_indices_to_int(word):
     word_dict = {'Bajo' : 1, 'Medio' : 2, 'Alto' :3, 0: 0}
     return word_dict[word]

def factores_to_int(word):
     word_dict = {'Clase baja' : 1, 'Clase media baja' : 2, 'Clase media' :3, 'Clase media alta' : 4, 'Clase alta' : 5, 0 : 0}
     return word_dict[word]

X['indices_depresion'] = X['indices_depresion'].apply(lambda x : nivel_indices_to_int(x))
X['nivel_estres'] = X['nivel_estres'].apply(lambda x : nivel_indices_to_int(x))
X['factores_socioeconomicos'] = X['factores_socioeconomicos'].apply(lambda x : factores_to_int(x))

y = dataSet.iloc[:, -1]
#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2, 88, 50, 1, 2, 1]]))