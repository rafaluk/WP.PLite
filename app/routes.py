from app import app
from flask import render_template, redirect, url_for, flash, session
import app.data.data_resolver as data
from flask import request
from app.data.text_extractor import AbcZdrowieExtractor, \
    ParentingExtractor, WiadomosciExtractor, TurystykaExtractor, \
    KobietaExtractor


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
    #todo: delete "zobacz też:", "przeczytaj też:" paragrahps, "dziejesie.wp.pl"
    if 'abczdrowie' in link:
        extr = AbcZdrowieExtractor(link)
        # art = extr.get_article()
        # title = extr.get_title()
    elif 'parenting.pl' in link:
        extr = ParentingExtractor(link)
        # art = extr.get_article()
        title = extr.get_title()
    elif 'wiadomosci.wp.pl/' in link:
        extr = WiadomosciExtractor(link)
        # EXCLUDE SPORTOWE FAKTY
    elif 'turystyka.wp.pl' in link:
        extr = TurystykaExtractor(link)
    elif 'kobieta.wp.pl' in link:
        extr = KobietaExtractor(link)
    art = extr.get_article()
    title = extr.get_title()

    return render_template('art.html', link=link, art=art, title=title)

