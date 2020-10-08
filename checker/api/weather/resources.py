from flask_restful import Resource, reqparse, abort


class WeatherChecker(Resource):
    """Weather Checker endpoint"""

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('city')
        args = parser.parse_args()
        city = args.get('city')
        if city is None:
            return abort(400, error="`city` name must be set via query param!")
