#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''It contains some userful function for parsing data from government.'''

import csv
from os.path import basename
import requests
import uniout

def save(url, path=None):
    '''It saves data from `url` into `path`.'''

    if not path:
        path = basename(url)

    with open(path, 'w') as f:
         f.write(requests.get(url).text.encode('utf-8'))

def parse_to_school_list(path):
    '''It parses `path` in schools csv format.'''

    with open(path) as f:
        next(f)
        next(f)
        school_list = [school for school in csv.DictReader(f)][:-2]

    return school_list

if __name__ == '__main__':

    import clime.now
