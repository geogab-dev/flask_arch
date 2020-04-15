import os


_BASIC_APP = ["from flask import Flask\nfrom configmodule import DevelopmentConfig\n\n\napp = Flask(__name__)\n"
              "app.config.from_object(DevelopmentConfig())\n\n\n@app.route('/')\ndef hello():\n\treturn 'Hello Py!'\n"
              "\n\n@app.route('/<name>')\ndef hello_name(name):\n\treturn 'Hello {}!'.format(name)\n"]

_BASE_HTML = ['<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<link rel="stylesheet" href="#">\n\t<meta charset="UTF-8">'
              '\n\t<title>Untitled</title>\n</head>\n<body>\n\n\n</body>\n</html>']

_APP_CONFIG = ['class Config(object):\n\t"""Base config, uses staging database server."""\n\tDEBUG = False'
               '\n\tTESTING = False\n\tDB_SERVER = "192.168.0.1"\n\tSECRET_KEY = "your_secret_key_here"\n\n\t@property'
               '\n\tdef DATABASE_URI(self):       # Note: all caps\n\t\treturn "mysql://user@{}/foo".format(self.DB_SER'
               'VER)\n\n\nclass ProductionConfig(Config):\n\t"""Uses production database server."""\n\tDB_SERVER = '
               '"192.168.19.32"\n\n\nclass DevelopmentConfig(Config):\n\tDB_SERVER = "localhost"\n\tDEBUG = True'
               '\n\n\nclass TestingConfig(Config):\n\tDB_SERVER = "localhost"\n\tDEBUG = True\n\tDATABASE_URI = '
               '"sqlite:///:memory:"\n']

_APP_RUN = [f"from app import app\n\n\nif __name__ == '__main__':\n\tapp.run()\n"]


def _set_root_app():
    open('__init__.py', 'a')
    os.mkdir('app')
    open('app/__init__.py', 'a')
    with open('app/app.py', 'a') as arq:
        arq.writelines(_BASIC_APP)
    with open('run.py', 'a') as app_run:
        app_run.writelines(_APP_RUN)
    _make_config_module()


def _make_models_dir():
    os.mkdir('app/models')
    open(f'app/models/__init__.py', 'a')


def _make_view_dir():
    os.mkdir('app/views')
    open(f'app/views/__init__.py', 'a')


def _make_test_dir():
    os.mkdir('app/test')
    open(f'app/test/__init__.py', 'a')


def _make_utils_dir():
    os.mkdir('app/utils')
    open(f'app/utils/__init__.py', 'a')


def _make_services_dir():
    os.mkdir('app/services')
    open(f'app/services/__init__.py', 'a')


def _make_templates_dir():
    os.mkdir('app/templates')
    with open(f'app/templates/base.html', 'a') as arq:
        arq.writelines(_BASE_HTML)


def _make_config_module():
    with open('configmodule.py', 'a') as arq:
        arq.writelines(_APP_CONFIG)
