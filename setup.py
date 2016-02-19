#!/usr/bin/env python

from distutils.core import setup

print "Welcome to the Pyglish cross-installer"

files = ["docs/*"]

setup(name='Pyglish',
      version='0.2',
      description='Computer automatic topic writer',
      author='David Smerkous',
      author_email='smerkousdavid@gmail.com',
      url='https://github.com/smerkousdavid/PyGlish/',
      packages=['Pyglish'],
      package_data={'Pyglish': files},
      scripts=['pyglish'],
      long_description="""
        Pyglish was an idea so that I wouldn't ever try to write an english essay again...
        Hopefully my english teacher will accept it because either way the underlying core to this writing, would
        be similar to what would be applied to the essay...
      """,
      requires=['bs4', 'nltk']
      )

print "done done done"
print "test"
