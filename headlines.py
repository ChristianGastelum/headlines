import feedparser #jinja
from flask import Flask
from flask import render_template
"""Takes a Jinja template as input and produces pure HTML, capable of
being read by any browser, as the output
"""
app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}

@app.route("/")
@app.route("/<publication>")
#Creates an argument called publication, which we need to add as a parameter 
#of the function directly, below the route
def get_news(publication="bbc"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles=feed['entries'])

if __name__ == "__main__":
    #If our application is run directly kicks off development server on our local machine
    app.run(port=5000, debug=True)