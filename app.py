from flask import Flask, json, jsonify, request
import numpy as np
import pickle

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

# Cargar modelos
model = pickle.load(open('model.pkl', 'rb'))

# TEST
@app.route('/', methods=['GET'])
def test():
    return jsonify({
        "status": 1,
        "message": 'Your app is online!',
        "data": ''
    })


# Obtener predicción
@app.route('/predict', methods=['POST'])
def obtenerPrediccion():
    status = 1
    message = ''
    data = ''

    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    # bind test
    data = output

    return jsonify({
        "status": status,
        "message": message,
        "data": data
    })


@app.route('/predict_api', methods=['POST'])
def predict_api():
    status = 1
    message = ''
    data = ''
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    valores = np.array(list(data.values()))
    prediction = model.predict([valores])
    probabilidad = model.predict_proba([valores])
    analisis = ''
    if prediction[0] == 0:
        analisis = 'Regular'
    elif probabilidad[0][1] > 0.90:
        analisis = "En peligro" # Tienen mas de un 90% de desertar
    elif probabilidad[0][1] > 0.70:
        analisis = "Critico" #Tienen de 70% a 90% de desertar
    else:
        analisis = "Irregular"  #Tienen de 50% a 70 % de desertar

    output = { 'desierta': int(prediction[0]), 'prob_si': probabilidad[0][1], 'prob_no': probabilidad[0][0], 'Analisis reticular': analisis }

    # bind test
    data = output
    print(data)
    return jsonify({
        "status": status,
        "message": message,
        "data": data
    })


if __name__ == '__main__':
    # Change this before deploying
    # app.run(debug=True)
    app.run()
