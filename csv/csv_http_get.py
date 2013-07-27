#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

url = 'http://stats.moe.gov.tw/files/school/101/u1_new.csv'

print requests.get(url).text
