# import dependencies
from flask import Flask
from flask.wrappers import Response
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask import Flask, render_template, request, redirect, jsonify
from flask_marshmallow import Marshmallow
import os
import decimal
import json
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData

##########################################################
# Create an app
app = Flask(__name__)
db = SQLAlchemy(app)
##########################################################
# Connect to Postgres
##########################################################


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:MildredChase84!@nba-champs.c6ka6apltccn.us-east-2.rds.amazonaws.com:5432/nbaChamps"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# engine = create_engine("postgresql+psycopg2://postgres:MildredChase84!@nba-champs.c6ka6apltccn.us-east-2.rds.amazonaws.com:5432/nbaChamps")

# Base.prepare(engine, reflect=True)
# Champs = Base.classes.champs

# session = Session(engine)


# champs = db.Table('champs', db.metadata, autoload=True, autoload_with=db.engine)


metadata = MetaData()
metadata.reflect(db.engine, only=['champs'])
Base = automap_base(metadata=metadata)
Base.prepare(db.engine, reflect=True)
Champs = Base.classes.champs

from sqlalchemy import inspect
insp = inspect(Champs)
insp.columns
col = list(insp.columns)
print(col)


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)

@app.route('/champs')
def index():

    results = db.session.query(Champs).all()
    champs_d = json.dumps(results, cls = Encoder)
    # champ = db.session.query(Champs).all()
     # return jsonify({'results', results_r})
    # print(champs_dict)
    champs_dict = []
    for data in results:
        champs_dict.append(data)
        champs_d = json.dumps(results, cls = Encoder)
        print(col)
        return ''
    
    # return jsonify(data)
    # return champs_dict




# @app.route('/')
# def index():
#     champs_results = session.query(Champs).all()
#     for c in champs_results:
#         print (c)
# champs_dict = []
# @app.route('/champs')
# def index():
#     for u in db.session.query(Champs).all():
#         return jsonify(u.__dict__)



if __name__ == '__main__':
     app.run(debug=True)
