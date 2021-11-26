from flask import Flask, render_template

app = Flask(__name__)



@app.route('/home/<name>')
def home(name):
	my_name = name
	letters = list(my_name)
	return render_template('home.html', name = my_name, letters = letters)

@app.route('/yolo')
def second_page():
	return render_template('page2.html')


if __name__ == '__main__':
	app.run(debug=True)