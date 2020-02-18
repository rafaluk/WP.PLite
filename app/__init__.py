from flask import Flask

app = Flask(__name__)




# this must be at the bottom
from app import routes
