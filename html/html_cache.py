#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import exists

import requests
from lxml import etree

cache_path = 'cache.html'

if exists(cache_path):
    with open(cache_path) as f:
        content = f.read().decode('utf-8')
else:
    content = requests.get('http://clbc.tw').content
    print type(content)
    with open(cache_path, 'w') as f:
        f.write(content)

root = etree.HTML(content)

print root
