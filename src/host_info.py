from dataclasses import dataclass


@dataclass
class HostInfo:
    """ Class for detailing a host """
    host: str
    username: str
    password: str
