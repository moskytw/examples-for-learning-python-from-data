#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import etree

content = requests.get('http://clbc.tw').content

root = etree.HTML(content)

print root
