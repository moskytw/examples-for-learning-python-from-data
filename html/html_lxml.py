#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import etree

text = requests.get('http://clbc.tw').text

tree = etree.HTML(text)

print tree
