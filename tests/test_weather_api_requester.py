import unittest
from unittest import mock
from checker.api.weather.services import WeatherAPIRequester


class WeatherAPIRequesterTest(unittest.TestCase):
    def test_request_url_format(self):
        city = 'dummy_city'
        base_url = 'http://dummy.com?q1=x'
        get_city_format = WeatherAPIRequester._build_req_url(city, base_url)
        print(get_city_format)
        self.assertEqual(get_city_format, '%s%s' % (base_url, f'&q={city},de'))
