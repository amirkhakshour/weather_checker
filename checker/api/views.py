from flask import Blueprint
from flask_restful import Api

from checker.api.weather import WeatherChecker

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)

api.add_resource(WeatherChecker, "/check/", endpoint="check-weather")
