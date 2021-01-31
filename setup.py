import codecs
import os

from setuptools import setup, find_packages


def read(file_name):
    return codecs.open(os.path.join(os.path.dirname(__file__), file_name)).read()


PACKAGE = "flask_arch"
NAME = "flask_arch"
DESCRIPTION = "Template generator for Flask applications."
AUTHOR = "George Gabriel"
AUTHOR_EMAIL = "geogab.dev@gmail.com"
URL = "https://github.com/Geo-Gabriel/flask_arch"
VERSION = __import__(PACKAGE).__version__


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read("README.txt"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests"]),
    zip_safe=False,
)
