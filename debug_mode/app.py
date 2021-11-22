from flask import Flask

app = Flask(__name__)

@app.route('/info/<name>')
def index(name):
	return '<h1>hi ' + name + '</h1>'

if __name__ == '__main__':
	app.run(debug=True)