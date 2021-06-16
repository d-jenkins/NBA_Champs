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

champs_results = session.query(Champs).first()
print (champs_results.id)

from sqlalchemy import inspect
insp = inspect(Champs)
insp.columns
list(insp.columns)

champs = db.Table('champs', db.metadata, autoload=True, autoload_with=db.engine)

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)

@app.route("/champstest")
def index():
    results = db.session.query(champs).all()
    results = json.dumps(results, cls = Encoder)
    # return render_template("/index.html", results=results)
    return results

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run(debug=True)