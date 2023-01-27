#!/usr/bin/env python3

from fabric import Connection, Config

from host_info import HostInfo
from utils import load_env, env


def create_connection(host_info: HostInfo) -> Connection:
    """ Create SSH connection given host information """
    config = Config(
        overrides={
            'sudo': {
                'password': host_info.password
            }
        }
    )

    return Connection(
        host=host_info.host,
        user=host_info.username,
        connect_kwargs={'password': host_info.password},
        config=config
    )


def run_commands(connection: Connection):
    """ Run bash commands via given SSH connection """
    commands = [
        'uname -s',
        'ls',
        'pwd'
    ]
    show_command = True

    for command in commands:
        result = connection.run(command, hide=show_command)
        print(result.stdout)


def main():
    """ Logic to create SSH connections to hosts & issue bash commands """
    load_env()

    hosts = [
        HostInfo(
            host=env('HOST', default='127.0.0.1'),
            username=env('USERNAME', default='pablo'),
            password=env('PASSWORD', default='password')
        )
    ]

    for host in hosts:
        connection = create_connection(host)
        run_commands(connection)


if __name__ == '__main__':
    main()
