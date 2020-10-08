from flask import Flask


def create_app(testing=False):
    """Application factory, used to create application"""

    app = Flask("checker")
    app.config.from_object("checker.config")

    if testing is True:
        app.config["TESTING"] = True

    return app
