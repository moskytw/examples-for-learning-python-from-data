#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import makedirs
from os.path import exists, join
from hashlib import md5

import requests
from lxml import etree

def get(url, cache_dir_path='cache/'):

    if not exists(cache_dir_path):
        makedirs(cache_dir_path)

    cache_path = join(cache_dir_path, md5(url).hexdigest())
    if exists(cache_path):
        with open(cache_path) as f:
            content = f.read().decode('utf-8')
        return content
    else:
        content = requests.get(url).content
        with open(cache_path, 'w') as f:
            f.write(content)
        return content

def find_urls(source_code):
    tree = etree.HTML(source_code)
    return [a.attrib['href'] for a in tree.xpath('//a') if 'href' in a.attrib]

if __name__ == '__main__':
    print find_urls(get('http://clbc.tw'))
