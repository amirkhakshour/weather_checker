import unittest
from unittest import mock
from checker.api.weather.services import WeatherAPIConsumer
from checker.api.weather.exceptions import APIError

DUMMY_LOCATION_RESPONSE = {
    'id': 123456,
    'name': 'dummy_city',
    'main': {
        'temp': 0
    }
}
DUMMY_LOCATION_SERIALIZED = {
    'id': 123456,
    'name': 'dummy_city',
    'temperature': -273.15
}


class WeatherAPIConsumerTest(unittest.TestCase):
    def _mocked_requester(self):
        mocked_requester = mock.Mock(spec=WeatherAPIConsumer.requester)
        mocked_requester.get.return_value = DUMMY_LOCATION_RESPONSE, 200
        return mocked_requester

    def test_get_city_non_200_raise_api_error(self):
        city = 'dummy_city'
        mocked_requester = mock.Mock(spec=WeatherAPIConsumer.requester)
        mocked_requester.get.return_value = None, 400
        with mock.patch.object(WeatherAPIConsumer, 'requester', mocked_requester):
            with self.assertRaises(APIError):
                WeatherAPIConsumer.get(city)
                mocked_requester.get.assert_called_once_with(city=city)

    def test_get_city_200_returns_loaded_serializer(self):
        city = 'dummy_city'
        mocked_requester = self._mocked_requester()
        with mock.patch.object(WeatherAPIConsumer, 'requester', mocked_requester):
            location = WeatherAPIConsumer.get(city)
            self.assertEqual(location, DUMMY_LOCATION_SERIALIZED)
