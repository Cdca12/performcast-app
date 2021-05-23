import pyrebase
from config import firebaseConfig 

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

#########################
# Demo app
# Esta clase fuera el DAL
# TODO: Añadir archivo de config.json o equivalente, donde esté la info de la bd y el firebaseConfig

# Añadir información de la data
def añadirDatosAlumno(numero_control, semestre, creditos_acumulados, indices_depresion, nivel_estres, factores_socioeconomicos, calificacion_final):
    db.child("alumnos").child(numero_control).set({
        "semestre": semestre,
        "creditos_acumulados": creditos_acumulados,
        "indices_depresion": indices_depresion,
        "nivel_estres": nivel_estres,
        "factores_socioeconomicos": factores_socioeconomicos,
        "calificacion_final": calificacion_final
    })

# Datos de alumnos (mismos que la data)
# añadirDatosAlumno(17171345, 1,	27,	"Bajo",	"Medio",	"Clase media baja",	89)
# añadirDatosAlumno(17171456, 2,	55,	"Bajo",	"Medio",	"Clase media baja",	82)
# añadirDatosAlumno(17171424, 2,	55,	"Bajo",	"Medio",	"Clase media",	90)

# Obtener información del alumno
def obtenerInformacionAlumno(numero_control):
    alumnoDb = db.child("alumnos").child(numero_control).get().val()
    alumno = {
        "semestre": alumnoDb['semestre'],
        "creditos_acumulados": alumnoDb['creditos_acumulados'],
        "indices_depresion": alumnoDb['indices_depresion'],
        "nivel_estres": alumnoDb['nivel_estres'],
        "factores_socioeconomicos": alumnoDb['factores_socioeconomicos'],
        "calificacion_final": alumnoDb['calificacion_final']
    }
    return alumno


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
