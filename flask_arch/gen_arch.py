from flask_arch.base_arch import _set_root_app, _make_view_dir, _make_templates_dir, _make_test_dir, _make_models_dir, \
    _make_utils_dir, _make_services_dir


def generate_mtv_arch():
    try:
        _set_root_app()
        _make_models_dir()
        _make_view_dir()
        _make_templates_dir()
        _make_test_dir()
        _make_utils_dir()
        _make_services_dir()
        print('Successfully generated MTV arch')
    except FileExistsError:
        print('Arquivos/Diretórios já existem')
