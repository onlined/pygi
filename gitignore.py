from __future__ import print_function
from __future__ import unicode_literals

import argparse

try:
    from urllib.request import urlopen
except:
    from urllib import urlopen

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--list', help='List available gitignores', action='store_true')
group.add_argument('gitignores', help='gitignores to be included', nargs='*', default=[])

args = parser.parse_args()

def get_text_from_url(url):
    return urlopen(url).read().decode('UTF-8')

if args.list:
    print(get_text_from_url('https://www.gitignore.io/api/list?format=lines'), end='')
else:
    print('\n'.join(get_text_from_url('https://www.gitignore.io/api/{}'.format(','.join(args.gitignores))).split('\n')[2:]), end='')
