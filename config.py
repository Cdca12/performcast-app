# Your web app's Firebase configuration
# For Firebase JS SDK v7.20.0 and later, measurementId is optional
import os

firebaseConfig = {
    "apiKey": os.getenv("apiKey", "optional-default"),
    "authDomain": os.getenv("authDomain", "optional-default"),
    "databaseURL": os.getenv("databaseURL", "optional-default"),
    "projectId": os.getenv("projectId", "optional-default"),
    "storageBucket": os.getenv("storageBucket", "optional-default"),
    "messagingSenderId": os.getenv("messagingSenderId", "optional-default"),
    "appId": os.getenv("appId", "optional-default"),
    "measurementId": os.getenv("measurementId", "optional-default"),
}

