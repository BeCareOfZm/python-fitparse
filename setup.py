# -*- coding: utf-8 -*-

import re
import sys

from distutils.core import setup

requires = ['six']
if sys.version_info < (2, 7):
    requires.append('argparse')

with open('fitparse/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

setup(
    name='fitparse',
    version=version,
    description='Python library to parse ANT/Garmin .FIT files',
    author='David Cooper, Kévin Gomez',
    author_email='dave@kupesoft.com, contact@kevingomez.fr',
    url='https://github.com/K-Phoen/python-fitparse',
    license=open('LICENSE').read(),
    packages=['fitparse'],
    scripts=['scripts/fitdump'],  # Don't include generate_profile.py
    install_requires=requires,
)
