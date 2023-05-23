# setup.py

from setuptools import setup, Extension

setup(
    hpy_ext_modules=[
        Extension('quickstart.hello', sources=['quickstart/hello.c']),
    ],
    setup_requires=['hpy'],
)
