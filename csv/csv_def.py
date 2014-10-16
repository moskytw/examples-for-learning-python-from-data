#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import basename
import requests

def save(url, path=None):

    if not path:
        path = basename(url)

    with open(path, 'w') as f:
         f.write(requests.get(url).content)

if __name__ == '__main__':

    from os.path import exists

    #url = 'http://stats.moe.gov.tw/files/school/101/u1_new.csv'
    url = 'https://raw.github.com/moskytw/learning-python-from-data-examples/master/sql/schools.csv'
    save_path = 'school_list.csv'

    if not exists(save_path):
        save(url, save_path)
        print "Saved into '%s'." % save_path
    else:
        print "'%s' is existent." % save_path

