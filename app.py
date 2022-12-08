# This is a app module
import pandas as pd

from flask import Flask

app = Flask(__name__)
  
@app.route('/')
def index():
    return 'Default API'


@app.route('/login')
def login():
    return 'Login API'

@app.route('/result')
def result():
    return 'Result API'


if __name__ == '__main__':
    app.run(debug=True)