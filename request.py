import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'semestre':4, 'calificacion':60, 'creditos_acumulados':100, 'indices_depresion':2, 'nivel_estres':2, 'factores_socioeconomicos':3})

print(r.json())