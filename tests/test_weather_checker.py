import unittest
from checker.app import create_app


class DefaultWeatherCheckTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.path = "/api/v1/checker"  # @todo get from settings
        self.client = self.app.test_client()
