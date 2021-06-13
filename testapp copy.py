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



##########################################################
# Create an app
app = Flask(__name__)

##########################################################
# Connect to Postgres
##########################################################

