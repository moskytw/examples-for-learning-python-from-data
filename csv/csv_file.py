#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

url = 'http://stats.moe.gov.tw/files/school/101/u1_new.csv'
save_path = 'school_list.csv'

with open(save_path, 'w') as f:
    f.write(requests.get(url).text.encode('utf-8'))

with open(save_path) as f:
    print f.read()

with open(save_path) as f:
    for line in f:
        print line,
