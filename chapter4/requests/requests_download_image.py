#!/usr/bin/python
# -*- coding: utf-8 -*-

import shutil
import requests

url = 'https://www.python.org/static/img/python-logo@2x.png'
response = requests.get(url, stream=True)
with open('python.png', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
