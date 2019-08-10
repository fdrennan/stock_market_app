from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/stats/<stat>')
def stats(stat):
    df = pd.read_csv('constituents-financials_csv.csv')
    return render_template('stats.html',
                           **locals())


@app.route('/about/')
def about():
    return "About content goes here!"

if __name__ =="__main__":
    app.run(debug = True)
