#!/usr/bin/env python

from distutils.core import setup

setup(name='python-zenoss',
    version="0.3",
    description='Zenoss API',
    author="Seth Miller",
    author_email='seth@migrantgeek.com',
    url='https://github.com/migrantgeek/python-zenoss',
    py_modules=['zenossapi',],
    scripts=['scripts/zenoss_add_device.py',],
    ext_modules = []
)
