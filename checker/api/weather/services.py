"""Weather checker registry."""
import requests
from checker import config
from .models import LocationWeather
from .exceptions import APIError


class WeatherAPIRequester:
    @classmethod
    def _build_req_url(cls, city, base_url=config.WEATHER_API_URL):
        return '%s&%s' % (base_url, f'&q={city},de')

    @classmethod
    def get(cls, city):
        # @todo add custom retry strategies on fail cases.
        session = requests.Session()
        result = session.request('get', cls._build_req_url(city))
        return result.json(), result.status_code


class WeatherAPIConsumer:
    requester = WeatherAPIRequester
    model = LocationWeather

    @classmethod
    def construct_from(cls, data):
        return cls.model().load_from_data(data)

    @classmethod
    def get(cls, city):
        city_json, status_code = cls.requester.get(city)
        if status_code != 200:
            raise APIError(message=f"City `{city}` doesnt exists!", http_status=status_code)
        return cls.construct_from(city_json)


class WeatherCheckService:
    def __init__(self):
        self._registry = dict()

    def register(self):
        """
        Register a checker service.

        @todo add priority as parameter to call checkers by order.
        :return:
        """

        def wrapper(checker_service):
            self._registry[checker_service.__name__] = checker_service
            return checker_service

        return wrapper


# default health checker service
checker = WeatherCheckService()
