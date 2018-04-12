from flask import Flask, jsonify, render_template, redirect, url_for, flash
from app.views import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/huffman-coding')
def huffman():
    result = coding()
    return render_template('index.html', responce=result)


@app.route('/encode-message')
def encode_message():
    result = message_coding()
    return render_template('index.html', responce=result)


if __name__ == '__main__':
    app.secret_key = '$6j1v32x+5)$d@uv)_)ek-9cb41q3+$)t20s)%la92ra#&63_*'
    app.debug = True
    app.run()
