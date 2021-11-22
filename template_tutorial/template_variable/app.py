from flask import Flask, render_template

app = Flask(__name__)



@app.route('/home')
def home():
	my_name = 'Ankit'
	return render_template('index.html', name = my_name)



if __name__ == '__main__':
	app.run(debug=True)