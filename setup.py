import codecs
import os

from setuptools import setup, find_packages


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


PACKAGE = "flask_arch"
NAME = "flask_arch"
DESCRIPTION = "Gerador de templates para aplicações Flask"
AUTHOR = "George Gabriel"
AUTHOR_EMAIL = "geoquimics@gmail.com"
URL = "https://github.com/Geo-Gabriel/flask_arch"
VERSION = __import__(PACKAGE).__version__


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read("README.md"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests"]),
    zip_safe=False,
)
