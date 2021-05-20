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
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    
    # bind test
    data = output

    return jsonify({
        "status": status,
        "message": message,
        "data": data
    })


if __name__ == '__main__':
    # Change this before deploying
    # app.run(debug=True)
    app.run()
