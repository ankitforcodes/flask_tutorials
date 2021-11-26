from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/signup_page')
def signup():
	return render_template('signup.html')


@app.route('/thanks')
def thankyou():
	fname = request.args.get('fname')
	lname = request.args.get('lname')
	return render_template('thankyou.html', fname = fname, lname = lname)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug=True)