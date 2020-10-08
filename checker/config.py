"""Default configuration

Use env var to override
"""
import os
import distutils.util
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
READ_DOT_ENV_FILE = distutils.util.strtobool(os.getenv("READ_DOT_ENV_FILE", default="False"))
if READ_DOT_ENV_FILE:
    from dotenv import load_dotenv  # NOQA

    load_dotenv()
    env_path = BASE_DIR / '.env'
    load_dotenv(dotenv_path=env_path)

# Base config
# ------------------------
ENV = os.getenv("FLASK_ENV")
DEBUG = ENV == "development"
SECRET_KEY = os.getenv("SECRET_KEY")

# Checker config
# ------------------------
WEATHER_API_KEY = '8ca1bf554fe26dff41d635d4e2f866ed'
WEATHER_API_URL = f'http://api.openweathermap.org/data/2.5/weather?appid={WEATHER_API_KEY}'
