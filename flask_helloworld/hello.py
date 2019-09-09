from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!\n'

if __name__ == '__main__':
	# must bind to 0.0.0.0 to be visible outside the docker container
    app.run(debug=True, host='0.0.0.0')
