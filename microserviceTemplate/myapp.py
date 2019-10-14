# Flask main application

from flask import *
app = Flask(__name__)
app.config.from_pyfile('config.py')
from views import *


if __name__ == '__main__':
    app.run()