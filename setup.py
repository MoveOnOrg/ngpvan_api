#! /usr/bin/python
import os
from setuptools import setup, find_packages

setup(
    name='ngpvan_api',
    version='0.1',
    author='MoveOn.org',
    author_email='tech@moveon.org',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/MoveOnOrg/ngpvan_api',
    license='BSD',
    description='Python wrapper for NGPVAN API.',
    classifiers=[
    ],
)
