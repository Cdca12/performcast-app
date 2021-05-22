from flask import Flask, jsonify, request
import numpy as np
import pickle
import csv

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

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
@app.route('/rendimiento', methods=['POST'])
def predecirRendimiento():
    status = 1
    message = ''
    data = ''

    bodyData = request.get_json(force=True)
    prediction = model.predict([np.array(list(bodyData.values()))])

    # Armamos respuesta con los resultados de la prediccion
    calificacion_final = prediction[0]
    rendimiento = obtenerRendimiento(calificacion_final)

    data = {
        "calificacion_final": calificacion_final,
        "rendimiento": rendimiento
    }

    return jsonify({
        "STATUS": status,
        "MESSAGE": message,
        "DATA": data
    })

# Método para regresar el rendimiento basándose en la predicción de la calificación final
def obtenerRendimiento(calificacion_final):
    rendimiento = ''

    # Basandonos en la Matriz de rendimiento escolar
    if calificacion_final >= 95:
        rendimiento = 'Excelente'
    elif calificacion_final >= 85 and calificacion_final <= 94:
        rendimiento = 'Notable'
    elif calificacion_final >= 76 and calificacion_final <= 84:
        rendimiento = 'Bueno'
    elif calificacion_final >= 70 and calificacion_final <= 75:
        rendimiento = 'Suficiente'
    elif calificacion_final < 70:
        rendimiento = 'Insuficiente'

    return rendimiento


if __name__ == '__main__':
    # Change this before deploying
    app.run(debug=True)
    # app.run()
