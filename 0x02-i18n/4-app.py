#!/usr/bin/env python3
""" Back to flask """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Flask configuration class """
    LANGUAGES: list = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app: Flask = Flask(__name__)
app.config.from_object(Config())
babel: Babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Get best localized language """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def index() -> str:
    """ Index route """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
