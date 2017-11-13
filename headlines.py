import feedparser #jinja
from flask import Flask
from flask import render_template
from flask import request #Get request
"""Takes a Jinja template as input and produces pure HTML, capable of
being read by any browser, as the output
"""
app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}

@app.route("/")
def get_news(publication="bbc"):
    query = request.args.get("publication")
    """
    This is useful becase the GET arguments that our user passes along as
    part of a request are automatically available in request.args, from which
    we can access key-value. 
    """
    if not query or query.lower() not in RSS_FEEDS:
        publication = "bbc"
    else:
        publication = query.lower()

    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles=feed['entries'])

if __name__ == "__main__":
    #If our application is run directly kicks off development server on our local machine
    app.run(port=5000, debug=True)