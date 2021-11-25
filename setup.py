#!/usr/bin/env python3

from distutils.core import setup

setup(
    name='bisect',
    version='0.1.0',
    description='CLI tool to bisect a range of numbers',
    author='Markus Grunwald',
    author_email='bisect.thegrue@spamgourmet.com',
    packages=['bisect'],
    scripts=['bisect.py'],
)
