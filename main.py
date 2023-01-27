#!/usr/bin/env python3

import getpass
from fabric import Connection, Config


def main():
    url = '127.0.0.1'
    user = 'billy'
    command = 'uname -s'
    show_command = True

    password = getpass.getpass('Enter your root password: ')
    print(password)
    config = Config(overrides={'sudo': {'password': password}})
    conn = Connection(url, user=user, config=config)

    result = conn.run(command, hide=show_command)
    print(result.stdout)
    # msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
    # print(msg.format(result))


if __name__ == '__main__':
    main()
