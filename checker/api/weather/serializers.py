import abc
from .exceptions import ValidationError


class Serializer(abc.ABC):
    def __init__(self, data):
        self._init_data = data

    def is_valid(self):
        raise NotImplementedError

    @property
    def data(self):
        raise NotImplementedError

    @property
    def errors(self):
        if not hasattr(self, '_errors'):
            msg = 'You must call `.is_valid()` before accessing `.errors`.'
            raise AssertionError(msg)
        return self._errors


class WeatherReportSerializer(Serializer):
    def is_valid(self):
        self._errors = []
        for report in self._init_data:
            if 'name' not in report:
                self._errors.append(f'Report item should have a name: {report}')
            if 'result' not in report:
                self._errors.append(f'Report item should provide a result set: {report}')
            elif 'passed' not in report['result']:
                self._errors.append(f'Report result should have a passed attribute: {report}')

        if self._errors:
            return False
        return True

    @property
    def data(self):
        if self.errors:
            raise ValidationError(self.errors)
        criteria = {item['name']: item['result']['passed'] for item in self._init_data}
        return {
            'check': all(criteria.values()),
            'criteria': criteria
        }
