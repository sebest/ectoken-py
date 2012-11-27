name, version='ectoken', '0.2'

from setuptools import setup, Extension

blowfish=Extension(
    name='_ecblowfish',
    sources=['blowfish.c'],
    libraries=['crypto'],
)

setup(
    name=name,
    version=version,
    description='Python implementation of EdgeCast Token (ectoken_generate)',
    author="Sebastien Estienne",
    author_email="sebastien.estienned@gmail.com",
    url="https://github.com/sebest/ectoken-py",
    py_modules=['ectoken'],
    ext_modules=[blowfish],
    install_requires=['setuptools'],
)
