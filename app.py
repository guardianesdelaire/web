from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/participa')
def participa():
    return render_template("participa.html")

@app.route('/sobre-nosotros')
def sobrenosotros():
    return render_template("sobrenosotros.html")

if __name__ == '__main__':
	app.debug = True
	app.run()