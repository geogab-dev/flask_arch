# flask_arch

Template generator for Flask applications.


## Pre-requisites

[Python 3.7+](https://www.python.org/)

## Installing via setup.py

Clone this repository inside a local folder and run the following commands on a terminal:
```
$ cd [LOCAL REPOSITORY PATH]
$ python setup.py install
```

## Installing via package building

### Build package and generate distro file
```
$ python setup.py sdist --formats=gztar,zip
```

### You should see something like this:
```
├─ flask_arch
│  └─ dist
│     ├─ flask_arch-1.0.tar.gz
│     └─ flask_arch-1.0.tar.zip
├─ flask_arch
│  └─ ...
├─ flask_arch.egg-info
│  └─ ...
└─ setup.py
└─ ...
```

[comment]: <> (For the author: please upload this project to https://pypi.org, much easier!)

### Installing the package _flask_arch-1.0.tar.zip_
```
$ pip install flask_arch-1.0.tar.zip
```

## Running tests
```
$ python run --tests flask_arch
```

### Generating an app template
 - Create a folder for your application.
 - Open a terminal (powershell, cmd, bash, etc) inside the folder and run the following command:
```
$ python -m flask_arch init
```

## With love ❤️

* [Python](https://www.python.org) 🐍

## Author

[George Gabriel](https://github.com/Geo-Gabriel) - *Initial Work* 

[Douglas Silva](https://github.com/douugbr) - *Contributor* 

See the [contributors](https://github.com/Geo-Gabriel/flask_arch/graphs/contributors).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
