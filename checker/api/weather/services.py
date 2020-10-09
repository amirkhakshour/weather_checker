"""Weather checker registry."""
import requests
from checker import config


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
