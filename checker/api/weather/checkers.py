from datetime import datetime, time
from checker import config
from .services import checker, WeatherAPIConsumer


@checker.register(name='naming')
def check_name_len_is_odd(location):
    """len of name is odd or even"""
    if len(location['name']) % 2:
        return True, "Name len is Odd!"
    return False, "Name len is Even!"


@checker.register(name='daytemp')
def check_day_temp_is_normal(location):
    """Temperature is normal?"""
    now_time = datetime.utcnow().time()
    day = time(6, 0) <= now_time <= time(18, 0)
    temp = location['temperature']
    if (day and 17 < temp < 25) or (not day and 10 < temp < 15):
        return True, f"It's {'day' if day else 'night'} and temperature is normal!"
    return False, "Name len is Even!"


@checker.register(name='rival')
def check_rival_comparison(location):
    """Is it warmer than it's rival?"""
    rival_city = WeatherAPIConsumer.get(config.WEATHER_RIVAL_CITY_NAME)
    temp_difference = round(location['temperature'] - rival_city['temperature'], 2)
    if temp_difference > 0:
        return True, f"It's {temp_difference}°C " \
                     f"warmer than it's rival city {rival_city['name']}"
    return False, f"It's {temp_difference}°C " \
                  f"colder than it's rival city {rival_city['name']}"
