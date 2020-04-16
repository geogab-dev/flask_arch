from flask_arch.base_arch import _set_root_app, _make_layer_models_dir, _make_layer_view_dir,\
    _make_layer_templates_dir, _make_layer_utils_dir, _make_layer_services_dir, _make_layer_test_dir,\
    _write_basics_config, _make_layer_controller_dir


def generate_mtv_arch():
    """Esta função chama as funções base do arquivo base_arch.py para gerar a arquitetura MTV
    (MODELS - VIEWS - TEMPLATES)"""
    try:
        _set_root_app()
        _make_layer_models_dir()
        _make_layer_view_dir()
        _make_layer_templates_dir()
        _make_layer_test_dir()
        _make_layer_utils_dir()
        _make_layer_services_dir()
        _write_basics_config()
        print('\n[ \033[32mSUCCESS\033[0m ] Successfully generated MTV arch')
    except FileExistsError or FileNotFoundError:
        print('\n[ ERROR ] Unsuccessfully generated MTV arch')


def generate_mvc_arch():
    """Esta função chama as funções base do arquivo base_arch.py para gerar a arquitetura MVC
    (MODELS - VIEWS - CONTROLLERS)"""
    try:
        _set_root_app()
        _make_layer_models_dir()
        _make_layer_view_dir(is_mvc_arch=True)
        _make_layer_controller_dir()
        _make_layer_test_dir()
        _make_layer_utils_dir()
        _make_layer_services_dir()
        _write_basics_config(is_mvc_arch=True)
        print('\n[ \033[32mSUCCESS\033[0m ] Successfully generated MVC arch')
    except FileExistsError or FileNotFoundError:
        print('\n[ ERROR ] Unsuccessfully generated MVC arch')
