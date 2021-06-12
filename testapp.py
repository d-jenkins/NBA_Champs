# import dependencies
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, render_template, request, redirect
import os

##########################################################
# Create an app
app = Flask(__name__)

##########################################################
# Connect to Postgres
##########################################################


app.config["DATABASE_URL"] = "'postgresql://postgres:{pw}@localhost:5432/nbachamps'"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



@app.route("/")
def home():
    return render_template("/index.html")


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run(debug=True)