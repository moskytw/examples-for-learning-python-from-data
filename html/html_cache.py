#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import exists

import requests
from lxml import etree

cache_path = 'cache.html'

if exists(cache_path):
    with open(cache_path) as f:
        text = f.read().decode('utf-8')
else:
    text = requests.get('http://clbc.tw').text
    print type(text)
    with open(cache_path, 'w') as f:
        f.write(text.encode('utf-8'))

tree = etree.HTML(text)

print tree
