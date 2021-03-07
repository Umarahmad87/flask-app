"""
This script runs the AIGrader application using a development server.
"""

from os import environ
from AIGrader import app
from flask import Flask, request

app ==Flask(__name__);
"""
en-core-web-sm
pywin32
pywinpty==0.5.7
mkl-fft
mkl-random
mkl-service
setuptools==52.0.0.post20210125
tensorboard-plugin-wit==1.6.0
"""

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
