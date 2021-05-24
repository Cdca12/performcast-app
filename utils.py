# Convertir datos cualitativos en cuantitativos
# Se les da un valor numérico para poder hacer operaciones y entrenar el modelo

def nivel_indices_to_int(word):
     word_dict = {'Bajo' : 1, 'Medio' : 2, 'Alto' :3, 0: 0}
     return word_dict[word]

def factores_to_int(word):
     word_dict = {'Clase baja' : 1, 'Clase media baja' : 2, 'Clase media' :3, 'Clase media alta' : 4, 'Clase alta' : 5, 0 : 0}
     return word_dict[word]



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