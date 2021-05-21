# Importamos las librerías a usar
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataSet = pd.read_csv('rendimientos.csv');
dataSet['indices_depresion'].fillna('Medio', inplace=True)
dataSet['nivel_estres'].fillna('Medio', inplace=True)
dataSet['factores_socioeconomicos'].fillna('Clase media', inplace=True)

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

from sklearn.linear_model import LogisticRegression
regressor = LogisticRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))

test = [4, 60, 100, 2, 2, 3]
print(model.predict([test]))
print(model.predict_proba([test]))