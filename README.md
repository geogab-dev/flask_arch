# flask_arch

Template generator for Flask applications.


### Pré-requisites

[Python 3.7+](https://www.python.org/)

### Build package and generate distro file
```
python setup.py sdist --formats=gztar,zip
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

### Installing the package _flask_arch-1.0.tar.zip_
```
pip install flask_arch-1.0.tar.zip
```

### Running tests
```
python run --tests flask_arch
```

### Generating an app template
 - Create a folder for your application.
 - Open a terminal (Power Shell) and follow the commands:
```
C:\Users\your_user\your_app_folder> python

>>> from flask_arch.gen_arch import generate_flask_arch

generate_flask_arch()
```

## With love ❤️

* [Python](https://www.python.org) 🐍

## Autor

[George Gabriel](https://github.com/Geo-Gabriel) - *Initial Work* 

See the [contributors](https://github.com/Geo-Gabriel/flask_arch/graphs/contributors).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
