# import dependencies
from flask import Flask
from flask import SQLAlchemy
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



@app.route("/champs")
def champs():
     # Run scrapped functions
    nba_champs = mongo.db.blank_blank
    nba_data = all_stats.scrape_teams()
    nba_data = all_stats.scrape_every_season()
    teams_f = all_stats.scrape_stats()
    teams_w = all_stats.scrape_playoffs()
    nba_data = all_stats.scrape_all_rel_stats()
    teams_info.update({}, nba_data, upsert=True)

    return redirect("/", code=302)
    return render_template("/index.html")


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run(debug=True)