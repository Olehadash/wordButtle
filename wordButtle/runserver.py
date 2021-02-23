"""
This script runs the wordButtle application using a development server.
"""

from os import environ
from wordButtle import app, socketio

if __name__ == '__main__':
    socketio.run(app,host = "localhost", port = 8080)
