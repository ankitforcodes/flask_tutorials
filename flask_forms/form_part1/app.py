from flask import Flask, render_template, session, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, DateTimeField,
                     RadioField, SelectField, TextAreaField, validators)
# from wtforms.validators import InputRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'


class InfoForm(FlaskForm):
    fname = StringField('Whats ur first name? ', validators=[validators.InputRequired()])
    teenage_flag = BooleanField('Are you teenager?')
    gender = RadioField('Select your gender', choices=[('M', 'Male'), ('F', 'Female')])
    comm_mode = SelectField('Select your communication mode',
                            choices=[('email', 'Email'), ('text', 'SMS'), ('call', 'Call')])
    about_you = TextAreaField()
    submit = SubmitField('Send')


@app.route('/home', methods=['GET', 'POST'])
def index():
    myform = InfoForm()

    if myform.validate_on_submit():
        print("Enter form validated")
        session['first_name'] = myform.fname.data
        session['teenage_flag'] = myform.teenage_flag.data
        session['gender'] = myform.gender.data
        session['comm_mode'] = myform.comm_mode.data
        session['about_you'] = myform.about_you.data

        return redirect(url_for('thanks'))

    return render_template('index.html', html_form=myform)


@app.route('/thanks')
def thanks():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
