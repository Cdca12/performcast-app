from flask import Flask, jsonify, request
import numpy as np
import pickle
import csv

import dataFirebase
import utils

app = Flask(__name__)

app.config.from_object('config')

# Cargar modelos
model = pickle.load(open('model.pkl', 'rb'))

# TEST
# TODO: Mostrar README.md del proyecto den GitHub
@app.route('/', methods=['GET'])
def test():
    return jsonify({
        "STATUS": 1,
        "MESSAGE": '¡Tu aplicación está funcionando correctamente!',
        "DATA": ''
    })

# Agregar información a la data
# Aqui recibimos todos los datos incluyendo la calificación final pasada, un hecho
@app.route('/datos', methods=['POST'])
def añadirDatos():
    status = 1
    message = ''
    data = ''

    # Obtenemos JSON
    bodyData = request.get_json(force=True)

    # Obtenemos en un arreglo solo los valores del JSON 
    arregloData = list(bodyData.values())

    # Insertamos registro en csv
    with open('rendimientos.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(arregloData)

    # Todo OK
    message = 'Se ha insertado el registro correctamente'
    data = bodyData

    return jsonify({
        "STATUS": status,
        "MESSAGE": message,
        "DATA": data
    })


# Obtener predicción de rendimiento
@app.route('/rendimiento/<string:numero_control>', methods=['GET'])
def predecirRendimiento(numero_control):
    status = 1
    message = ''
    data = ''

    # Obtenemos información del alumno con el numero de control
    alumno = dataFirebase.obtenerInformacionAlumno(numero_control)

    if not alumno:
        status = 0
        message = 'No existe un alumno con ese número de control'
        return jsonify({
            "STATUS": status,
            "MESSAGE": message,
            "DATA": data
    })

    # Obtenemos predicción con la información del alumno
    prediction = model.predict([np.array(list(alumno.values()))])

    # Armamos respuesta con los resultados de la prediccion                                                                                                                                             
    calificacion_final = prediction[0]
    rendimiento = utils.obtenerRendimiento(calificacion_final)    

    data = {
        "calificacion_final": calificacion_final,
        "rendimiento": rendimiento
    }

    return jsonify({
        "STATUS": status,
        "MESSAGE": message,
        "DATA": data
    })


if __name__ == '__main__':
    app.run()
