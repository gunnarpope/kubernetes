# Flask-Docker Tutorial
@gunnarpope on telegram

## Build the python code

```python
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!\n'

if __name__ == '__main__':
    # must bind to 0.0.0.0 to be visible outside the docker container
    app.run(debug=True, host='0.0.0.0')
```

Notice that the host must bind to IP `0.0.0.0` for it to be a visible service outside of the docker container.


## Build the docker image
	```
	~/repos/kubernetes/flask_helloworld $ docker build -t gunnarpope/hello:v0.1 .

	~/repos/kubernetes/flask_helloworld $ docker images
	REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
	gunnarpope/hello    v0.1                2ae135e30c59        36 seconds ago      184MB
	```

## Log into your docker account in the terminal

	~/repos/kubernetes/flask_helloworld $ docker login -u gunnarpope 
	Password: 
	Login Succeeded
	

## Push the docker image to a remote repo

	```
	~/repos/kubernetes/flask_helloworld $ docker push gunnarpope/hello:v0.1
	The push refers to repository [docker.io/gunnarpope/hello]
	cde1a0cd76ad: Pushed 
	853ec9782f1f: Pushed 
	4d7d5ef347a3: Layer already exists 
	07208ab1af6f: Layer already exists 
	0cbac64398b8: Layer already exists 
	523a99e3c88d: Layer already exists 
	1c95c77433e8: Layer already exists 
	v0.1: digest: sha256:484926c059ce69f924e8487eff55512e12bada22ef8d1f3c69b682d291b6e758 size: 1789
	```

## Run the docker image

	docker run -d -p 5000:5000  gunnarpope/hello:v0.1 
	af5d583fcae739408a78f15e68b050c8a4f5ea3893bd9b234597c75c3447c053

	$ docker run -d -p 5000:5000  gunnarpope/hello:v0.1

The `-d` flag runs the app without displaying to the output. 

## Navigate to `localhost:5000` to see the helloworld display.
	
	```
	~/repos/kubernetes/flask_helloworld $ curl localhost:5000
	Hello, World!
	```



