import pyrebase
from config import firebaseConfig 

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

#########################
# Demo app
# Esta clase fuera el DAL
# TODO: Añadir archivo de config.json o equivalente, donde esté la info de la bd y el firebaseConfig

# Añadir tupla de la data
def añadirTupla(semestre, creditos_acumulados, indices_depresion, nivel_estres, factores_socioeconomicos, calificacion_final):
    db.child("rendimientos").push({
        "semestre": semestre,
        "creditos_acumulados": creditos_acumulados,
        "indices_depresion": indices_depresion,
        "nivel_estres": nivel_estres,
        "factores_socioeconomicos": factores_socioeconomicos,
        "calificacion_final": calificacion_final
    })

# Datos de la data
# añadirTupla(1, 90, 100,	"Bajo",	"Bajo",	"Clase baja", "Excelente")
# añadirTupla(5,	70,	200,	"Medio",	"Medio",	"Clase media baja",	"Excelente")
# añadirTupla(7,	60,	100,	"Alto",	"Alto",	"Clase media",	"Excelente")
# añadirTupla(10,	100,	200,	"Bajo",	"Bajo",	"Clase media alta",	"Notable")
# añadirTupla(1, 90, 100,	"Bajo",	"Bajo",	"Clase baja", "Excelente")
# añadirTupla(5,	70,	200,	"Medio",	"Medio",	"Clase media baja",	"Excelente")
# añadirTupla(7,	60,	100,	"Alto",	"Alto",	"Clase media",	"Excelente")
# añadirTupla(10,	100,	200,	"Bajo",	"Bajo",	"Clase media alta",	"Notable")
# añadirTupla(1, 90, 100,	"Bajo",	"Bajo",	"Clase baja", "Excelente")
# añadirTupla(5,	70,	200,	"Medio",	"Medio",	"Clase media baja",	"Excelente")
# añadirTupla(7,	60,	100,	"Alto",	"Alto",	"Clase media",	"Excelente")
# añadirTupla(10,	100,	200,	"Bajo",	"Bajo",	"Clase media alta",	"Notable")
# añadirTupla(1, 90, 100,	"Bajo",	"Bajo",	"Clase baja", "Excelente")
# añadirTupla(5,	70,	200,	"Medio",	"Medio",	"Clase media baja",	"Excelente")
# añadirTupla(7,	60,	100,	"Alto",	"Alto",	"Clase media",	"Excelente")

# Regresar data de la bd
def obtenerData():
    data = db.child("rendimientos").get()
    return data

#########################
# Script de test, aprendiendo a usar el firebase

# Create table users
# db.child("users").set("Users table")

# Add grade
# def addGrade(numeroControl, calificacion):
#     db.child("users").child(numeroControl).update({
#         "calificacion": calificacion
#     })

# addGrade(17171345, [50, 90, 100])

# Update user
# db.child("users").child("1").update({
#     "name": "Chris",
#     "age": 21
# })

# Delete user
# db.child("users").remove()

# Edit user
# def writeUserData(userId, name, email, imageUrl):
#     db.child("users").ref('users/' + userId).set({
#         "username": name,
#         "email": email,
#         "profile_picture": imageUrl
#     })
