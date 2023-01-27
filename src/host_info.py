from dataclasses import dataclass


@dataclass
class HostInfo:
    """ Class for detailing a host """
    hostname: str
    username: str
    password: str
