from datetime import date
import feedparser
from flask import Flask, render_template
import os


app = Flask(__name__)


@app.route('/')
def index():
    Feed = feedparser.parse('http://www.reddit.com/r/python/.rss')
    for pointer in Feed.entries:
        feed_title = pointer.title
        feed_link = pointer.link
    user = os.getlogin()
    today = date.today().strftime('%B %d %Y')
    return render_template('index.html', user=user, today=today, feed_title=feed_title, feed_link=feed_link)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

