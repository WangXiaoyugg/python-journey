from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/shiyanlou')
def say_my_name():
    return 'garen'
if __name__ == '__main__':
    app.debug = True
    app.run()
