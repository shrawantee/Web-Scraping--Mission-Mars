from flask import Flask, render_template, redirect,jsonify
from flask_pymongo import PyMongo
import scrape_mars
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    listings_news = mongo.db.listings_news.find_one()
    return render_template("index.html", listings_news=listings_news)

@app.route("/scrape")
def scrape():
    
