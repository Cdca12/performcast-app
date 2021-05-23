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
    if not alumnoDb:
        return None

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
# añadirDatosAlumno(17170013,	1,	27,	"Bajo",	"Medio", "Clase media baja")
# añadirDatosAlumno(17171043,	2,	55,	"Bajo",	"Medio",	"Clase media baja")
# añadirDatosAlumno(17170562,	2,	55,	"Bajo",	"Medio",	"Clase media")
# añadirDatosAlumno(17170014,	2,	60,	"Bajo",	"Medio",	"Clase media baja")
# añadirDatosAlumno(17170015,	2,	55,	"Bajo",	"Alto",	"Clase media")
# añadirDatosAlumno(17170600,	2,	50,	"Medio",	"Bajo",	"Clase baja")
# añadirDatosAlumno(17170601,	3,	73,	"Medio",	"Bajo",	"Clase baja")
# añadirDatosAlumno(17170016,	3,	83,	"Bajo",	"Alto",	"Clase alta")
# añadirDatosAlumno(17170017,	4,	112,	"Bajo",	"Alto",	"Clase media alta")
# añadirDatosAlumno(17170826,	4,	116,	"Bajo",	"Alto",	"Clase media alta")
# añadirDatosAlumno(17170018,	4,	107,	"Medio",	"Medio",	"Clase media baja")
# añadirDatosAlumno(17170019,	5,	130,	"Alto",	"Alto",	"Clase media baja")
# añadirDatosAlumno(17170020,	5,	138,	"Bajo",	"Medio",	"Clase media")
# añadirDatosAlumno(17170021,	5,	138,	"Bajo",	"Alto",	"Clase alta")
# añadirDatosAlumno(17170522,	5,	138,	"Bajo",	"Bajo",	"Clase alta")



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
