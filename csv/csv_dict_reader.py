#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
from os.path import basename
import requests
import uniout # You want this!

def save(url, path=None):

    if not path:
        path = basename(url)

    with open(path, 'w') as f:
         f.write(requests.get(url).text.encode('utf-8'))

if __name__ == '__main__':

    from os.path import exists

    #url = 'http://stats.moe.gov.tw/files/school/101/u1_new.csv'
    url = 'https://raw.github.com/moskytw/learning-python-from-data-examples/master/sql/schools.csv'
    save_path = 'school_list.csv'

    if not exists(save_path):
        save(url, save_path)

    with open(save_path) as f:
        next(f) # a useful technique
        next(f)
        for row in csv.DictReader(f):
            print row
