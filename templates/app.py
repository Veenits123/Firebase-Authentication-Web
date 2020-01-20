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

# email=input("enter email\n")
# password=input("enter password \n")

# user=auth.create_user_with_email_and_password(email,password)

# auth.get_account_info(user['idToken'])

@app.route('/', methods=['GET', 'POST'])

def basic():
	unsuccessful = 'Please check your credentials'
	successful = 'Login successful'
	if request.method == 'POST':
		email = request.form['name']
		password = request.form['pass']
		try:
			auth.sign_in_with_email_and_password(email, password)
			return render_template('index.html', s=successful)
		except:
			return render_template('signup.html', us=unsuccessful)

	return render_template('index.html')

app.route('/signup', methods=['GET', 'POST'])

def basic():
	
	if request.method == 'POST':
		email = request.form['name']
		password = request.form['pass']
		try:
			#auth.sign_in_with_email_and_password(email, password)
			auth.create_user_with_email_and_password(email,password)
			return render_template('signup.html', s=successful)
		except:
			return render_template('signup.html', us=unsuccessful)

	return render_template('signup.html')

if __name__ == '__main__':
	app.run()
