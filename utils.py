import os
from dotenv import load_dotenv


def load_env():
    load_dotenv()


def env(key, default):
    value = os.environ.get(key)
    if value is None:
        return default
    else:
        return value
