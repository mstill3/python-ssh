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


def execute_commands(connection: Connection, commands: [str]):
    """ Executes bash commands via given SSH connection """
    for index, command in enumerate(commands):
        print("\n> " + command)
        if command.startswith('sudo '):
            result = connection.sudo(command.replace('sudo ', ''), hide=True)
            print(result.stdout)
        elif command.startswith('cd '):
            with connection.cd(command.replace('cd ', '')):
                execute_commands(connection, commands[index + 1:])
            break
        else:
            result = connection.run(command, hide=True)
            print(result.stdout)


def read_commands(file_name: str):
    """ Form bash commands list from input file """
    # read bash file lines
    commands = open(file_name).read().splitlines()
    # remove leading & trailing spaces on each line
    commands = list(map(lambda cmd: cmd.lstrip().rstrip(), commands))
    # remove commented out lines
    commands = list(filter(lambda cmd: not cmd.startswith('#'), commands))
    # remove blank lines
    commands = list(filter(lambda cmd: not len(cmd) == 0, commands))
    return commands


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
        commands = read_commands('res/input.sh')
        execute_commands(connection, commands)


if __name__ == '__main__':
    main()
