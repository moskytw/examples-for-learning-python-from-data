#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hashlib import md5

message = 'There should be one-- and preferably only one --obvious way to do it.'

print md5(message).hexdigest()

# Actually, it is noting about HTML.

