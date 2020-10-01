#!/usr/bin/python3
import os
import sys

TO_MONITOR = [
    ('network', 'MyGateway', '10.10.10.1')
]


def main():
    for (category, name, ip) in TO_MONITOR:
        is_online = os.system('ping -c 1 {} >/dev/null 2>&1'.format(ip))

        text = 'category={},item={} online={}'.format(
            category,
            name,
            1 if is_online == 0 else 0
        )

        print('reachables,{}'.format(text))


if __name__ == "__main__":
    sys.exit(main())
