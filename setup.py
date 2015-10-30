#!venv/bin/python
import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="torip",
    version="0.1.4",
    author="mendrugory",
    author_email="mendrugory@gmail.com",
    description="Library for Tornado web framework to locate IPs or server names.",
    license="MIT License",
    keywords="Tornado IP Locate",
    url="https://github.com/mendrugory/torip",
    packages=find_packages(),
    long_description=read('README.rst'),
    install_requires=[
        'tornado'
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers"
    ]
)
