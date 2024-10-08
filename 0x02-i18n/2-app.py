#!/usr/bin/env python3
""" Back to flask """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Flask configuration class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config())
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Get best localized language """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def index():
    """ Index route """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(debug=True)
