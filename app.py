import os
from flask import Flask
from flask import render_template
import socket
import random
import os

app = Flask(__name__)

rockets = {
    "small": "small",
    "average": "average",
    "big": "big",
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
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    print(THIS_FOLDER);
    my_file = THIS_FOLDER + "/data/testfile.txt"
    print(my_file);
    f = open(my_file)
    contents = f.read()
    return render_template('hello.html', name=socket.gethostname(), contents=contents, rocket=rockets[rocket])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")