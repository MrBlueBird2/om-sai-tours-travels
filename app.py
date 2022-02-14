from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from dotenv import load_dotenv
load_dotenv()

import os

user_name = os.environ.get('USER')
password = os.environ.get('PASSWORD')

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = user_name
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def main_home_page():
	if request.method == 'POST':
		name = request.form['name']
		phone = request.form['phone']
		pickup = request.form['pickup']

		msg = Message(sender ='badrivishalmanitripathi@gmail.com',recipients=['badrivishalmanitripathi@gmail.com'])
		msg.subject = "New Customer"
		msg.body = "Hello, You have new customer, Contact the customer using his phone number {} , His/Her Pickup Location is {} , His/Her name is {} ".format(phone, pickup, name)
		mail.send(msg)
		return "Sent"

	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True, port=8000, host="localhost")
