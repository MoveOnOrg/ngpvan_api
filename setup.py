#! /usr/bin/python
import os
from setuptools import setup, find_packages

setup(
    name='ngpvan_api',
    version='1.0.0',
    author='MoveOn.org',
    author_email='opensource@moveon.org',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/MoveOnOrg/ngpvan_api',
    license='BSD',
    description='Python wrapper for NGPVAN API.',
    classifiers=[
    ],
)
