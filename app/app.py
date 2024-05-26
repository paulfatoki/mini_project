# Flask Application
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello bisi ,you are welcome to my world!"

@app.route('/create')
def create():
   a=100
   b=50
   c=a+b
   return "This is the result " + str(c)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8001, debug =True)
