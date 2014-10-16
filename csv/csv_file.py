#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

#url = 'http://stats.moe.gov.tw/files/school/101/u1_new.csv'
url = 'https://raw.github.com/moskytw/learning-python-from-data-examples/master/sql/schools.csv'
save_path = 'school_list.csv'

with open(save_path, 'w') as f:
    f.write(requests.get(url).content)

with open(save_path) as f:
    print f.read()

with open(save_path) as f:
    for line in f:
        print line,
