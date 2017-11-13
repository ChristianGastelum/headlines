import feedparser
from flask import Flask
#imports flask from package flask
app = Flask(__name__)
"""
Create a instance of the Flask object using our module name as parameter,
Flask use this to resolve resources, and in complex cases one can use other that __name__ here
"""
BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

@app.route("/")

def get_news():
    feed = feedparser.parse(BBC_FEED)
    first_article = feed['entries'][0]
    return """<html>
        <body>
            <h1> BBC headlines</h1>
            <b>{0}</b> <br/>
            <i>{1}</i> <br/>
            <p>{2}</p> <br/>
        </body>
    </html>""".format(first_article.get("tittle"), first_article.get("published"), first_article.get("summary"))
    
if __name__ == '__main__':
    #If our application is run directly kicks off development server on our local machine
    app.run(port=5000, debug=True)