import os
from flask import Flask
from flask import render_template
import socket
import random
import os

app = Flask(__name__)

rockets = {
    "small": "small.jpg",
    "average": "average.jpg",
    "big": "big.jpg",
}

rocket = os.environ.get('APP_ROCKET') or random.choice(["small","average","big"])

@app.route("/")
def main():
    #return 'Hello'
    print(rocket)
    return render_template('hello.html', name=socket.gethostname(), rocket=rockets[rocket])

@app.route('/rocket/<new_rocket>')
def new_rocket(new_rocket):
    return render_template('hello.html', name=socket.gethostname(), rocket=rockets[new_rocket])

@app.route('/read_file')
def read_file():
    f = open("/data/testfile.txt")
    contents = f.read()
    return render_template('hello.html', name=socket.gethostname(), contents=contents, rocket=rockets[rocket])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")