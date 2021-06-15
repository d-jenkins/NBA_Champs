import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask
from flask.wrappers import Response
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, render_template, request, redirect
import os
import json


#################################################
# Database Setup
#################################################
engine = create_engine("postgresql://postgres:{'SteveO2021'}@localhost:5432/nbachamps")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
all_stats = Base.classes.all_stats

import psycopg2
import sys
from  flask import Flask,render_template, jsonify
from flask_marshmallow import Marshmallow


##########################################################
# Create an app
app = Flask(__name__)

class stats(db.Model):

@app.route('/')
def send_data():
    # conn = psycopg2.connect("dbname=nbaChamps user=postgres password=MildredChase84!")
    conn = psycopg2.connect(
    host = "nba-champs.c6ka6apltccn.us-east-2.rds.amazonaws.com",
    database="nbaChamps",
    user="postgres",
    password="MildredChase84!")
    
    cur = conn.cursor()
    cur.execute("""select * from  all_stats""")
    data = [col for col in cur]
    cur.close()
    return jsonify({'results', data})


if __name__ == '__main__':
    app.run(debug=True)
