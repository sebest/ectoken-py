#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


from setuptools import setup, Extension

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

blowfish=Extension(
    name='ectoken/_ecblowfish',
    sources=['blowfish.c'],
    libraries=['crypto'],
)

setup(
    name='ectoken',
    version='0.3',
    description='Python implementation of EdgeCast Token (ectoken_generate).',
    long_description=readme + '\n\n' + history,
    author='Sébastien Estienne',
    author_email='sebastien.estienne@gmail.com',
    url='https://github.com/sebest/ectoken-py',
    packages=[
        'ectoken',
    ],
    package_dir={'ectoken': 'ectoken'},
    include_package_data=True,
    install_requires=[
    ],
    ext_modules=[blowfish],
    license="BSD",
    zip_safe=False,
    keywords='ectoken',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)
