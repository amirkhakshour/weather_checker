import unittest
from unittest import mock
from checker.app import create_app
from checker.api.weather.services import WeatherCheckService
from checker.api.weather.models import LocationWeather


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

    def test_check_runs_checkers(self):
        test_ok = mock.Mock(return_value=(True, "OK"))
        location = LocationWeather()
        self.checker.register('test_ok')(test_ok)
        results = self.checker.check(location=location)
        test_ok.assert_called_once_with(location=location)
        assert len(results) == 1
        assert 'name' in results[0]
        assert 'result' in results[0]

    def test_run_checker_output_format(self):
        test_ok = mock.Mock(return_value=(True, "OK"))
        location = LocationWeather()
        result = self.checker.run_checker(checker=test_ok, location=location)
        self.assertEqual(list(result.keys()), ['info', 'output', 'passed', 'timestamp'])
