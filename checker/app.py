from flask import Flask
from checker import api


def create_app(testing=False):
    """Application factory, used to create application"""

    app = Flask("checker")
    app.config.from_object("checker.config")

    if testing is True:
        app.config["TESTING"] = True

    register_blueprints(app)
    fill_registry(app)

    return app


def register_blueprints(app):
    """register all blueprints for application
    """
    app.register_blueprint(api.views.blueprint)


def fill_registry(app):
    """Fill registry by importing relevant files at startup!"""
    from checker.api.weather import checkers
