name, version = 'ectoken', '0.1'

from distutils.core import setup, Extension
from distutils.sysconfig import get_python_lib

blowfish = Extension(
    name = '_ecblowfish',
    sources = ['blowfish.c'],
    libraries=['ssl'],
)

setup(
  name=name,
  version=version,
  description='Python implementation of EdgeCast Token (ectoken_generate)',
  author="Sebastien Estienne",
  author_email="sebastien.estienned@gmail.com",
  url="https://github.com/sebest/ectoken-py",
  py_modules=['ectoken'],
  ext_modules = [blowfish],
)
