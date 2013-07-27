#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import makedirs
from os.path import exists, join
from hashlib import md5

import requests
from lxml import etree

def get(url, cache_dir='cache/'):

    if not exists(cache_dir):
        makedirs(cache_dir)

    cache_path = join(cache_dir, md5(url).hexdigest())
    if exists(cache_path):
        with open(cache_path) as f:
            text = f.read().decode('utf-8')
        return text
    else:
        text = requests.get(url).text
        with open(cache_path, 'w') as f:
            f.write(text.encode('utf-8'))
        return text

def find_urls(source_code):
    tree = etree.HTML(source_code)
    return [a.attrib['href'] for a in tree.xpath('//a') if 'href' in a.attrib]

if __name__ == '__main__':
    print find_urls(get('http://clbc.tw'))
