import pyrebase
from config import firebaseConfig 
import utils 

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

#########################
# Demo app
# Esta clase fuera el DAL

# Añadir información de la data
def añadirDatosAlumno(numero_control, semestre, creditos_acumulados, indices_depresion, nivel_estres, factores_socioeconomicos):
    db.child("alumnos").child(numero_control).set({
        "semestre": semestre,
        "creditos_acumulados": creditos_acumulados,
        "indices_depresion": indices_depresion,
        "nivel_estres": nivel_estres,
        "factores_socioeconomicos": factores_socioeconomicos,
    })

# Obtener información del alumno
def obtenerInformacionAlumno(numero_control):
    alumnoDb = db.child("alumnos").child(numero_control).get().val()
    alumno = {
        "semestre": alumnoDb['semestre'],
        "creditos_acumulados": alumnoDb['creditos_acumulados'],
        "indices_depresion": utils.nivel_indices_to_int(alumnoDb['indices_depresion']), 
        "nivel_estres": utils.nivel_indices_to_int(alumnoDb['nivel_estres']),
        "factores_socioeconomicos": utils.factores_to_int(alumnoDb['factores_socioeconomicos'])
    }
    return alumno

# Test  Inicial
# Datos de alumnos (mismos que la data)
# añadirDatosAlumno(17171345, 1,	27,	"Bajo",	"Bajo",	"Clase media baja")
# añadirDatosAlumno(17171456, 2,	55,	"Bajo",	"Medio",	"Clase media baja")
# añadirDatosAlumno(17171424, 2,	55,	"Bajo",	"Medio",	"Clase media")


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
