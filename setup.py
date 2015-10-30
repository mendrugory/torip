#!venv/bin/python
import os
from setuptools import setup, find_packages
import pypandoc


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="torip",
    version="0.1.3",
    author="mendrugory",
    author_email="mendrugory@gmail.com",
    description="Library for Tornado web framework to locate IPs or server names.",
    license="MIT License",
    keywords="Tornado IP Locate",
    url="https://github.com/mendrugory/torip",
    packages=find_packages(),
    long_description=pypandoc.convert('README.md', 'rst'),
    install_requires=[
        'tornado','pypandoc'
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers"
    ]
)
