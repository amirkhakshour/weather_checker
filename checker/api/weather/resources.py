from flask_restful import Resource, reqparse, abort
from .services import WeatherAPIConsumer, checker
from .exceptions import APIError


class WeatherChecker(Resource):
    """Weather Checker endpoint"""

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('city')
        args = parser.parse_args()
        city = args.get('city')
        if city is None:
            return abort(400, error="`city` name must be set via query param!")
        try:
            location = WeatherAPIConsumer.get(city)
        except APIError as e:
            return abort(400, error=e.message)
        report = checker.check(location)
        return report
