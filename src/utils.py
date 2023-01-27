import os
from datetime import datetime

from dotenv import load_dotenv


def load_env():
    """ Sources the local `.env` file """
    load_dotenv()


def env(key, default=''):
    """ Reads an environment variable or defaults """
    value = os.environ.get(key)
    if value is None:
        return default
    else:
        return value


def to_timestamp(dt_time: datetime) -> str:
    """ Convert a date time object into a clean string format """
    return str(dt_time.year).zfill(4) + '-' + \
        str(dt_time.month).zfill(2) + '-' + \
        str(dt_time.day).zfill(2) + '_' + \
        str(dt_time.hour).zfill(2) + '-' + \
        str(dt_time.minute).zfill(2) + '-' + \
        str(dt_time.second).zfill(2)


def get_current_timestamp() -> str:
    """ Returns the current date time as a formatted string """
    return str(to_timestamp(datetime.now()))
