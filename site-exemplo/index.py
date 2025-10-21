import flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def menu_principal():
    return 'Olá, primeiro site em python :) '

if __name__ == '__main__':
    app.run(debug=True)