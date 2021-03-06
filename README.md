# WP.PLite
If you are familiar with polish mass-info portals, the purpose of this project is self-explanatory.

Portals like:
* wp.pl
* onet.pl
* interia.pl
* o2.pl
* se.pl
(and many more)

are the most annoying websites in the Internet. The ads are everywhere, there's no content anchoring, so everythings jumps up and down, some huge, overlaying banners appear, everything is so unreadable... even adblock softwares can't sometimes manage! And not everyone know how to/wants to/can use adblock... however, although the form is awful, the content of the articles might be interesting and good to read.

And this is WP.PLite: **wp.pl content extractor**.

## Backend
The project has a form of a webapp, which has been developed only for my own porpuses :) Therefore it's hosted locally and hasn't been tested or adapted for hosting anywhere else.

The web server and routing logic have been implemented using `Flask` framework.

The links to articles and articles themselves have been extracted from HTML code (which had been previously obtained with `requests` library) using `BeautifulSoup4`.

Simplified HLD looks as follows:
![](wpplite.png)

## Running the project
After cloning all files and installing required dependencies (see: `requirements.txt`), navigate to the repo using command line and set the flask app variable:
* Windows:
```
set FLASK_APP=webapp.py
```

* Linux:
```
export FLASK_APP=webapp.py
```

and run the app:
* Windows/Linux:
```
flask run
```

## Exclusions
Some of linked portals are too hard to scrape. Since there are so many articles on wp.pl I wasn't trying to get every possible article and some websites have been excluded (they are not displayed on the list).
