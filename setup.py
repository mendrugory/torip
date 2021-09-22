#!venv/bin/python
from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="torip",
    version="RELEASE_VERSION",
    author="Gonzalo Gabriel Jiménez Fuentes",
    author_email="iam@mendrugory.com",
    description="Library for Tornado web framework to locate IPs or server names.",
    license="MIT License",
    keywords="Tornado IP Locate",
    url="https://github.com/mendrugory/torip",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
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
