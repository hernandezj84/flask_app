from datetime import date
from flask import Flask, jsonify, request, make_response

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route("/")
def index():
    """Returns index"""
    today = date.today().strftime("%d/%m/%Y")
    return make_response(jsonify({"message": "flask_app ready!", "datetime": today}))
