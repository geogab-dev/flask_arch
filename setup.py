from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

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
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests"]),
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
