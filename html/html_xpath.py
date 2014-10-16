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

tree = etree.HTML(content)

titles = tree.xpath('/html/head/title')
print titles[0].text

title_texts = tree.xpath('/html/head/title/text()')
print title_texts[0]

as_ = tree.xpath('//a')
print as_
print [a.get('href') for a in as_]
