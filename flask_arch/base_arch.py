import os


_flags_dict = {'flag_ok': '[\033[32m OK \033[0m]',
               'flag_error': '[\033[31m ERROR \033[0m]',
               'flag_warning': '[\033[93m WARNING \033[0m]',
               'flag_file': lambda file: f"\033[32m{file}\033[0m"}

_files_dict = {
    'app.py': [
        "from flask import Flask\nfrom configmodule import DevelopmentConfig\n\n\napp = Flask(__name__)\n"
        "app.config.from_object(DevelopmentConfig())\n\n\n@app.route('/')\ndef hello():\n\treturn 'Hello Py!'\n"
        "\n\n@app.route('/<name>')\ndef hello_name(name):\n\treturn 'Hello {}!'.format(name)\n"
    ],
    'template.html': [
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<link rel="stylesheet" href="#">\n\t<meta charset="UTF-8">'
        '\n\t<title>Untitled</title>\n</head>\n<body>\n\n\n</body>\n</html>'
    ],
    'config.py': [
        'class Config(object):\n\t"""Base config, uses staging database server."""\n\tDEBUG = False'
        '\n\tTESTING = False\n\tDB_SERVER = "192.168.0.1"\n\tSECRET_KEY = "your_secret_key_here"\n\n\t@property'
        '\n\tdef DATABASE_URI(self):       # Note: all caps\n\t\treturn "mysql://user@{}/foo".format(self.DB_SER'
        'VER)\n\n\nclass ProductionConfig(Config):\n\t"""Uses production database server."""\n\tDB_SERVER = '
        '"192.168.19.32"\n\n\nclass DevelopmentConfig(Config):\n\tDB_SERVER = "localhost"\n\tDEBUG = True'
        '\n\n\nclass TestingConfig(Config):\n\tDB_SERVER = "localhost"\n\tDEBUG = True\n\tDATABASE_URI = '
        '"sqlite:///:memory:"\n'
    ],
    'run.py': [
        f"from app import app\n\n\nif __name__ == '__main__':\n\tapp.run()\n"
    ],
    'test.py': [
        f"import unittest\n\n\nclass TestExample(unittest.TestCase):\n\n\tdef test_example_1(self):\n\t\t"
        f"self.assertEqual(10, 10)\n\n\tdef test_example_2(self):\n\t\tself.assertNotEqual(10, 20)\n"
    ]
}

_app_dirs = ('models', 'controllers', 'views', 'tests',
            'utils', 'services', 'templates')

_app_files = {
    'run.py': os.getcwd(),
    'config.py': os.getcwd(),
    'app.py': os.getcwd() + "\\" + 'app',
    'template.html': os.getcwd() + "\\" + 'app\\templates',
    'test.py': os.getcwd() + "\\" + 'app\\tests'
}


def _create_dir(directory_name: str) -> None:
    try:
        os.makedirs(directory_name)
        open(file=f'{directory_name}/__init__.py', mode='x')
        print(f'{_flags_dict["flag_ok"]} Directory {directory_name} created.')
    except FileExistsError or FileNotFoundError:
        print(f'{_flags_dict["flag_warning"]} Directory {directory_name} already exists, not created.')


def _create_app_dirs(tuple_app_dirs: tuple = _app_dirs) -> None:
    for directory in tuple_app_dirs:
        _create_dir(directory_name=f'app/{directory}')


def _create_file_config(file_content: list, dir_name: str = str(), file_name: str = str()) -> None:
    try:
        with open(f'{dir_name}/{file_name}', 'x') as file_config:
            file_config.writelines(file_content)
        print(f'{_flags_dict["flag_ok"]} File {_flags_dict["flag_file"](file_name)} created.')
    except FileExistsError or FileNotFoundError:
        print(f'{_flags_dict["flag_warning"]} File already exists {dir_name}\\{_flags_dict["flag_file"](file_name)},'
              f' not created.')


def _create_app_files_config(dict_app_files: dict = _app_files) -> None:
    for item in dict_app_files.items():
        _create_file_config(dir_name=item[1], file_name=item[0], file_content=_files_dict[item[0]])
