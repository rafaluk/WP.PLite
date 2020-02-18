from app import app
from flask import render_template, redirect, url_for, flash, session
import app.data.data_resolver as data
from flask import request


@app.route('/')
def nothing():
    return redirect(url_for('index'))


@app.route('/index', methods=['GET', 'POST'])
def index():
    links = data.wp()
    # print(links)

    return render_template('index.html', title='Start',
                           links=links)


@app.route('/art', methods=['GET', 'POST'])
def art():
    link = request.args.get('link')
    print(link)
    

    return render_template('art.html', link=link)
