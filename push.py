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

auth = firebase.auth()

db = firebase.database()

# @app.route('/', methods=['GET', 'POST'])
# def basic():
# 	if request.method == 'POST':
# 		if request.form['submit'] == 'add':

# 			name = request.form['name']
# 			db.child("todo").push(name)
# 			todo = db.child("todo").get()
# 			to = todo.val()
# 			return render_template('push.html', t=to.values())
# 		elif request.form['submit'] == 'delete':
# 			db.child("todo").remove()
# 		return render_template('push.html')
# 	return render_template('push.html')



@app.route('/', methods=['GET', 'POST'])

def basic():
    if request.method == 'POST':
        if request.form['name'] and request.form['pass']:
        
            #variables to hold the requested form elements 
            name = request.form['name']
            password = request.form['pass']

            # Cursor for execution of SQL statements in Flask
            db.child("detail").push(name)
            user=auth.create_user_with_email_and_password(name,password)
            db.child("detail").push(user)
        return render_template('signup.html')
            # Cursor needs to be committed for execution of the SQL commands
            #cursor.connection.commit()
            # Always close the cursor
            #cursor.close()






















if __name__ == '__main__':
	app.run(debug=True)












