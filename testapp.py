# import dependencies
from flask import Flask
from flask.wrappers import Response
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, render_template, request, redirect
import os
import json

##########################################################
# Create an app
app = Flask(__name__)

##########################################################
# Connect to Postgres
##########################################################


app.config["DATABASE_URL"] = "postgresql://postgres:{pw}@localhost:5432/nbachamps"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



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


if __name__ == '__main__':
    app.run(debug=True)