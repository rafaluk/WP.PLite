from app import app
from flask import render_template, redirect, url_for, flash, session
import app.data.data_resolver as data

@app.route('/')
def nothing():
    return redirect(url_for('index'))


@app.route('/index', methods=['GET', 'POST'])
def index():
    links = data.wp()
    print(links)
    fiut = "dupszczi"
    return render_template('index.html', title='Start',
                           links=links)

