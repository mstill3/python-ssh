#!/usr/bin/env python3

from utils import load_env, env
from fabric import Connection, Config


def main():
    load_env()
    host = env('HOST', default='127.0.0.1')
    user = env('USERNAME', default='pablo')
    password = env('PASSWORD', default='password')

    command = 'uname -s'
    show_command = True

    config = Config(overrides={'sudo': {'password': password}})

    conn = Connection(
        host=host,
        user=user,
        connect_kwargs={'password': password},
        config=config
    )

    result = conn.run(command, hide=show_command)
    print(result.stdout)

    # msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
    # print(msg.format(result))


if __name__ == '__main__':
    main()
