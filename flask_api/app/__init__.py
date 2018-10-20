from flask import Flask

app = Flask(__name__, static_folder='./templates', static_url_path='') # change static folder directory
app.config.from_object("config")

from app import views
