from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from dotenv import load_dotenv
load_dotenv()

import os

user_name = os.environ.get('USER')
password = os.environ.get('PASSWORD')

formCode='''
<div class="row justify-content-center" style="margin-top: -20px;">
	<div class="col-md-6">
	<form action="/" method="POST">
	<div class="mb-3">
		<label for="phone" class="form-label text-light">Phone Number</label>
		<input type="text" class="form-control" name="phone" id="phone" aria-describedby="emailHelp"
		style="background: rgba(255, 255, 255, 0.5)">
	</div>
	<div class="mb-3">
		<label for="pickup" class="form-label text-light">Pickup Location</label>
		<input type="text" class="form-control" name="pickup" id="pickup"
		style="background: rgba(255, 255, 255, 0.5)">
	</div>
	<div class="mb-3">
		<label for="name" class="form-label text-light">Your Name</label>
		<input type="text" class="form-control" name="name" id="name"
		style="background: rgba(255, 255, 255, 0.5)">
	</div>
	<button type="submit" class="btn btn-danger py-2 p-4">Submit</button>
	</form>
	</div>
</div>
'''

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
