from flask import Flask, render_template

app = Flask(__name__)



@app.route('/home/<name>')
def home(name):
	my_name = name
	letters = list(my_name)
	return render_template('index.html', name = my_name, letters = letters)



if __name__ == '__main__':
	app.run(debug=True)