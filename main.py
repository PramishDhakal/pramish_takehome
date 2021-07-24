from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello! This is a test run for pramish take home test !!!! '


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

