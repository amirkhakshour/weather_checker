from marshmallow import Schema, fields, EXCLUDE


class ModelMixin:
    @classmethod
    def load_from_data(cls, data):
        return cls().load(data, unknown=EXCLUDE)


class LocationWeather(ModelMixin, Schema):
    id = fields.Integer()
    name = fields.String()
    temperature = fields.Method(data_key="main", deserialize="load_temperature")

    def load_temperature(self, temp_details):
        """Load and convert temperature from kelvin to Celsius!"""
        return round(float(temp_details['temp']) - 273.15, 2)
