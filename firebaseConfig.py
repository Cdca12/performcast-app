# For Firebase JS SDK v7.20.0 and later, measurementId is optional
import config

firebaseConfig = {}

if config.TESTING == True:
    from firebaseTesting import firebaseTesting
    firebaseConfig = firebaseTesting
else:
    import os
    firebaseConfig = {
        "apiKey":  os.environ.get("apiKey"),
        "authDomain": os.environ.get("authDomain"),
        "databaseURL": os.environ.get("databaseURL"),
        "projectId": os.environ.get("projectId"),
        "storageBucket": os.environ.get("storageBucket"),
        "messagingSenderId": os.environ.get("messagingSenderId"),
        "appId": os.environ.get("appId"),
        "measurementId": os.environ.get("measurementId")
    }
