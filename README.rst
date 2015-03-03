===============================
Python implementation of EdgeCast Token
===============================

Python implementation of EdgeCast Token (ectoken_generate).

* Free software: BSD license

Usage
-----

```
import ectoken

key = 'XXXXXXXXXXXXXX'
url = 'http://my.edgesuite.net/path/to/my/file.txt'
print ectoken.ectoken_generate(key, url)
```
