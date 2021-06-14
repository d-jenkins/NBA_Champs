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
<<<<<<< Updated upstream


app.config["DATABASE_URL"] = "postgresql://postgres:{pw}@localhost:5432/nbachamps"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
=======
>>>>>>> Stashed changes
db = SQLAlchemy(app)

##########################################################

<<<<<<< Updated upstream

@app.route("/",methods=['GET'])
def home(request):
    stats = []
    with db.connect() as conn:
        all_stats = conn.execute("select * from all_stats ").fetchall()
        stats = list(all_stats)
    data = {'stats': stats}
    resp = Response(json.dumps(data, status=200, mimetype='application/json')
    return render_template("index.html", stats=stats)


# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)
=======
stats = db.Table('all_stats', db.metadata, autoload=True, autoload_with=db.engine)


>>>>>>> Stashed changes

@app.route("/getdata")
def index():
    results = db.session.query(stats).all()
    return render_template("/index.html", results=results)

if __name__ == '__main__':
    app.run(debug=True)