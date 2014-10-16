#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
from os.path import basename
import requests
import uniout

def save(url, path=None):

    if not path:
        path = basename(url)

    with open(path, 'w') as f:
         f.write(requests.get(url).content)

def parse_to_school_list(path):

    with open(path) as f:
        next(f)
        next(f)
        school_list = [school for school in csv.DictReader(f)][:-2]

    return school_list

if __name__ == '__main__':

    from os.path import exists

    save_path = 'school_list.csv'

    if not exists(save_path):
        save(url, save_path)

    school_list = parse_to_school_list(save_path)

    # Pythonic way!
    print [school['學校名稱'] for school in school_list]
