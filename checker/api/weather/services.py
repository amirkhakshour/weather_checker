"""Weather checker registry."""


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
