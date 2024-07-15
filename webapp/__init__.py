from flask import Flask

app = Flask(__name__)

from webapp import connect

app.run(debug=True)
