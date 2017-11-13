import feedparser
from flask import Flask
#imports flask from package flask
app = Flask(__name__)
"""
Create a instance of the Flask object using our module name as parameter,
Flask use this to resolve resources, and in complex cases one can use other that __name__ here
"""
RSS_FEEDS = {
    'bbc':'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn':'http://rss.cnn.com/rss/edition.rss',
    'fox':'http://feeds.foxnews.com/foxnews/latest',
    'iol':'http://www.iol.co.za/cmlink/1.640'}

@app.route("/")

@app.route("/<publication>")
"""
Creates an argument called publication, which we need to add as a parameter of the function directly,
below the route
"""
def get_news(publication="cnn"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return """<html>
        <body>
            <h1>headlines</h1>
            <b>{0}</b> <br/>
            <i>{1}</i> <br/>
            <p>{2}</p> <br/>
        </body>
    </html>""".format(first_article.get("tittle"), first_article.get("published"), 
    first_article.get("summary"))
 
if __name__ == '__main__':
    #If our application is run directly kicks off development server on our local machine
    app.run(port=5000, debug=True)
