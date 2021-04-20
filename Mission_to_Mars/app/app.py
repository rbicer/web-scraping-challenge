#Import
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo Connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

#ROUTES
@app.route("/")
def index():
    
    #Find the data from the Mongo db and return template and data
    mars_info = mongo.db.collection.find_one()
    print(mars_info)
    return render_template("index.html", mars=mars_info)


@app.route("/scrape")
def scrape():

    mars_data = scrape_mars.scrape()

    mongo.db.collection.update({}, mars_data, upsert=True)

    return redirect('/')


if __name__ == "__main__":
    app.run()
