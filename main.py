#!/usr/bin/env python3

from fabric import Connection


def main():
    print("hello world")

    URL = "web1.example.com"
    COMMAND = 'uname -s'
    SHOW_COMMAND = True

    result = Connection(URL).run(COMMAND, hide=SHOW_COMMAND)
    msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
    print(msg.format(result))


if __name__ == '__main__':
    main()
