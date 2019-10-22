from flask import Flask

app = Flask(__name__)

@app.route('/sayhi/<name>')
def sayhi(name):
	return 'Hello ' + name

app.run()