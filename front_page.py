from datetime import date
from flask import Flask, render_template
import os


app = Flask(__name__)



@app.route('/')
def index():
    user = os.getlogin()
    today = date.today().strftime('%B %d %Y')
    return render_template('index.html', user=user, today=today)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
