# import dependencies
from flask import Flask
from flask.wrappers import Response
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask import Flask, jsonify, render_template, request, redirect
from flask_marshmallow import Marshmallow
import os
import json

##########################################################
# Create an app
app = Flask(__name__)
# Connect to Postgres
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:MildredChase84!@nba-champs.c6ka6apltccn.us-east-2.rds.amazonaws.com:5432/nbaChamps"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
##########################################################
db = SQLAlchemy(app)

##########################################################

stats = db.Table('all_stats', db.metadata, autoload=True, autoload_with=db.engine)



@app.route("/getdata")
def index():
    results = db.session.query(stats).all()
    return render_template("/index.html", results=results)

if __name__ == '__main__':
    app.run(debug=True)