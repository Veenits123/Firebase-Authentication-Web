import pyrebase
from flask import *
app = Flask(__name__)
config = {
    "apiKey": "AIzaSyCUKYI8DT8PxrFoUokJ8DMNZtkfjqw7Y5U",
    "authDomain": "myproject-470ac.firebaseapp.com",
    "databaseURL": "https://myproject-470ac.firebaseio.com",
    "projectId": "myproject-470ac",
   "storageBucket": "myproject-470ac.appspot.com",
    "messagingSenderId": "1066158301685",
    "appId": "1:1066158301685:web:6aad4628b1f2b70f7b40bc",
    "measurementId": "G-BL0SLN7EF2"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

db.child("names").push({"name:"veenit"})