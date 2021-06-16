# import dependencies
from flask import Flask
from flask.wrappers import Response
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask import Flask, render_template, request, redirect
from flask_marshmallow import Marshmallow
import os
import decimal
import json
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

##########################################################
# Create an app
app = Flask(__name__)
db = SQLAlchemy(app)
##########################################################
# Connect to Postgres
##########################################################


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:MildredChase84!@nba-champs.c6ka6apltccn.us-east-2.rds.amazonaws.com:5432/nbaChamps"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Base = automap_base()
engine = create_engine("postgresql+psycopg2://postgres:MildredChase84!@nba-champs.c6ka6apltccn.us-east-2.rds.amazonaws.com:5432/nbaChamps")

Base.prepare(engine, reflect=True)
Champs = Base.classes.champs

session = Session(engine)

champs_results = session.query(Champs).all()
print (champs_results)

from sqlalchemy import inspect
insp = inspect(Champs)
insp.columns
col = list(insp.columns)
print(col)


@app.route('/')
def index():
    db.session.query(champs_results)



if __name__ == '__main__':
    app.run(debug=True)
