#!/usr/bin/env python3
import datetime

from fabric import Connection, Config

from host_info import HostInfo
from utils import load_env, env, get_current_timestamp


def create_connection(host: HostInfo) -> Connection:
    """ Create SSH connection given host information """
    config = Config(
        overrides={
            'sudo': {
                'password': host.password
            }
        }
    )

    return Connection(
        host=host.hostname,
        user=host.username,
        connect_kwargs={'password': host.password},
        config=config
    )


def log(message: str, file_name: str = None):
    if not file_name:
        print(message)
    else:
        open(file_name, 'a+').write(message + "\n")


def execute_commands(connection: Connection, commands: [str], file_name: str = None):
    """ Executes bash commands via given SSH connection """
    for index, command in enumerate(commands):
        log("\n> " + command, file_name)
        if command.startswith('sudo '):
            result = connection.sudo(command.replace('sudo ', ''), hide=True)
            log(result.stdout, file_name)
        elif command.startswith('cd '):
            with connection.cd(command.replace('cd ', '')):
                execute_commands(connection, commands[index + 1:], file_name)
            break
        else:
            result = connection.run(command, hide=True)
            log(result.stdout, file_name)


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
            hostname=env('HOSTNAME', default='127.0.0.1'),
            username=env('USERNAME', default='pablo'),
            password=env('PASSWORD', default='password')
        )
    ]

    write_to_file: bool = True

    for host in hosts:
        connection = create_connection(host)
        commands = read_commands('res/input.sh')
        if write_to_file:
            execute_commands(
                connection,
                commands,
                file_name='res/output__' + host.hostname + '__' + get_current_timestamp() + '.log'
            )
        else:
            execute_commands(connection, commands)


if __name__ == '__main__':
    main()
