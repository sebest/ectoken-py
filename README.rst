===============================
Python implementation of EdgeCast Token
===============================

.. image:: https://badge.fury.io/py/ectoken.png
    :target: http://badge.fury.io/py/ectoken
    
.. image:: https://travis-ci.org/sebest/ectoken.png?branch=master
        :target: https://travis-ci.org/sebest/ectoken

.. image:: https://pypip.in/d/ectoken/badge.png
        :target: https://crate.io/packages/ectoken?version=latest


Python implementation of EdgeCast Token (ectoken_generate).

* Free software: BSD license
* Documentation: http://ectoken.rtfd.org.

Usage
-----

import ectoken

key = 'XXXXXXXXXXXXXX'
url = 'http://my.edgesuite.net/path/to/my/file.txt'
print ectoken.ectoken_generate(key, url)
