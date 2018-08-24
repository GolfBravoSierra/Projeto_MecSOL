# -*- coding: utf-8 -*-
# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='trusspy',
    version='SNAPSHOT-20180816',
    description='Truss Solver for Python',
    long_description=readme,
    author='Andreas Dutzler',
    author_email='a.dutzler@gmail.com',
    url='https://github.com/adtzlr/trusspy',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)