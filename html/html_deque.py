#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import makedirs
from os.path import exists, join
from hashlib import md5
from collections import deque

from lxml import etree
import requests

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

NEW     = 0
QUEUED  = 1
VISITED = 2

def search_urls(url):

    url_queue = deque([url])
    url_state_map = {url: QUEUED}

    while url_queue:

        url = url_queue.popleft()
        print url

        try:
            found_url_list = find_urls(get(url))
        except Exception, e:
            url_state_map[url] = e
            print 'Exception: %s' % e
        except KeyboardInterrupt, e:
            return url_state_map
        else:
            for found_url in found_url_list:
                if not url_state_map.get(found_url, NEW):
                    url_queue.append(found_url)
                    url_state_map[found_url] = QUEUED
            url_state_map[url] = VISITED

if __name__ == '__main__':
    print search_urls('http://clbc.tw')
