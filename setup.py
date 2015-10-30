#!venv/bin/python
import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="torip",
    version="0.0.1",
    author="mendrugory",
    author_email="mendrugory@gmail.com",
    description="Library for locating IP for Tornado Web Framework.",
    license="MIT License",
    keywords="Tornado IP Locate",
    url="",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 0.04 - Beta",
        "Topic :: Tornado IP Locate",
        "License :: MIT License",
    ],
)
