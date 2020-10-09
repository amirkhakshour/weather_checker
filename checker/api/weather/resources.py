from flask_restful import Resource, reqparse, abort
from .services import WeatherAPIConsumer, checker
from .exceptions import APIError
from .serializers import WeatherReportSerializer


class WeatherChecker(Resource):
    """Weather Checker endpoint"""
    serializer_class = WeatherReportSerializer

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
        serializer = self.serializer_class(report)
        if not serializer.is_valid():
            return abort(500, error=serializer.errors)
        return serializer.data
