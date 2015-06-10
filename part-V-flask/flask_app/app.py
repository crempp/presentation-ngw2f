from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello, World! (from Flask)'

if __name__ == '__main__':
    app.run(port=8000)