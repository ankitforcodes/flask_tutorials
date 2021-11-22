from flask import Flask, render_template

app = Flask(__name__)



@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/info/<name>')
def index(name):
	return '<h1>hi ' + name + '</h1>'

if __name__ == '__main__':
	app.run(debug=True)