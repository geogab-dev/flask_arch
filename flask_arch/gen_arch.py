#!/usr/bin/python

from flask_arch.base_arch import _create_app_dirs, _create_app_files_config, _flags_dict
import sys

if sys.argv[0] == 'init' and len(sys.argv) == 2:
    generate_flask_arch()

def generate_flask_arch():
    try:
        _create_app_dirs()
        _create_app_files_config()
        print(f'\n{_flags_dict["flag_ok"]} Check your app template.')
    except FileExistsError or FileNotFoundError as e:
        raise e
