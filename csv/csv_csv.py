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

    url = 'http://stats.moe.gov.tw/files/school/101/u1_new.csv'
    save_path = 'school_list.csv'

    if not exists(save_path):
        save(url, save_path)

    with open(save_path) as f:
        for row in csv.reader(f):
            print row
