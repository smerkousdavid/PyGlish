#!/usr/bin/env python

from distutils.core import setup

setup(name='Pyglish',
      version='0.2',
      description='Computer automatic topic writer',
      author='David Smerkous',
      author_email='smerkousdavid@gmail.com',
      url='https://github.com/smerkousdavid/PyGlish/',
      packages=['distutils', 'distutils.command'],
      requires=['bs4', 'nltk']
      )
