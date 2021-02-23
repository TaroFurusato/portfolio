from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.config.from_object('portfolio.config') 
db = SQLAlchemy(app)

import portfolio.views