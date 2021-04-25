from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Fala galera!'

@app.route('/bye')
def bye():
    return 'Bye bye'


if __name__ == '__main__':
    app.run()
