name, version = 'ectoken', '0.1'

from distutils.core import setup, Extension
from distutils.sysconfig import get_python_lib

blowfish = Extension(
    name = '_ecblowfish',
    sources = ['blowfish.c'],
    libraries=['ssl'],
)

setup(
  name = name,
  version = version,
  py_modules=['ectoken'],
  ext_modules = [blowfish],
)
