import unittest
from checker.app import create_app
from checker.api.weather.services import WeatherCheckService


class DefaultWeatherCheckTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.path = "/api/v1/checker"  # @todo get from settings
        self.client = self.app.test_client()
        self.checker = WeatherCheckService()

    def test_checker_registry(self):
        @self.checker.register()
        def test_ok():
            return True, "OK"

        self.assertTrue(len(self.checker._registry.keys()) == 1)
        self.assertTrue(test_ok.__name__ in self.checker._registry)
        self.assertTrue(self.checker._registry[test_ok.__name__] == test_ok)
