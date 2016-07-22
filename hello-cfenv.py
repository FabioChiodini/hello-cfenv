from __future__ import print_function
import os
import uuid
from flask import Flask, render_template, request
import socket
from cfenv import AppEnv

#cfenv = require("cfenv")
#envkk = cfenv.getAppEnv(port)

env = AppEnv()
app = Flask(__name__)
hostk1 = socket.gethostname()
my_uuid = str(uuid.uuid1())
BLUE = "#0099FF"
GREEN = "#33CC33"

COLOR = GREEN

@app.route('/')
def hello():
    return render_template("index.html",bgcolor=COLOR,guid=my_uuid,namek=env.name,hostk=hostk1,portk=env.port,appk=env.app)

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=env.port)
