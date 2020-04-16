import os
import time

_OK_GREEN = '\033[32mOK\033[0m'

_ERROR_RED = '\033[31mERROR\033[0m'

_WARNING_YELLOW = '\033[93mWARNING\033[0m'

_BASIC_APP: list = [
        "from flask import Flask\nfrom configmodule import DevelopmentConfig\n\n\napp = Flask(__name__)\n"
        "app.config.from_object(DevelopmentConfig())\n\n\n@app.route('/')\ndef hello():\n\treturn 'Hello Py!'\n"
        "\n\n@app.route('/<name>')\ndef hello_name(name):\n\treturn 'Hello {}!'.format(name)\n"
]

_BASE_HTML: list = [
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<link rel="stylesheet" href="#">\n\t<meta charset="UTF-8">'
        '\n\t<title>Untitled</title>\n</head>\n<body>\n\n\n</body>\n</html>'
]

_APP_CONFIG: list = [
        'class Config(object):\n\t"""Base config, uses staging database server."""\n\tDEBUG = False'
        '\n\tTESTING = False\n\tDB_SERVER = "192.168.0.1"\n\tSECRET_KEY = "your_secret_key_here"\n\n\t@property'
        '\n\tdef DATABASE_URI(self):       # Note: all caps\n\t\treturn "mysql://user@{}/foo".format(self.DB_SER'
        'VER)\n\n\nclass ProductionConfig(Config):\n\t"""Uses production database server."""\n\tDB_SERVER = '
        '"192.168.19.32"\n\n\nclass DevelopmentConfig(Config):\n\tDB_SERVER = "localhost"\n\tDEBUG = True'
        '\n\n\nclass TestingConfig(Config):\n\tDB_SERVER = "localhost"\n\tDEBUG = True\n\tDATABASE_URI = '
        '"sqlite:///:memory:"\n'
]

_APP_RUN: list = [
    f"from app import app\n\n\nif __name__ == '__main__':\n\tapp.run()\n"
]

_TEST_EXAMPLE = [f"import unittest\n\n\nclass TestExample(unittest.TestCase):\n\n\tdef test_example_1(self):\n\t\t"
                 f"self.assertEqual(10, 10)\n\n\tdef test_example_2(self):\n\t\tself.assertNotEqual(10, 20)\n"
                 ]


def _set_root_app() -> None:
    _make__init__module()
    _make_dir()
    _make__init__module(dir_name='app/')
    time.sleep(0.1)


def _make_layer_models_dir() -> None:
    _make_dir('/models')
    _make__init__module('app/models/')
    time.sleep(0.1)


def _make_layer_controller_dir() -> None:
    _make_dir('/controllers')
    _make__init__module('app/controllers/')
    time.sleep(0.1)


def _make_layer_view_dir(is_mvc_arch: bool = False) -> None:
    _make_dir('/views')
    _make__init__module('app/views/')
    if is_mvc_arch:
        _make_dir('/views/templates')
    time.sleep(0.1)


def _make_layer_test_dir() -> None:
    _make_dir('/tests')
    _make__init__module('app/tests/')
    time.sleep(0.1)


def _make_layer_utils_dir() -> None:
    _make_dir('/utils')
    _make__init__module('app/utils/')
    time.sleep(0.1)


def _make_layer_services_dir() -> None:
    _make_dir('/services')
    _make__init__module('app/services/')
    time.sleep(0.1)


def _make_layer_templates_dir() -> None:
    _make_dir('/templates')
    time.sleep(0.1)


def _write_basics_config(is_mvc_arch: bool = False) -> None:
    _make_and_write_files_config(file_name='run.py', list_config=_APP_RUN)
    _make_and_write_files_config(file_name='configmodule.py', list_config=_APP_CONFIG)
    _make_and_write_files_config(dir_name='app/', file_name='app.py', list_config=_BASIC_APP)
    if not is_mvc_arch:
        _make_and_write_files_config(dir_name='app/templates/', file_name='base.html', list_config=_BASE_HTML)
    else:
        _make_and_write_files_config(dir_name='app/views/templates/', file_name='base.html', list_config=_BASE_HTML)
    _make_and_write_files_config(dir_name='app/tests/', file_name='test_example.py', list_config=_TEST_EXAMPLE)


def _make__init__module(dir_name: str = str()) -> None:
    try:
        open('{}__init__.py'.format(dir_name), 'x')
        print('[ {} ] file {}__init__.py created.'.format(_OK_GREEN,
                                                          dir_name if dir_name else os.getcwd().split('/')[-1] + '/'))
        time.sleep(0.1)
    except FileExistsError or FileNotFoundError:
        print('[ {} ] file {}__init__.py already exists, not created.'.format(_ERROR_RED, dir_name))
        time.sleep(0.1)


def _make_dir(dir_name: str = str()) -> None:
    try:
        os.mkdir('app{}'.format(dir_name))
        print('[ {} ] Directory app{} created.'.format(_OK_GREEN, dir_name))
        time.sleep(0.1)
    except FileExistsError or FileNotFoundError:
        print('[ {} ] Directory app{} already exists, not created.'.format(_ERROR_RED, dir_name))
        time.sleep(0.1)


def _make_and_write_files_config(list_config: list, dir_name: str = str(), file_name: str = str()) -> None:
    try:
        with open('{}{}'.format(dir_name, file_name), 'x') as file_config:
            file_config.writelines(list_config)
        print('[ {} ] File {}{} created.'.format(_OK_GREEN, dir_name, file_name))
        time.sleep(0.1)
    except FileExistsError or FileNotFoundError:
        print('[ {} ] File already exists {}{}, not created.'.format(_ERROR_RED, dir_name, file_name))
        time.sleep(0.1)
