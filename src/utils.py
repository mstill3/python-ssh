import os
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
