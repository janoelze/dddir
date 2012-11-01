#!/usr/bin/python
from setuptools import setup, find_packages

setup(
    name='dddir',
    version='0.1',
    description='dddir - creates directories from a blueprint',
    author='Jan Oelze',
    author_email='hallo@janoelze.de',
    packages=['dddir'],
    entry_points={
        'console_scripts': [
            'dddir = dddir.__init__:main'
        ],
    },
)
