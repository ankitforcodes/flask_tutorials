from flask import Flask, render_template
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

class InfoForm(FlaskForm):
	fname = StringField('Whats ur first name? ')
	submit = SubmitField('Send')


@app.route('/home', methods = ['GET', 'POST'])
def index():
	first_name = False
	myform = InfoForm()

	if myform.validate_on_submit():
		print("Enter form validated")
		first_name = myform.fname.data
		myform.fname.data = ''

	return render_template('index.html', html_form = myform, first_name = first_name)


if __name__ == '__main__':
	app.run(debug = True)